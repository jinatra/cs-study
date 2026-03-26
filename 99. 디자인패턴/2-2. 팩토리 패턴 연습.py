class Americano:
    def serve(self):
        return "아아 나왔어용"

class Latte:
    def serve(self):
        return "라떼 나왔어용"

def coffee_factory(coffee_type):
    if coffee_type == "americano":
        return Americano()
    elif coffee_type == "latte":
        return Latte

drink = coffee_factory("americano")
print(drink.serve())
