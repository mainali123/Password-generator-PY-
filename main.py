# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Shuffling all the characters of list
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

list = []  # Creating new list

count = 0
while (count < nr_letters):
    count += 1
    final_letters = random.choice(letters)  # generates random element
    list.append((final_letters))  # adding random letter into list
    # print(final_letters)

count = 0
while (count < nr_symbols):
    count += 1
    final_symbols = random.choice(symbols)
    list.append(final_symbols)
    # print(final_symbols)

count = 0
while (count < nr_numbers):
    count += 1
    final_numbers = random.choice(numbers)
    list.append(final_numbers)
    # print(final_numbers)

random.shuffle(list)  # final shuffling the list
Final_Password = ''.join(list)  # converting list into string
print(Final_Password)
