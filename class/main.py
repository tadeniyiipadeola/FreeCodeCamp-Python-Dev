class Item:
    pay_rate = 0.8  # pay rate after the discount is applied
    def __init__(self, name: str, price: float, quantity: int):
        # Running validation to the received arguments
        assert price >= 0, f'price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item('jeff', 10, 3)
cost = item1.total()

print(item1.name, " ", item1.price, ' ', item1.quantity)
print(cost)
# instance attributes vs Class attributes
# since Item1 instance couldn't find the pay_rate attribute the the instance attributes
# it moves to the class attribute to find if the pat_rate can be found and there it is.
print(Item.pay_rate)

print(Item.pay_rate)
print(Item.pay_rate)
print(Item.__dict__)  # All the attributes for class level
print(item1.__dict__)  # All the attributes for instance level
item1.apply_discount()
print(item1.price)
