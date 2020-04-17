class Cart:

    def __init__(self, products):
        self.prod = products
        self.total = self.total()
        self.tot_eat = self.totally_eatable()

    def total(self):
        total = 0
        for prod in self.prod:
            total += prod.total_price
        return total

    def totally_eatable(self):
        for prod in self.prod:
            if not prod.eatable:
                return False
        return True


print('cart.py')
