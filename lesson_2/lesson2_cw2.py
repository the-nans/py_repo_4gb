'''
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
'''
a = ''
user_list = []
while a != "enough":
    a = input('enter next list element or type "enough"')
    user_list.append(a)
user_list.remove('enough')
i = 0
print(user_list)
while i < len(user_list)-1:
    user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
    i += 2
print(user_list)