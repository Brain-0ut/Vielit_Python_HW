# coding: utf-8

from Lesson15.product import Product
from Lesson15.cart import Cart

prod_cat = ('hh_chemical', 'food', 'alcohol')
units = ('peaces', 'kg', 'liters')
prod1 = Product(15.0, prod_cat[1], 'Bread', 2, units[0])
prod2 = Product(458.95, prod_cat[2], 'Jameson Whisky', 1, units[2])
prod3 = Product(89.38, prod_cat[0], 'Washing powder', 4, units[1])
prods=(prod1, prod2, prod3)

for prod in prods:
    print(f'Is the {prod.prod_name} eatable: {prod.eatable},\n'
          f'The price for {prod.quantity} {prod.units} of {prod.prod_name} is {prod.total_price}')

cart = Cart(prods)
print('\nTotal price for all goods in your cart: ', cart.total)
print('The all goods in cart is eatable: ', cart.tot_eat)
print('Total goods in cart: ', Product.prodCount)