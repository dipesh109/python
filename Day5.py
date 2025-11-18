
# conditions
if True:
    print("is true")
if False:
    print("is false")

lang = 'Py'
if lang == 'Py':
    print('lang is py')
elif lang == 'java':
    print('lang is java')
else:
    print('no match')


# python doesn't have switch statement



# != not equal
# > greater than 
# < less than
# Object Identity : is


# and when both are true
# or when only one is true
# not change true to false and false to true

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('bad cred')


user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('bad cred')



logged_in = False
if not logged_in:
    print('Please log in')
else:
    print('sucess')



a = [1,2,3]
b = [1,2,3]
# a = b 
print(a ==b) #this return true
print(a is b)   #this return false becaues this are two different object in memory
print(id(a))
print(id(b)) 
#here id of a abd b are diffent so above is false cause is check id of varible


# here are the value that py evalute to false 
  ##False
  ##None
  ##Zero of any numeric type
  ##Any empty sequence. For example, '',(),[]
  ##Any empty mapping . For example {}

condition = False
condition = None
condition = 0
condition = 101
condition = ''
condition = []
condition = ()
condition = {}



if condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')


# Here above return false so every this other than this evaluate to true 