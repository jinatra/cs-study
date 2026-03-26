from abc import ABC, abstractmethod

# 추상화 클래스
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
# 구체화 클래스
class Dog(Animal):
    def speak(self):
        print('멍멍')

class Cat(Animal):
    def speak(self):
        print('야옹')
        
# 팩토리 클래스
class AnimalFactory:
    def create_animal(self, type) -> Animal:
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            return "없는 동물타입"

# 구현
factory = AnimalFactory()
my_dog = factory.create_animal('dog')
my_dog.speak()

