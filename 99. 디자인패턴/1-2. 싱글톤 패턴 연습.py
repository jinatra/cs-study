# 싱글톤 패턴: 하나의 클래스가 하나의 인스턴스만을 가짐

class Singleton:
    _instance = None #클래스 내 인스턴스 현재 없는 상태
    
    # 기본적으로는 __new__ 함수는 선언될때마다 새 객체 생성하지만,
    # 이번에는 싱글톤이므로 새롭게 오버라이드
    def __new__(cls):
        if cls._instance is None: #클래스의 인스턴스가 없으면
            cls._instance = super().__new__(cls) #  super()라는 부모함수 가져와서 새로운 인스턴스 생성
        return cls._instance # 이로인해 무조건 하나의 인스턴스만 반환

a = Singleton()
b = Singleton()

print(a is b) # 같은 인스턴스니까 True

class Dif:
    pass

c = Dif()
d = Dif()
print(c is d)