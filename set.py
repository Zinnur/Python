# color = ( 'Red' , 'Green', 'Blue', 'Red', 'Green' )
# 
# set = { 'Alfa', 'Bravo', 'Charlie' }
#
# для определения структуры данных в классах и списках применяется
# функция - type () Python
#
# in - оператор вхождения - нужен для того, чтобы найти значение в списке

zoo = ( 'Kangaroo', 'Leopard', 'Mouse' )
print ( 'Typle:' , zoo, '\tLenght:' ,  len (zoo) )
print ( type (zoo) )

bag = { 'Red', 'Green', 'Blue'}
bag.add ( 'Yellow' )
print ( '\nSet:' , bag , '\tLenght:' , len (bag) )
print ( type (bag) )

print ( '\nIs Green in bag Set?:' , 'Green' in bag )
print ( '\nIs Orenge in bag Set?:' , 'Orenge' in bag )

box = { 'Red' , 'Purple' , 'Yellow' }
print ( '\nSet:' , box , '\tLenght:' , len (box) )
print ( 'Common To Both Sets:' , bag.intersection (box) )

# set () - конструктор, с помощью к-го также можно создать множество,
# где в скобках аключен список
#
# frontzet () - конструктор, с помощью к-го также можно создать Изменяемое множество
#