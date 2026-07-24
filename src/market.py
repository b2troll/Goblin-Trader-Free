import random


class Market:
    def __init__(self):
        self.price = 10000

    def update_price(self):
        change = random.uniform(-0.02, 0.02)
        self.price = self.price * (1 + change)
        return round(self.price, 2)


if __name__ == "__main__":
    market = Market()

    for i in range(5):
        print(market.update_price())
