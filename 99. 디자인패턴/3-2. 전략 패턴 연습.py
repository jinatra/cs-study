# 전략패턴: 한 기능에 대해서 여러 방법(전략)이 가능할때 사용 (캡슐화된 알고리즘)

# 여러 결제 방법
class CashPayment:
    def pay(self, amount):
        print(f'현금결제로 {amount}원 사용')

class CardPayment:
    def pay(self, amount):
        print(f'카드결제로 {amount}원 사용')

# 실제 전략패턴이 구현되는곳
class PaymentService:
    # 객체에 초기값 할당될때 어떤 전략이 할당될지 선택
    def __init__(self, strategy):
        self.strategy = strategy
    
    def checkout(self, amount):
        self.strategy.pay(amount)

service = PaymentService(CardPayment())
service.checkout(10000)