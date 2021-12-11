from Item import Item


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

