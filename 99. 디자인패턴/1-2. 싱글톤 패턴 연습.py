# 싱글톤 패턴 - 하나의 클래스에 하나의 인스턴스만 가지는 개념

class Singleton:
    _instance = None
    
    # 객체가 생성될때 쓰는 기본 __new__ 함수를 새로 정의
    # 원래 __new__ 함수는 기본제공인데 우린 싱글톤 패턴 써야하니 오버라이드
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
        