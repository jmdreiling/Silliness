import random

def comparison(guess, correct):
    diff = guess-correct
    if abs(diff) < 5 and abs(diff) > 0:
        print("Within 5 Degrees!")
    if diff > 0:
        print("Too high, try again")
    else:
        print("Too low, try again.")


def c_to_f(celsius_val):
    print(f"What is {celsius_val} Centigrade in Fahrenheit?")

    f_guess = int(input())
    f_correct = int((celsius_val * 1.8) + 32)

    while (f_guess != f_correct):
        comparison(f_guess, f_correct)
        print(f"What is {celsius_val} Centigrade in Fahrenheit?") 
        f_guess = int(input())
  
    print("good job, type that again as '__ C is __ F'")
    repeat_f = input()
    while (repeat_f != f"{celsius_val} C is {f_correct} F"):
        repeat_f = input()


def f_to_c(fahrenheit_val):
    print(f"What is {fahrenheit_val} Fahrenheit in Centigrade?")
 
    c_guess = int(input())
    c_correct = int((fahrenheit_val - 32) * (5/9))

    while (c_guess != c_correct):
        comparison(c_guess, c_correct)
        print(f"What is {fahrenheit_val} Fahrenheit in Centigrade?")
        c_guess = int(input())
   
    print("good job, type that again as '__ F is __ C'")
    repeat_c = input()
    while (repeat_c != f"{fahrenheit_val} F is {c_correct} C"):
        repeat_c = input()



