# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = ['Fedor', 354, 3.14, 'notebook']

length_my_list = len(my_list)

while length_my_list > 0:
    print(my_list[length_my_list-1], type(my_list[length_my_list-1]))
    length_my_list = length_my_list - 1
