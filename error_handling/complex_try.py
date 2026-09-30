# [try except else finally]
def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor=="unknown":
            raise ValueError("We dont know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else: #executed if did not fell into exception
        print(f"{flavor} is served")
    finally:
        print("Next Customer please") #irrespective of what happens above this executes 


serve_chai("Masala")
serve_chai("unknown")
