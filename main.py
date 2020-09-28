print("What is your name?")
name = input().lower()
if name == "anakin":
  print("How do you do Anakin!")
else:
  print(f"Nice name, {name}")
print(f"So {name}, is it hot or cold where you are today?")
weather = input().upper()
if weather == "COLD":
  print("You must be freezing!")
elif weather == "HOT":
  print("Drink plenty of water")
else:
  print("I can't advise you on that type of weather.")
print("Do you like the colour blue?")
likes_blue = input().lower()
if likes_blue == "yes":
  print("I like blue too")
print("Do you like dogs or cats?")
dogsorcats = input().lower()
if dogsorcats == "dogs":
  print("I like dogs too!")
elif dogsorcats == "cats":
  print("Cats are cute but I prefer dogs.")
else:
  print("That wasn't dogs or cats...")
print("Have a good day! Bye!")