class item:
    def total(self, x, y):
        return x * y


item1 = item()
item1.name = "jeff"
item1.price = 10
item1.quantity = 3

cost = item1.total(item1.price, item1.quantity)

print(item1.name, " ", item1.price, ' ', item1.quantity)
print(cost)