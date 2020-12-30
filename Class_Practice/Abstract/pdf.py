from document import Document

class PDF(Document):
    def show(self):
        return 'PDF ' + super().name() + ' say hello.'

class Word(Document):
    def show(self):
        return 'Word ' + super().name() + ' say hello.'

class Html:
    def __init__(self, name):
        self.__name = name

    def print(self):
        print("HTML: " + self.__name + ' say hello.')