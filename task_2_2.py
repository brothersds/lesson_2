# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = []
user_values = input('Введите элементы чрез пробел: ', )
user_list = user_values.split(" ")
length_user_list = len(user_list)
print(length_user_list)
final_list = []
for i in range(0, length_user_list // 2):
    final_list.append(user_list[2*i+1])
    final_list.append(user_list[2*i])
if length_user_list % 2 > 0:
    final_list.append(user_list[length_user_list-1])
print(final_list)
