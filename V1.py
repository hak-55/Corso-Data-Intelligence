class my_class:
    my_list = []
    nome = 'nome'
    surname = 'surname'
    age = 26
    profession = 'profession'

data = my_class()
data.nome = input('Enter your name: ')
data.surname = input('Enter your surname: ')
data.age = input('Enter your age: ')
data.profession = input('Enter your profession: ')

if type(data.nome == str):
    data.my_list.append(data.nome)
if type(data.age == int):
    data.my_list.append(data.age)
if type(data.surname == str):
    data.my_list.append(data.surname)
if type(data.profession == str):
    data.my_list.append(data.profession)

print(data.my_list)
