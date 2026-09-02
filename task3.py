class Car:
    def __init__(self):
        self.engine_temperature = 20
    def start_engine(self):
        self.engine_temperature = 90
        print("Двигатель прогрет")
    def drive(self):
        if self.engine_temperature > 80:
            print("Машина едет")
        else:
            print("Сначала запустите двигатель")

car = Car()
car.drive()
car.start_engine()
car.drive()
