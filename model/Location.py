# To store addresses
class Location:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return self.address

    def __repr__(self):
        return self.__str__()
