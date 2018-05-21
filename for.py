# for элемент in имя-списка
# выполняемые инструкции на каждой итерации
# 
# range () - функция. к-я генерирует последовательносить,
# к-я начинаетсяс нуля и заканчивается числом в скобках, НЕ атрагивая его
# т.е.
# range (3) будет равно 0, 1. 2
# 
# items () - метод словаря, к-й выводит пары - ключ:значение
# 
# zip () - функция, к-я позволяет обзодить несколько списков одновременно
# 
# enumerate () - функция, к-я выводит все индексы и связанные с ними значения,
# где в качестве параметра указывается имя списка
# 
# 

chars = [ 'A' , 'B' , 'C' ]
fruit = ( "Apple" , 'Babana' , 'Cherry' )
dict = { 'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Win' }
# добавим инструкцию для вывода значений всех элементов списка
print ( '\nElements:\t' ,  end = '' )
for item in chars :
	print ( item , end = '' )
# добавим инструкцию для вывода значений всех элементов списка,
# а также их индексов
print ( '\nEnumerated:\t' , end = '' )
for item in enumerate ( chars ) :
	print (item , end = '' )
# выведем все элементы списка и кортежа
print ( '\nZipped:\t' , end = '' )
for item in zip ( chars , fruit ) :
		print ( item , end = '' )
# добавим инструкцию для вывода всех имен ключей словаря
print ( '\nPaired:' )
for key , value in dict.items () :
	print (key , '=' , value )



# Для перебора элементов в языке Python используется оператор for in.
# После in указывается имя списка, а заканчивается все двоеточием. 
# После этого идут инструкции, которые выполняются на каждой итерации цикла. 
# for элемент in имя-списка : выполняемые-инструкции-на каждой-итерации 
# Строка – это не что иное, как список символов, поэтому каждый символ 
# можно обходить в цикле, используя эту инструкцию. 
# Из этого можно сделать вывод, что с помощью инструкции for in можно 
# делать обход элементов списка, кортежа, множества, а также ключей словаря...