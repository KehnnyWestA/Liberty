from math import factorial
from types import new_class

#length = float(input("what is the length :" ))
#width = float(input("what is the width :" ))
#area = length * width

#print(f"the area is {area}cm ")

#for x in range(1, 11) :
#    if x == 7:
 #       break
 #   else:

 #       print(x)
#weight = float(input("Enter your weight: "))
#unit = input("Kilo or pounds? (K or L): ")

#if unit == "K".casefold():
 #    weight = weight * 2.205
   #  unit = "Lbs."
   #  print(f"you weigh: {round(weight, 1)} {unit}")
#elif unit == "L".casefold():
 #   weight = weight / 2.205
 #   unit = "kgs"
  #  print(f"you weigh: {round(weight, 1)} {unit}")
#else:
 #    print(f"{unit} not valid")


#my_dict={'ola':'001','omo':'oo2','seyi':'003'}
#print(my_dict)
#type(my_dict)
#new_dict=dict()
#print(new_dict)
#type(new_dict)

#emp_details={'ola':{'ID':'001','salary':'#3000','position':'leader'},
 #            'omo':{'ID':'002','salary':'#2000','position':'intern'}}
#emp_details ['ola'] = '0001'
#emp_details ['sheyi'] = '003'
#for x in emp_details.values():
 #print (x)

#print(my_dict.get('ola'))

#for k in my_dict.values():
#    print(k)

#import pandas
#df= pandas.DataFrame(emp_details['employee'])
#print(df)

#sir = 20
#num = 19
#compare  = sir > num
#compare

#if sir == num:
 #   print('equal')
#elif sir > 1:
 #   print('greater')
#else:
 #   print('lesser')

#list1 = [10,20,30]
#list2 = [10,20,30]

#x = list1
#x is list1

#20 in list1

#10 | 12

#count = 0
#while count < 9 :
  #  print ('Number:', count)
 #   count = count + 1
#print('Nice Try!')

#import random
#k = 20
#to_be_guessed = int(k* random.random()) +1
#guess = 0
#while guess != to_be_guessed:
#    guess = int(input('New Number!'))
#    if guess > 0:
#        if guess > to_be_guessed:
#            print('Number too large')
#        elif guess < to_be_guessed:
#            print('Number too small')
#    else:
#            print('you lose!')
#else:
#     print('you win!!')

#fruits = ['mango','orange','banana','apple']
#for fruit in fruits:
 #   print('current', fruit )

#num = int(input('Number:'))
#factorial = 1
#if num < 0:
#    print('must be +ve')
#elif num == 0:
#    print('factorial = 1')
#else:
 #   for i in range(1, num + 1):
  #      factorial = factorial * i
#print(factorial)

#from math import sqrt
#n = int(input('max number: '))
#for a in range (1,n + 1):
 #   for b in range (a,n):
  #      c_square = a**2 + b**2
   #     c = int(sqrt(c_square))
    #    if ((c_square - c**2) ==0):
     #      print(a,b,c)


#def pattern (n):
#         k = 2 * n - 2
#         for i in range (0,n-1):
#             for j in range (0,k):
#                 print(end = " ")
#             k = k - 2
#             for j in range (0, i + 1):
#                 print("*", end = " ")
#             print("\r")
#         k = k - 1
#         for i in range (n-1, -1, -1):
#             for j in range (k, -1, -1):
#                 print(end = " ")
#             k = k + 2
#             for j in range(0,i+1):
#                 print("* ", end="")
#             print("\r")
#pattern(5)


#def fib():
#    f,s = 0,1
#    while True:
#        yield f
#        f,s = s, f+s
#for x in fib():
#    if x >50:
#        break
#    print(x, end= " ")

#a = range(51)
#b = (x for x in a)
#print(b)
#for y in b:
#    print(y)

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
#def s(flip = 2):
#    x = np.linespace(0, 14, 100)
#    for i in range (1, 5):
#        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)



#sb.set()
#s()
#plt.show()



#import mod1 as md
#addition = md.add(6,7)
#print(addition)


#import numpy as np
#import matplotlib.pyplot as plt
#x = np.arange (0,3 * np.pi , 0.1)
#y = np.tan(x)
#plt.plot(x,y)
#plt.show()


#import pandas
#XYZ_web = { 'day':[1,2,3,4,5,6], 'visitors':[50,70,30,700,900,600], 'bounce':[4,20,3,70,57,4] }
#df = pandas.DataFrame(XYZ_web)
#print(df)

#from matplotlib import pyplot as plt
#plt.plot([2,7,3],[5,2,9])
#plt.show()

#from matplotlib import pyplot as plt
#X = [3,2,6]
#Y = [1,4,0]

#plt.plot(X,Y)
#plt.title ('info')
#plt.ylabel('Y_axis')
#plt.xlabel('X_axis')

#plt.show()

#from matplotlib import pyplot as plt
#from matplotlib import style
#style.use('ggplot')
#X = [3,2,6]
#Y = [1,4,0]
#X2 = [2,7,3]
#Y2 = [5,2,9]

#plt.plot(X,Y , label = 'line1',linewidth = 5)
#plt.plot(X2,Y2,  label = 'line2', linewidth = 4)
#plt.title('info')
#plt.ylabel('Y_axis')
#plt.xlabel('X_axis')

#plt.grid(True, color = 'k' )
#plt.legend()
#plt.show()


"""
from matplotlib import pyplot as plt
from matplotlib.pyplot import ylabel

plt.bar([1,9,23,4,7],[4,6,1,10,3], label = 'Example_1')
plt.bar([6,2,3,4,12],[9,14,11,5,2], label = 'Example_2',color = 'c')

plt.legend()
plt.xlabel('bar_number')
plt,ylabel('bar_height')

plt.title('Info')

plt.show()

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = sns.load_dataset('flights')
sns.relplot(x='passengers',y='month', data=a)

