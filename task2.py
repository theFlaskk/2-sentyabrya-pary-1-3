class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
    def draw(self): 
        print(f"На экране рисуется кот {self.name}, порода {self.breed}")
cat1= Cat("Siamese", "Whiskers", 3)
cat2= Cat("Persian", "Fluffy", 5)
cat3= Cat("Maine Coon", "Shadow", 2)

cat1.draw()
cat2.draw()
cat3.draw()
