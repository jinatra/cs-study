# 팩토리패턴
# 객체 생성 책임을 하나의 클래스(팩토리)에 일임하여 클라이언트에서 각 객체별 생성 로직을 알지 않아도 되게 (팩토리 하나만 있으면 객체생성 할 수 있도록)

from abc import ABC, abstractmethod

# 추상클래스
# 추상 -> 세부사항을 숨기고 뭘 할 수 있는지만 정의
# 객체들이 같은 메서드를 가진다는 것을 보장하기 위해 사용
# 추상클래스임을 명시하기 위해 ABC 설정
class Animal(ABC):
    # 추상메서드를 설정하여 Animal 클래스를 상속받는 객체들은 speak 함수가 있도록 강제
    @abstractmethod
    def speak(self):
        pass

# 구체클래스
class Dog(Animal):
    def speak(self):
        print('walf')

class Cat(Animal):
    def speak(self):
        print('meow')

# 팩토리 클래스
class AnimalFactory:
    # 객체 생성 함수 설정
    def create_animal(self, type:str) -> Animal:
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            raise ValueError()

# 테스트
factory = AnimalFactory()
my_cat = factory.create_animal('cat')
my_cat.speak()