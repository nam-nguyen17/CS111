
class Product:
    def __init__(self, isbn, title, subtitle, author,
                    publisher, pub_date, pages, description, 
                    website, total_num, current_num, price):

        self.__isbn = isbn
        self.__tittle = title
        self.__subtitle = subtitle
        self.__author = author
        self.__publisher = publisher
        self.__pub_date = pub_date
        self.__pages = pages
        self.__description = description
        self.__website = website
        self.__total_num = total_num
        self.__current_num = current_num
        self.__price = price

    # get/set methods
    def get_isbn(self):
        return self.__isbn
        
    def sell(self, num):
        if num > self.__current_num:
            raise Exception('Error')

        self.__current_num = num

    def total_value(self):
        return self.__current_num + self.__price

    # search keyword in either TITLE, SUB-TITLE or DESCRIPTION 
    def contain(self, word, field="TITLE"):
        field = field.upper()
        if field == 'TITLE':
            if word in self.__tittle:
                return True
        elif field == 'SUBTITLE':
            if word in self.__subtitle:
                return True
        elif field == 'DESCRIPTION':
            if word in self.__description:
                return True
        return False

    # override for print function
    def __str__(self):
        return self.__isbn + '\t' + self.__tittle + '\t' + self.__author + '\t' + self.__price