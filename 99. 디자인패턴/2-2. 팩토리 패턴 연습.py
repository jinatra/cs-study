from abc import ABC, abstractmethod

# 1. 추상화 클래스 생성
class Animal(ABC):
    @abstractmethod
    def speak(self): # Animal 클래스들은 모두 speak라는 함수를 갖도록 강제적으로 추상화
        pass

# 2. 구체화 클래스 생성
class Dog(Animal):
    def speak(self):
        print('멍멍')

class Cat(Animal):
    def speak(self):
        return '야옹'

# 3. 팩토리 클래스
class AnimalFactory:
    def create_animal(self, type):
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            return "nono"

fac = AnimalFactory()
dog = fac.create_animal('dog')
dog.speak()