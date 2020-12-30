from abc import ABC, abstractmethod

class Document:
    def __init__(self, name):
        self.__name = name
    
    def name(self):
        return self.__name

    @abstractmethod
    def show(self):
        pass
        # raise NotImplementedError("This type is abstract")