# 전략패턴
# 하나의 기능에 대해 여러가지 전략을 설정해놓고 런타임에 전략을 바꿀 수 있음

# 여러 전략들
class CardPayment:
    def pay(self, amount):
        print(f'{amount}원 만큼 카드 결제')

class CashPayment:
    def pay(self, amount):
        print(f'{amount}원 만큼 현금 결제')

# 전략 설정
class PaymentService:
    # __init__: __new__로 메모리에 생성된 객체에 속성(프로퍼티)을 세팅하는 함수
    # 여기서 strategy 속성을 주입받아서, 이후 checkout 등에서 사용할 수 있게 됨 
    def __init__(self, strategy):
        self.strategy = strategy # 전략을 초기값으로 주입받도록
    
    def checkout(self, amount):
        self.strategy.pay(amount) #위 __init__ 에서 전략들을 주입받았으므로 주입받은 전략의 pay 메서드를 사용 가능

# 테스트
card = PaymentService(CardPayment()) #CardPayment 객체가 먼저 생성되고, 해당 객체가 PaytmentServie의 전략으로서 주입됨 (초기값으로)
card.checkout(2000)
print(card.strategy)
