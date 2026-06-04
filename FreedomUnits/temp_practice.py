import random
import temp_functions

print("Would you like to test baking temps or daily temps? (b/d)")
user_input = input()

if user_input == "b":
    celsius_list = list(range(100,350,25))
    celsius_val = random.choice(celsius_list)

    fahrenheit_list = list(range(200,500,25))
    fahrenheit_val = random.choice(fahrenheit_list)
else:
   celsius_val = random.randint(-40,45)
   fahrenheit_val = random.randint(-20,110)

temp_functions.c_to_f(celsius_val)
temp_functions.f_to_c(fahrenheit_val)
quit()
