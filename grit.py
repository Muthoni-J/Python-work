def greet(name):
    print(f"Hello {name}")
    return
def greet(*names):
    print(names)
    return
def greet(*names):
    for name in names:
        print(f"Hello {name}")

def greet_mutilple (**kwargs):
    print(kwargs)
    keys = kwargs.keys()
    values = kwargs.values()
    print(keys)
    print(values)

def greet_mutilple(**kwargs):
    keys = kwargs.keys()
    if "country" in keys:
        return f"Hello{kwargs["name"]} from {keys["country"]}
    elif "age" in keys:
        year = 2022 = kwargs["age"]
        return f "Hello{kwags['name' you were born in {year}"
    elif "name" in keys:
        return f "Hello"{kwargs['name']}
    else:
        return f "Hello Anonymous"

def func_name (*age,**kwargs):
def sum_and_greet(*age,**kwargs):
    print(age)
    print(kwargs)

        



 

