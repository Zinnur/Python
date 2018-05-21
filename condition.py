
# ?:
#
# (проверочное выражение) ? если истина - возращаем это : если ложь - возвращаем это
#
# если истина - возвращаем это - if (проверочное выражение) else если ложь - возврщаем это
#
# c = a if ( a < b ) else b
#

a = 5
b = 6

print ( '\nVariable a is :' , 'One' if ( a == 5 ) else 'Not One' )
print ( 'Variable a is :' , 'Even' if ( a % 2 == 0) else 'Odd' )

print ( '\nVariable b is :' , 'One' if ( b == 5 ) else 'Not One' )
print ( 'Variable b is :' , 'Even' if ( b % 2 == 0 ) else 'Odd' )

max = a if ( a > b ) else b

print ( '\nGreater Value is:' , max)

