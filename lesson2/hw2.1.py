#Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.#
my_str = 'строка'
list = (1, 2, 3, 4)
tuple = (5, 6, 7, 8)
print(type(my_str))
print(type(list))
print(type(tuple))


#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
my_list = input("Введите элементы списка: ").split()

for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)

#Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
weather_list = ['Зима', 'Весна', 'Лето', 'Осень']
weather_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите номер месяца-> "))
if month ==12 or month == 1 or month == 2:
        print(weather_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(weather_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(weather_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(weather_dict.get(4))
else:
        print("Введите номер от 1 до 12")