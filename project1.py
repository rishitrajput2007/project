print("Welcome to the Interactive Personal Data Collector")
print()

n=input("Please enter your name: ")
m=int(input("Please enter your age: "))
a=float(input("Please enter your height in meters: "))
b=int(input("Please enter your favourite number: "))

print()

print("Thank you! Here is the information we collected:")

print()

print(f"Name: {n} (Type: {type(n)}, Memory Address: {id(n)})")
print(f"Age: {m} (Type: {type(m)}, Memory Address: {id(m)})")
print(f"Height: {a} (Type: {type(a)}, Memory Address: {id(a)})")
print(f"Favourite Number: {b} (Type: {type(b)}, Memory Address: {id(b)})")


print()

from datetime import datetime

current_year=datetime.now().year
birth_year=current_year-m

print(f"Your birth year is approximately: {birth_year} (based on your age of {m})")

print()

print("Thank you for using the personal data collector.Goodbye!")
