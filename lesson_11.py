#Створіть новий файл .py у пайчарм
#Імпортуй бібліотеку os
import os

#За допомогою бібліотеки os створіть дерикторію(папку) files
os.mkdir("files")

#Зміни поточну дерикторію на дерикторію files
os.chdir("files")

#Створи цикл котрий ітерує range від 1 до 10(не включно), в середині циклу створи 9 нових папок використовуючи числа, котрі повертає range
for i in range(10):
    os.makedirs("new_"+str(i))

#В будь-якій з тільки що створених папок створи TXT файл (руками, без використання бібліотек)
#Використай метод isfile та перевір створений файл.
print(os.path.isfile('/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject/files/new_1/newtxt.txt'))
#True - відповідь

#За допомогою бібліотеки os видали дерикторії з 7-9
for i in range(7,10):
  os.rmdir("new_"+str(i))