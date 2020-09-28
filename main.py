print("Guess a number between 1 and 10:")
number = int(input())
if number == 7:
    print("You got it!")
elif number < 7:
    print("Higher")
else:
    print("Lower")