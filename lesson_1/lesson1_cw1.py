"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""
v_str = 'строка текста и в ней "ещё одна" '
v_int = 1
v_float = 3.4
v_bool = True
v_tuple = (3,4,6, 'apple')
v_list = [3,4,6, 'apple']
v_dictionary = {'Name' : 'James Bond', 'callsign' : '007'}

print(f'{v_int:<10}{v_str:<10}{v_float}')

v_user_input = int(input('введите целое число'))
print(v_user_input, type(v_user_input))
v_user_input = float(input('а теперь число с плавающей точкой'))
print(v_user_input, type(v_user_input))
v_user_input = input('можете ввести что угодно - это будет строка в итоге')
print(v_user_input, type(v_user_input))

print(v_list)
print(v_tuple)
print(v_dictionary)
