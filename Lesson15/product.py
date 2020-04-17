class Product:

    prodCount = 0

    def __init__(self, price, cat, prod_name, quantity, units):
        self.price = price
        self.cat = cat
        self.prod_name = prod_name
        self.quantity = quantity
        self.units = units
        self.eatable = self.is_eateble()
        self.total_price = self.price_total(self.quantity)
        Product.prodCount += 1

    def is_eateble(self):
        if self.cat != 'hh_chemical':
            return True
        return False

    def price_total(self, count):
        return self.price*count


print('product.py')
