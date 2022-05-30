# def hello():
#     print('Hello Joan...')

# def hello(name,age):
#     year=2022-age
#     return f "Hello"{name}you were born in {year}
# hello("Joan",20)
# hello("Sande",21)

def hello(name, age):
    year  = 2022 - age
    print(f"Hello {name} you were born in {year}")
# position argument
hello("Juma", 50)
hello("Saraa", 60)
# keyword argument
hello(name ="Joan",age=20)
hello(name ="Sande",age=21)
hello(age 20,name="Joan")
