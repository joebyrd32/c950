# Used to store package data
class Package:
    def __init__(self, address_id, address, city, state, zip_code, delivery_deadline, mass, delivery_status):
        self.address_id = address_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.delivery_status = delivery_status

    def __str__(self):
        return '{:<25}'.format(self.address) + '{:<18}'.format(self.city) + '{:<4}'.format(self.state) + \
                '{:<7}'.format(self.zip_code) + '{:<10}'.format(self.delivery_deadline) + \
                '{:<4}'.format( self.mass) + '{:<25}'.format(self.delivery_status)

    def __repr__(self):
        return self.__str__()
