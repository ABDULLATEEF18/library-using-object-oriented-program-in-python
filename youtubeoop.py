
# implement functions to transfer money to a friend and buy books with the money.
#try using other oop concepts e.g inheritance and co.
class Booknotfound(Exception):
    pass
class depositt(Exception):
     pass
class Librarymanager:
    def __init__(self, user_name):
        self.user_name = user_name
        self.balance = 0
        #self.price = book_price
        #self.books = books
        self.listss = {'lati mi':20, 'hunter man':10, 'the rare hunter':30,'akin olu':50}
        self.borrowed = []
    def borrowed_books(self):
        print(f"\n the books {self.user_name} borrowed are \n{self.borrowed}")
    def borrow_books(self, books):
        #for i in self.listss:
            if books in self.listss:
                self.borrowed.append(books)
            else:
                raise Booknotfound("We do not have this book in our library! ")   
    def withdraw_books(self, books):
         if books in self.borrowed:
              self.borrowed.remove(books)
         else:
            raise Booknotfound("book not found in your borrowed list!..... ") 
    def deposit(self, amount):
         if amount > 0:
              self.balance += amount
         else:
              raise depositt(f"please deposit has to be above $0.") 
class buy_books(Librarymanager):
    #def __init__(self, book_to_buy):      
    def buy_book(self, book_to_buy):
         self.book = book_to_buy
         if self.balance > 0:
              if self.book in self.listss:
                   self.price = self.listss[self.book]
                   if self.balance > self.price:
                        self.borrowed.append(self.book)
                        self.balance = self.balance - self.price
                        #self.borrow_books()
                   else:
                        print(f"sorry {self.user_name} you dont have enough cash, make a deposit instead.")   
              else:
                   print("book isnt available.")  
         else:
              print(f"hello {self.user_name} a deposit has to be made to buy books.")

         
         
         
        