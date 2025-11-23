# when we want to import the module from different folder then 
# we have to different ways to handle this problem 
#first ma chai 
#sys patha ma tyo module vanako folder ko path append garne 
# just like below

import sys
sys.path.append('D:\py')

print(sys.path)
# yaha k vayo vaney mero tyo path sys ma aad vyo 
from module2 import find_index ,test 



courses = ['History','Math','Physics','CompSci']
index = find_index(courses,"Math")
print(index)
print(test) 


#this is not the best way to do 
# so we direct set the enviroment variable



#now we gonna import from strand lib


import random 
courses = ['History','Math','Physics','CompSci']
random_course = random.choice(courses)
print(random_course)


import math
rads = math.radians(90)
print(rads)

import datetime
import calendar
today = datetime.date.today()
print(today)

print(calendar.isleap(2020))


import os
print(os.getcwd())

print(os.__file__)





