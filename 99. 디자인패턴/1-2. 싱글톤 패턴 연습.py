# 하나의 클래스에 하나의 인스턴스만 생성

class Singleton:
    _instance = None
    
    # 객체 생성 로직 오버라이드
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
    return _instance