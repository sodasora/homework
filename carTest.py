class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color
        self.speed=0
    def accelerate(self):
        self.speed += 10
    def brake(self):
        self.speed -= 10
    def get_speed(self):
        return self.speed

    
my_car = Car("소나타","빨간색")

print(my_car.color)

my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.brake()
my_speed = my_car.get_speed()
print(my_speed)