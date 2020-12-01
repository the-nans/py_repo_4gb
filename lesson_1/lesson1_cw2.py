"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
time_sec = int(input('Enter seconds\n'))
hours = "%02d" % ((time_sec - time_sec % 3600)//3600)
minutes = "%02d" % ((time_sec - int(hours)*3600 - time_sec % 60) // 60)
sec = "%02d" % (time_sec - int(hours) * 3600 - int(minutes)*60)
print(f'{hours:<5}:{minutes:<5}:{sec:<5}')   # подровняем для красоты
