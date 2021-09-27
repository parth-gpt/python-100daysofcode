# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#
# add(1, 2, 3, 4, 5)

# def calculate(n, **kwargs):
#     print(kwargs)
#     # for (key, value) in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=4)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Ford")
print(my_car.model)
