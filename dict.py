# ключ:значение
# del - удалить пару  - имя словаря и [имя ключа]
#
# keys () - метод ,к-й возвращает в случайном порядке список всех ключей словаря
#
# sorted () - метод, к-й сортирует в алфавитно-цифровом порядке 
#
# Итог:
# Типы контейнеров на языке Python:
# 1)    переменная - это одиночное значение
# 2)  () список - это несколько значений, упорядоченных по индексу
# 3)  [] кортеж -  несколько фиксированных значений в определенной последовательности
# 4)  {} множество - несколько уникальных значений в неупорядоченном наборе 
# 5)  {:} словарь - несколько неупорядоченных пар - ключ:значение

dict = { 'name' : 'Bob' , 'ref' : 'Python' , 'sys' : 'Win' }
print ( ' Dictionary:' , dict )

# выведем на экран единичное значение, указав на него ссылку по ключу
print ( '\nReference:' , dict ['ref'] )
# выведем все ключи, которые содержатся в словаре 
print ( '\nKeys:' , dict.keys () )
# удалим одну из пар словаря
del dict [ 'name' ]
# Добавим новую пару в словарь
dict [ 'user' ] = 'Tom'
# выведем содержание словаря  
print ( "New Dictionary:" , dict)
# запустим поиск определенного ключа и увидим результаты поиска
print ( '\nIs There A name Key?:' , 'name' in dict )
