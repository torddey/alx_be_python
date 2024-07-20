# Exercise 1: Constructors and Destructors Instructions:
# •	Create a Person class with attributes like name and age. Implement a constructor (__init__) to initialize these attributes.
# •	Also, implement a destructor (__del__) method to print a farewell message when an object is deleted.

# Exercise 2: Magic Methods (str and repr) Instructions:
# •	Create a Book class with attributes like title, author, and pages.
# •	Implement both __str__ and __repr__ magic methods to provide different string representations of the book object.

# Exercise 3: Class Inheritance Instructions:
# •	Create a base class Animal with methods like eat and sleep.
# •	Create a subclass Dog that inherits from Animal and adds a method bark.
# •	Create instances of both classes and demonstrate method inheritance.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __del__(self):
        return f"This object has been deleted"

person1 = Person("James", 36)
print(person1)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"The book {self.title}, written by {self.author} has {self.pages} pages"

    def __repr__(self):
        return "New Book"

book1 = Book("IDGAF","Trump", 208)
print(book1)


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name is sleeping}")

    def __str__(self):
        return(f"Dog name: {self.name}")

  
class Dog(Animal):
    def __init__(self, name,):
        super().__init__(name)  # Call parent class constructor
    
    def make_sound(self):
        print(f"{self.name} is Barking!")


dog = Dog("Rodeo")
print(dog)
dog.make_sound()
