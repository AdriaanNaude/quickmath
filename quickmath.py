import random
import math

num1 = 0
num2 = 0

symbol = ""
symbol_list = ["*", "+", "-", "/"]

def check(num1, symbol, num2, answer):

    answer1 = "correct"
    answer2 = "incorrect"
    result = 0

    if symbol == "+":
        result = num1 + num2
    elif symbol == "-":
        result = num1 - num2
    elif symbol == "*":
        result = num1 * num2
    elif symbol == "/":
        result = num1 / num2

    if int(answer) == result:
        print(answer1)
    else:
        print("{0}: {1}".format(answer2, result))

def sum():
    while True:
        num1 = random.randrange(0,101)
        num2 = random.randrange(0,101)
        symbol =symbol_list[random.randrange(0,4)]

        if symbol == "*" or symbol == "/":
            num = random.randrange(1,13)

        print("{0}{1}{2}".format(num1, symbol, num2))
        answer = input("= ")
        check(num1, symbol, num2, answer)

sum()
