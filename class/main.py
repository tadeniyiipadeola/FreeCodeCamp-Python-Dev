class item:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


item1 = item('jeff', 10, 3)
cost = item1.total()

print(item1.name, " ", item1.price, ' ', item1.quantity)
print(cost)
