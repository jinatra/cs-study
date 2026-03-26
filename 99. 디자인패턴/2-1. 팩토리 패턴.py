# 팩토리 패턴: 객체 생성을 하위 클래스에 맡기는 패턴

# --- 음료 클래스들 (만들어질 객체들) ---
class Americano:
    def serve(self):
        return "아메리카노 나왔습니다"

class Latte:
    def serve(self):
        return "라떼 나왔습니다"

# --- 팩토리 (객체를 대신 만들어주는 함수) ---
def coffee_factory(coffee_type):
    if coffee_type == "americano":
        return Americano()
    elif coffee_type == "latte":
        return Latte()

# --- 사용 ---
drink = coffee_factory("americano")  # "아메리카노 하나 주세요"
print(drink.serve())  # "아메리카노 나왔습니다"