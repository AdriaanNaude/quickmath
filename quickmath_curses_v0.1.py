import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import random

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
            stdscr.addstr(f"{answer1}")
        else:
            stdscr.refresh()
            stdscr.addstr(f"{answer2}: {result}")

    def sum():

        while True:
            stdscr.clear()
            
            num1 = random.randrange(0,101)
            num2 = random.randrange(0,101)
            symbol =symbol_list[random.randrange(0,4)]
            if symbol == "*" or symbol == "/":
                num1 = random.randrange(1,13)
            #stdscr.addstr(f"{num1}{symbol}{num2}")
            #win = curses.newwin(1,4,4,4)
            #box = Textbox(win)
            
            stdscr.addstr(f"{num1}{symbol}{num2}")
            stdscr.refresh()
            win = curses.newwin(1,4,1,1)
            box = Textbox(win)
            box.edit()
            answer = box.gather()
            #stdscr.addstr(f"= {answer}")
        
            #stdscr.getch()

            check(num1, symbol, num2, answer)
            stdscr.getch()
    sum()

wrapper(main)
