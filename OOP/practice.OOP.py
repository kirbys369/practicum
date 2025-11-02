class Customer:
    def __init__(self, name):
        self.name = name
        self.__discount = 10

    def get_price(self, price) -> float:
        return round(price - (price * self.__discount / 100), 2)

    def set_discount(self, value):
        if value <= 80: self.__discount = value
        else: self.__discount = 80


customer = Customer("Иван Иванович")
print(type(customer.get_price(100)))
print(type(round(12.123132, 2)))
customer.set_discount(20)
print(customer.get_price(100))
