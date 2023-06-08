#  Day_ 30 Constructors in Python .........................................................................................

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):  
#         print("move")

#     def draw(self):
#         print("draw")
 

# point = Point(10, 20)
# print(point.x)

# EXERCISE # 1: Make a class person wit two attributes name and talk 

# class Person:
#     def talk(self):
#         print("talk")
    
#     def name(self):
#         print("name")

# person = Person()
# person.talk()

# person = Person()
# person.name()

# Second method to write it using constructors

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk (self):
#         print("talk")

# person = Person("Haris")
# print(person.name)
# person.talk()

# Third method to write it using constructors and functions

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk (self):
#         print(f"Hi I am, {self.name} ")

# person1 = Person("Haris")
# person1.talk()

# person2 = Person("Shakir")
# person2.talk()
