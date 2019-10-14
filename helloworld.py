def Helloword():
    print("hello world")


Helloword()


def Greeting(name):
    print("hi" + name + "!")


Greeting("deepthi")


def Add(num1, num2):
    print(num1 + num2)


Add(10, 15)


def returnAdd(num1, num2):
    return (num1 + num2)


sum = returnAdd(45, 34)
print(sum)


class car:
    def __init__(self, model, type):
        self.model = model
        self.type = type

    def carmake(self):
        print("the car model is " + self.model)
    def cartype(self):
        print("the type of the car is " + self.type)

p = car("audi", "auto")
p.carmake()
p.cartype()

