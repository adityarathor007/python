from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        func(*args, **kwargs)
        print(f"Ending: {func.__name__}")
    return wrapper



@log_activity # prepare_tea = log_activity(prepare_tea)
def prepare_tea(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")


prepare_tea("Masala")
prepare_tea("Tandoor","yes")
