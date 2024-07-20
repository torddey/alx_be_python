from book_class import Book

def main():
 
    my_book = Book("IDGAF", "Donald Trump", 1995)
    print(my_book)  # Expected to use __str__
    print(repr(my_book))  # Expected to use __repr__
    del my_book

if __name__ == "__main__":
    main()