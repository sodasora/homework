class Animal:
    def __init__(self,name, age):
        self.name = name
        self.age=age
    def speak(self):
        print("The animal speaks")
    
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed
    def speak(self):
        print("멍멍")

class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("야옹")

cute_dog = Dog("존","9","포메라니안")
cute_dog.speak()

cute_cat = Cat("나비","7",'white')
cute_cat.speak()