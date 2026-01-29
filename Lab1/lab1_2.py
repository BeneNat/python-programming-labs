from datetime import date

inputs = [i for i in input("Please provide your name, surname and the year of birth (Filip Zurek 2002): ").split()]
for i in inputs:
    i = i.strip()

#if not len(inputs) == 3 or isinstance(inputs[2], int):
if not len(inputs) == 3:
    print("You need to enter the 3 value and the year must be the number!")
else:
    current_year = date.today().year
    print("Hello", inputs[0], inputs[1], "you're approximately", current_year - int(inputs[2]), "years old.")


