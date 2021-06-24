from CursoPOOUber.Python.car import Car
from CursoPOOUber.Python.account import Account

if __name__ == "__main__":
    print("Hello world!")
    car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))
