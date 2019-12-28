#################################################################
# Module defining some classes and methods for my librairy      #
#                           management                          #
# author : SINGBO Israel                                        #
#   e-mail: sisra1993@yahoo.fr                                  #
#   tel   : +22997816156                                        #
# date : 16/11/2019                                             #
#################################################################

# *-* coding:utf-8 *-*

class Library:
    def __init__(self, name=None, number_of_books=0, manager=None):
        self.name=name
        self.number_of_books = number_of_books
        self.manager = manager

class Book:
    def __init__(self, reg_number=None, name=None,
                 author=None, price=None, isbn=None,
                 classe=None, num_user=None, status=1):
        self.reg_number = reg_number
        self.name = name
        self.author = author
        self.price = price
        self.isbn = isbn
        self.classe = classe
        self.status = status
        self.num_user = num_user

    #Defining getters

    def get_reg_num(self):
        return self.reg_number

    def get_name(self):
        return self.name
    
    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def get_isbn(self):
        return self.isbn

    def get_classe(self):
        return self.classe

    def get_status(self):
        return self.status

    def get_num_user(self):
        return self.num_user

    # definig setters

    def set_reg_num(self, reg_num):
        self.reg_num = reg_num

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_classe(self, classe):
        self.classe = classe

    def set_status(self, status):
        self.status = status

    def set_num_user(self, num_user):
        self.num_user = num_user

    def set_values(self, reg_number=None, name=None,
                 author=None, price=None, isbn=None,
                 classe=None, num_user=None, status=1):
        self.__init__(reg_number, name,
                 author, price, isbn,
                 classe, num_user, status)

class User:
    def __init__(self, name=None, mle=None, books_reads=[]):
        self.name = name
        self.mle = mle
        self.books_read = books_read

    def get_attributs(self):
        return {'name':self.name, 'mle':self.mle, 'books_read':books_read}

    def add_book_read(self, book_reg_num):
        self.books.append(book_reg_num)





        
        
