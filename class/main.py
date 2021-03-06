import csv


class Item:
    pay_rate = 0.8  # pay rate after the discount is applied
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Running validation to the received arguments
        assert price >= 0, f'price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # Append the instance to the all list
        Item.all.append(self)

    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    # this decorator convert the function instance method to a class method
    @classmethod
    def instantiate_from_csv(cls):  # the cls is just  an argument that refers to the class rather than the instances
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)  # reads our contents as a least of dictionaries
            items = list(reader)  # converts the reader into a list and

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')))

    # static method should have a connection toe the class you are working with
    @staticmethod
    def is_integer(num):
        # We will count the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Used to display the list of instances
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


# imagine you have an Item phone with two instance of different price but same quantity
# if you have a type of phone that share the same attributes but has addition quirkes
# it it good practice into inherit from the Item class of the phone and add new attributes
# in this case the new attributes will be the phone is broken.

class Phone(Item):
    # without using the super, you have to copy nad paste the attributes from Item class into tthe child
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # The super() function all use to access the argument, datastructure all, and function
        # the parent function we simply need to add any additional attributes unique
        #to this class Phone.
        super().__init__(name, price, quantity)
        # Running validation to the received arguments
        assert broken_phones >= 0, f'Broken Phones {broken_phones} is not greater or equal to zero!'
        # Assign to self object
        self.broken_phones = broken_phones



phone1 = Phone('jscPhonev10', 500, 5, 1)
phone2 = Phone('jscPhonev10', 700, 5, 1)
print(Item.all)
print(Phone.all)