# fruits = ['apple', 'orange', 'pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' Pie')

# students_height =  input("Enter students height: ").split(',')
# sum = 0
#
# print(students_height)
# for n in range(0, len(students_height)):
#     sum += int(students_height[n])
#
# average = sum / len(students_height)
# print(round(average, 0))


# student_scores = input("Enter students scores: ").split(',')
# big = int(student_scores[0])
#
# for n in range(0, len(student_scores)):
#    student_scores[n] = int(student_scores[n])
#    if student_scores[n] > big:
#        big = student_scores[n]
# print(big)
# print(student_scores)

#
# sum = 0
#
# for n in range(1,101):
#     if n%2 == 0:
#         sum+= n
#
# print(sum)

# for n in range(1,101):
#     if n % 3 == 0 and n % 5 !=0:
#         print('Fizz')
#     elif n % 3 !=0 and n % 5 ==0:
#         print('Buzz')
#     elif n% 3 == 0 and n% 5 == 0:
#         print('FizzBuzz')
#     else:
#         print(n)
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordList = []


for char in range(1, nr_letters + 1):

    passwordList +=  random.choice(letters)


for char in range(1, nr_numbers + 1):

    passwordList +=  random.choice(numbers)


for char in range(1, nr_symbols + 1):
    passwordList += random.choice(symbols)


random.shuffle(passwordList)

password = ""

for char in passwordList:
    password += char

print(f"Your password is: {password}")