import tiktoken
enc=tiktoken.encoding_for_model("gpt-4o")
text="Hey there! My name is Bakugo"

# Tokenize the text
tokens=enc.encode(text)
print("Tokens:", tokens) 

decoded_text=enc.decode(tokens)
print("Decoded Text:", decoded_text)