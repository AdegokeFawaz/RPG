rental_car = input("should I get you a Toyota?: ")
print(rental_car)
prompt = "If you tell us how many people in your group, we can personalize the messages you see."
prompt += "\nHow many people are in your group? "
name = input(prompt)
print(f"\nHello, {name}!")
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 6 == 0:
print(f"\nThe number {number} is even.")
else:
print(f"\nThe number {number} is odd.")
