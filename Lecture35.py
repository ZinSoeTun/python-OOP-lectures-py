# Decorator = A function that extends the behavior of another function
#                      w/o modifying the base function
#                      Pass the base function as an argument to the decorator

def add_sprinkles(fun):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles🍿")
        fun(*args, **kwargs)
    return wrapper
    
def add_fudge(fun):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        fun(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(falvar):
    print(f"Here is your {falvar} ice cream")

get_ice_cream("vanilla")