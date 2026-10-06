from openai import OpenAI
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

# --------------------------------------------------------------
# Available tools for the agent
# --------------------------------------------------------------
def get_weather(city: str) -> str:
    """
    Fetches the current weather (condition + temperature) for a given city
    using wttr.in.

    Args:
        city: City name as a string.

    Returns:
        A short human-readable weather summary, e.g. "Cloudy 20C".
    """
    city_lower = city.lower()
    url = f"https://wttr.in/{city_lower}?format=%C+%t"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.text.strip()


# Map tool names to callable implementations.
AVAILABLE_TOOLS = {
    "get_weather": get_weather,
}

SYSTEM_PROMPT = (
    "You're an AI assistant resolving queries using Chain-of-Thought (CoT).\n"
    "You work in a sequence of steps: START, PLAN (which may repeat multiple times), OBSERVE, TOOL, and finally OUTPUT.\n\n"
    "Rules:\n"
    "- Strictly follow the given JSON output format.\n"
    "- Only run one step at a time.\n"
    "- The sequence of steps is START (where the user gives input), PLAN (which can happen multiple times), and OUTPUT.\n"
    "- You must first PLAN what needs to be done. The PLAN can be multiple steps.\n"
    "- Once you think enough planning has been done, finally you can give an OUTPUT.\n"
    "- You can also call a tool if required from the list of available tools.\n"
    "- For every tool call, wait for the OBSERVE step (the output from the called tool) before proceeding.\n\n"
    
    
    "Output JSON format:\n"
    '{"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string"}\n\n'
   
   
    "Available tools:\n"
    "- get_weather(city): get the current weather (condition and temperature) for a city. Example: get_weather with input 'delhi'.\n\n"
    
    
    "Example interaction:\n"
    "START: What is the weather of Delhi?\n"
    'PLAN: {"step": "PLAN", "content": "The user wants the weather for Delhi, so I will call the get_weather tool."}\n'
    'PLAN: {"step": "TOOL", "tool": "get_weather", "input": "delhi"}\n'
    'PLAN: {"step": "OBSERVE", "tool": "get_weather", "output": "The temp in delhi is cloudy with 20C"}\n'
    'PLAN: {"step": "PLAN", "content": "I have the weather information for Delhi; I can now compose the final answer."}\n'
    'PLAN: {"step": "TOOL", "content": "Great, I got the weather info about delhi"}\n'
    'OUTPUT: {"step": "OUTPUT", "content": "The weather in Delhi is cloudy with a temperature of 20C."}\n'
)


def main():
    # Message history must always end with a "user" turn when we call the API,
    # because Gemini rejects requests ending with an assistant turn.
    message_history = []
    prompt = (
        "That was a good plan. What is the next step? "
        "If you need to call a tool, make the TOOL call now. "
        "If you have enough information, give your OUTPUT."
    )

    while True:
        # If history doesn't end with a user turn, fetch fresh input (the START phase).
        if not message_history or message_history[-1].get("role") != "user":
            user_query = input("-> ")
            message_history.append({"role": "user", "content": user_query})

        response = client.chat.completions.create(
            model="gemini-3.5-flash-lite",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + message_history,
            temperature=0.0,
        )

        assistant_message = response.choices[0].message.content
        print("🤖:", assistant_message)

        try:
            parsed_result = json.loads(assistant_message)
        except json.JSONDecodeError as e:
            print("⚠️ Failed to parse assistant output as JSON:", e)
            message_history.append({"role": "user", "content": assistant_message})
            continue

        step = parsed_result.get("step")

        if step in ("START", "PLAN"):
            message_history.append({"role": "assistant", "content": assistant_message})
            message_history.append({"role": "user", "content": prompt})
            continue

        if step == "OUTPUT":
            message_history.append({"role": "assistant", "content": assistant_message})
            print("📝 Final output:", parsed_result.get("content"))
            break

        if step == "TOOL":
            tool_to_call = parsed_result.get("tool")
            tool_input = parsed_result.get("input")

            if not tool_to_call or tool_to_call not in AVAILABLE_TOOLS:
                if not tool_to_call:
                    print("⚠️ TOOL step missing a tool name; asking model to continue.")
                else:
                    print(f"⚠️ Unknown tool: {tool_to_call}")
                message_history.append({"role": "user", "content": assistant_message})
                message_history.append({"role": "user", "content": prompt})
                continue

            print(f"🛠️ tool_call: {tool_input}")
            tool_response = AVAILABLE_TOOLS[tool_to_call](tool_input)
            print("🛠️ tool_response:", tool_response)

            observe_entry = {
                "step": "OBSERVE",
                "tool": tool_to_call,
                "input": tool_input,
                "output": tool_response,
            }
            message_history.append({"role": "user", "content": json.dumps(observe_entry)})
            message_history.append({"role": "user", "content": prompt})
            continue

        # Unknown step type; default to continuing.
        message_history.append({"role": "user", "content": assistant_message})
        print(f"⚠️ Unknown step: {step}")
        continue


if __name__ == "__main__":
    main()
