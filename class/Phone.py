
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

