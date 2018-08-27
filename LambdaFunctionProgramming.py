#Reference
#https://www.python-course.eu/lambda.php

#reduce function is not directly available in python. We need to import reduce from functools in python
#Ref- https://www.python-course.eu/python3_lambda.php

from functools import reduce

'''

1.Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 

Order Number	Book Title and Author	Quantity	Price per Item
34587	Learning Python, Mark Lutz	4	40.95
98762	Programming Python, Mark Lutz	5	56.80
77226	Head First Python, Paul Barry	3	32.95
88112	Einführung in Python3, Bernd Klein	3	24.99


Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is less than 100,00 €. 
Write a Python program using lambda and map.


2.The same bookshop, but this time we work on a different list. The sublists of our lists look like this: 
[ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 
Write a program which returns a list of two tuples with (order number, total amount of order).

'''

#Solution-1

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],["98762", "Programming Python, Mark Lutz", 5, 56.80],["77226", "Head First Python, Paul Barry", 3,32.95],["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),map(lambda x: (x[0],x[2] * x[3]), orders)))

#Note- To understand the working of above lambda function break the function till innermost map function. Break and understand in below fashion
'''
output1 = map(lambda x: (x[0],x[2] * x[3]), orders) #Innermost lambda function execution

output2 = map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),map(lambda x: (x[0],x[2] * x[3]), orders))

final = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),map(lambda x: (x[0],x[2] * x[3]), orders)))
'''

#Solution-2

from functools import reduce

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],[2, ("5464", 9, 9.99), ("9744", 9, 44.95)],[3, ("5464", 9, 9.99), ("88112", 11, 24.99)],[4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

invoice = list(map(lambda k: k if k[1]>=100 else (k[0],k[1]+10),map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))),orders)))

#Breaking

'''
output1=map(lambda y:y[1]*y[2] ,x[1:])
output2=list(map(lambda y:y[1]*y[2] ,x[1:]))
output3=reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))
output4=map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:]))))
output5=map(lambda k: k if k[1]>=100 else (k[0],k[1]+10),map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))),orders))
output6=list(map(lambda k: k if k[1]>=100 else (k[0],k[1]+10),map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))),orders)))
'''


