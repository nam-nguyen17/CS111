import json
from product import Product

class Store:
    def __init__(self, fname):
        self.__listofproduct = []
        
        with open(fname) as f:
            data = json.load(f)
            
            for b in data['books']:
                self.__listofproduct.append(Product(isbn=b['isbn'],
                                                    title=b['title'],
                                                    subtitle=b['subtitle'],
                                                    author=b['author'],
                                                    publisher=b['publisher'],
                                                    pub_date=b['publisher'],
                                                    pages=b['pages'],
                                                    description=b['description'],
                                                    website=b['website'],
                                                    total_num=b['total_num'],
                                                    current_num=b['current_num'],
                                                    price=b['price']))

    def list_product(self):
        for b in self.__listofproduct:
            print(b + '\t' + str(b.total_value()))

    def search(self, keyword):
        results = []
        for b in self.__listofproduct:
            if b.contain(keyword, field='title'):
                results.append(b)

        return results

    def get_product_by_isbn(self, isbn):
        for b in self.__listofproduct:
            if b.get_isbn() == 'isbn':
                return b
        
        return None

    def get_amount(self):
        return sum([b.total_value for b in self.__listofproduct])


    def save(self):
        pass