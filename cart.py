class ShoppingCart:
    def __init__(self,quantity,price):
        self.products = []
        self.quantity = quantity
        self.price = price
    def add_item(self, product):
        # method to add a product to the shopping cart
        self.products.append(product)
    def remove_item(self, product):
        # method to remove a product from the shopping cart
        self.products.remove(product)
    def checkout(self, address, payment_method):
        self.adress =address
        self.payment_method = payment_method
        # method to complete the checkout process
        # verify user's address and payment information
        # pass
