from pdf import PDF, Word, Document, Html

#function
def show_common(obj):
    if type(obj) == PDF:
        print(obj.show())
    elif type(obj) == Word:
        print(obj.show())
    elif type(obj) == Html:
        obj.print()
    elif type(obj) == Document:
        print(obj.show())
        # print(obj.name() + ' is an abstract class. Cannot say anything!')

docs = [PDF('Doc1'), Word('Doc2'), Document('Doc3'), Html('Doc4')]
for d in docs:
    # print(d.show())
    show_common(d)