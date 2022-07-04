from ast import And
from typing import final


#1:
my_system = input('Insert your input here: ')
if my_system != False:
    print(my_system)
else:
    print(' Sorry! Your input is False! Try again...')

#2:
my_list = []
input_1 = input()
input_2 = input()
input_3 = input()
my_list.append(input_1, input_2, input_3)
for x in my_list:
    if x != False:
        print(my_list)
    else:
        print("Cannot print becasue one or more values in the list is false")


#3:
name = "Haseeb"
location = "Turin"
age = 26
final_list = []
question_1 = input("What is your name? : ")
question_2 = input("Where do you live? : ")
question_3 = input("How old are you? : ")
while True:
    question_1 == "Haseeb", 
    question_2 == "Turin",
    question_3 == 26
    print("All 3 answers are correct! You win!! creating list...")
    final_list.append(question_1, question_2, question_3)
    print(final_list)
else:
    print("Sorry! Your data is not entirely correct. Try again!") 

