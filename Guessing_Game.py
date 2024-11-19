import random
user=input("Enter your mode of play:")
if user=="user":
    print("you need to guess the number choosen by the machine")
    print("After each guess, the machine will tell weather it is too high or low or correct")
    low=int(input("set the lower range:"))
    high=int(input("set the upper range:"))
    number_of_guess=random.randint(low,high)
    atmp=0
while True:
 guess=int(input(f"guess number between {low}and{high}:"))
 atmp+=1
 if guess < number_of_guess:
     print("The guess number is too low")
     low=guess+1
 elif guess > number_of_guess:
     print("The guess number is too high")
     high=guess-1
else:
     print("your guess is corret")
    
