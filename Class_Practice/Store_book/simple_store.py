from product import Product
from store import Store

# p = Product(isbn='9781593275846', 
#             title='Eloquent JavaScript, Second Edition',
#             subtitle='A Modern Introduction to Programming',
#             author='Marijn Haverbeke',
#             publisher='No Starch Press',
#             pub_date='2014-12-14T00:00:00.000Z',
#             pages=472,
#             description="JavaScript lies at the heart of almost every modern web application, from social apps to the newest browser-based games. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
#             website='http://eloquentjavascript.net/',
#             total_num=10,
#             current_num=10,
#             price=100)

# print(p)
# print(p.contain('Take', field='description'))

s = Store('book.json')
results = s.search('Java')
for p in results:
    print(p)

print(s.get_amount())
# s.get_product_by_isbn()
