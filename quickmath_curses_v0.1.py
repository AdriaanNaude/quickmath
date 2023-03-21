import curses
from curses import wrapper
from curses.textpad import Textbox
import random
import keyboard

num1 = 0 
num2 = 0
symbol = ""
symbol_list = ["*", "+", "-", "/"]

def main(stdscr):

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
            stdscr.refresh,()         
            stdscr.addstr(11, 48, f"{answer1}")
        else:
            stdscr.refresh()
            stdscr.addstr(11, 47, f"{answer2}: {result}")

    def sum():

        while True:
            stdscr.clear()
            
            num1 = random.randrange(0,101)
            num2 = random.randrange(0,101)
            symbol =symbol_list[random.randrange(0,4)]
            if symbol == "*" or symbol == "/":
                num1 = random.randrange(1,13)
            
            stdscr.addstr(9, 49, f"{num1}{symbol}{num2}")
            stdscr.refresh()
            win = curses.newwin(1,4,10,50)
            box = Textbox(win)
            box.edit()
            answer = box.gather()



            check(num1, symbol, num2, answer)
            stdscr.getch()
    sum()

wrapper(main)
