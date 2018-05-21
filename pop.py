# 1, 2, 3, A, B, C.
#
# len (L) - это функция, к-я возвращает размер списка L,
# т.е. общее количество элементов, содержащихся в списке L
#
# str(n) - это функция, к-я преобразует числовое значение в строковое
# как правило, это используется для сложения с другими строками 
#
# del(i) - это функция, к-я удаляет отдельные элементы списка
#
# int(s) - это функция, к-я возвращает числовое представление строковой велечины s
#

basket = [ 'Apple' , 'Bun' , 'Cola' ]
crate = [ 'Egg' , 'Fig' , 'Grape' ]

print ( 'Basket List:' , basket )
print ( 'Basket Element:' , len(basket) )

basket.append ( 'Damson' )
print ( 'Appended:' , basket )
print ( 'Last Item Removed:' , basket.pop () )
print ( 'Basket List:' , basket )

