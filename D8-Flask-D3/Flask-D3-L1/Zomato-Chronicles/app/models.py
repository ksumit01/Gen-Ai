class MenuItem:
    def __init__(self, dish_name, price, available=True):
        self.dish_name = dish_name
        self.price = price
        self.available = available

class OrderItem:
    def __init__(self, dish_id, status):
        self.dish_id = dish_id
        self.status = status

class Order:
    def __init__(self, customer_name, dishes):
        self.customer_name = customer_name
        self.dishes = dishes
