class Author:
    all = []

    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        return [cont for cont in Contract.all if cont.author == self]

    def books(self):
        return [cont.book for cont in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        royal = [cont.royalties for cont in Contract.all if cont.author == self]
        ans = sum(royal)
        return ans


class Book:
    all = []

    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [cont for cont in Contract.all if cont.book == self]

    def authors(self):
        return [cont.author for cont in self.contracts()]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if type(author) is Author:
            self.author = author
        else:
            raise Exception("Error")

        if type(book) is Book:
            self.book = book
        else:
            raise Exception()

        if type(date) is str:
            self.date = date
        else:
            raise Exception()
        
        if type(royalties) is int:
            self.royalties = royalties
        else:
            raise Exception()

        Contract.all.append(self)

    def contracts_by_date():
        Contract.all.sort(key= lambda obj : obj.date)
        return Contract.all