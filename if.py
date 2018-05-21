# if проверочное выражение - 1:
#
# выполняемая инструкция - когда - проверочное - выражение - 1 - истинно
#
# elif проверочное выражение - 2 :
#
# выполняемая интструкция - когда - проверочное - выражение - 2 - истинно
#
# else :
#
# выполняемая - инструкция - когда - проверочное - выражение - ложно
# 
num = int ( input ( 'Please Enter A Number:' ) )

if num > 5 :
	print ( 'Number Exceeds 5' )

elif num < 5 :
	print ( 'Number is Less 5' )

else :
	print ( 'Number is 5' )

if num > 7 and num < 9 :
	print ( 'Number is 8' )

if num == 1 or num == 3 :
	print ( 'Number is 1 or 3' )
