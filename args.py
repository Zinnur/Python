"""
#23 Подстановка аргументов

Принятие аргумента для вывода на печать будет выглядеть так:
	def echo (user) :
	print ( 'User:' , user )

Укажем значение, к-е передается аргументу в скобках,
чтобы потом вывести его на печать:
	echo ( 'Mike' ) 

В функцию можно передать несколько аргументов (параметров),
значение в скобках будет разделяться запятой
	def echo (user , lang , sys )
	print ( 'User:' , user , 'Language' , lang , 'Platform' , sys )

Важно понимать, что при вызове функции и заполняя аргументами,
нужно понимать тоже самое кол-во передаваемых значений
	echo ( 'Mike' , 'Python' , 'Windows' )

а при вызове ф-ции передаваемые значения должны идти в том же порядке,
что и аргументы
	echo ( lang = 'Python' , user = 'Mike' , sys = 'Windows' )
 
также существует  возможность при определении ф-ции, заранее указать 
аргументы по умолчанию
	def echo ( user , lang , sys = 'Linux' )
	print ( 'User:' , user , 'Language:' , lang , 'Platform:' , sys )

"""

# начнем прогамму с определения функции, 
# к-я принимает 3 аргумента и выводит на печать их значения

def echo ( user , Lang , sys ) :
	print ( 'User:' , user , 'Language:' , Lang , 'Platform', sys )

# вызовем функцию и передадим строковые значения аргументов
# в том порядке, в к-м они определены

echo ( 'Mike' , 'Python' , 'Windows' )

# вызовем функцию заного, передав ей строковые значения и
# проименуем аргументы
echo ( Lang = 'Python' , sys = 'Mac OS' , user = 'Anne' )
# объявим еще одну ф-цию, к-я принимает 2 аргумента со значениями
def mirror ( user = 'Carole' , Lang = 'Python' ) :
	print ( '\nUser:' , user , 'Language:' , Lang )
# добавим новую инструкцию с вызовом второй ф-ции,
# переписывая значения аргументов, но сначал используем
# их по умолчанию!
mirror ()
mirror ( Lang = 'Java' )
mirror ( user = 'Tony' )
mirror ( 'Susan' , 'C++' )
