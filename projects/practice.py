from collections import deque
#Enum

# from enum import Enum

# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1

# print(State.ACTIVE.value)

#List

# dogs = ["Teddy",25,"Keerthi",32]
# print(dogs)
# dogs.append(True)
# print(dogs)
# lists = ["Loki",24,"Maybe Interested","Meteor 650"]
# dogs.extend(lists)
# print(dogs)
# dogs.insert(2,"Doesn't know this person")
# print(dogs)
# dogs.remove("Teddy")
# print(dogs)
# dogs.pop(1)
# print(dogs)
# dogs.append("Thomas")
# print(dogs)
# dogs.pop()
# print(dogs)
# index=dogs.index("Keerthi")
# print(f"The index of Keerthi is {index}")
# dogs.append("Thomas")
# dogs.append("Thomas")
# print(dogs)
# print(dogs.count("Thomas"))
# dog=[1,847,922,2,3,-9,-8439]
# print(sorted(dog))
# print(dog)
# dog.sort()
# print(dog)
# dogs.reverse()
# print(dogs)
# dogs_copy = dogs[:]
# print(dogs_copy)
# queue = deque(dogs_copy)
# queue.popleft()
# print(list(queue))

x = 5
# squares = []
# for x in range(1,11):
#     squares.append(x**2)

# print(squares)
# print(x)
#squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(1,11)]
# print(squares)
# print(x)

# vec = [-4,-2,0,2,4]
# vec = list(filter(lambda x: x>=0 , vec))
# print(vec)

# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(b)
# print(a | b)
# print(a & b)
# print(a ^ b)
# print(a - b)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# print(dict(zip(questions,answers)))
# for q, a in zip(questions, answers):
#     print(f'What is your {q}?  It is {a}.')

# def hello(name = "my friend"):
#     print('Hello from hello() function! ' + name)


# hello("and it's keerthana")
# hello()

# def talk(phrase):

#     def printWord(word):
#         print(word)

#     words = phrase.split(" ")
#     for word in words:
#         printWord(word)

# talk("hello world this is a test")

# import argparse

# parser  = argparse.ArgumentParser(
#     description="This program prints Hello World if no argument given."
#     )
# parser.add_argument('-w', '--word', metavar='word', required=True, choices={"Keerthi", "Reddy"}, help='the word to given  argument for')

# args = parser.parse_args()
# print(args.word)

# lambda num : num % 2 == 0
# numbers = [1, 2, 3]
# result = map(lambda num : num % 2 == 0, numbers)
# print(list(result))

# from functools import reduce

# expenses = [
#     ("Grocery", 120),
#     ("Rent", 670)

# ]

# sum = reduce(lambda a, b : a[1] + b[1], expenses)
# print(sum)

