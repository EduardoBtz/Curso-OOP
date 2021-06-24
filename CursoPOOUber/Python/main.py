from car import Car

if __name__ == "__main__":
    print("Hello world!")
    car = Car()
    car.license = "AMS1233"
    car.driver = "Jesus Orjle"
    print(vars(car))

    car2 = Car()
    car2.license = "JJK123"
    car2.driver = "Carlos Bella"
    print(vars(car2))
   
