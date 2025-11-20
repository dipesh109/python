def hello_func():
    pass
print(hello_func())


def hello_func():
    print('hello function!')

hello_func()
hello_func()
hello_func()
hello_func()


#DRY don't repeat yourself

def hello_func():
    return 'Hello FUnction'

print(hello_func())
print(hello_func().upper())


def hello_func(greeting):
    return '{} world'.format(greeting)

print(hello_func('Hi'))

def hello_func(greeting,name= 'Dipesh'):
    return '{} {} '.format(greeting ,name)

print(hello_func('Hi',"Marasini"))


def student_info(*args, **kwargs):
    print(args) #postional argument
    print(kwargs) #keyword value
student_info('Math','Art',name = 'john',age= 22)


def student_info(*args, **kwargs):
    print(args) #postional argument
    print(kwargs) #keyword value

course = ['math','Art']
info = {'name':'john','age':22}
student_info(course,info)


def student_info(*args, **kwargs):
    print(args) #postional argument
    print(kwargs) #keyword value

course = ['math','Art']
info = {'name':'john','age':22}
student_info(*course,**info)


#Number of days in month.First value placeholder for indexing purposes
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """Return true for learyears and false for non leap years"""
    return year % 4 == 0 and (year%100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    """return number of dqays in that month in that year"""
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
       return 29 
    return month_days[month]


# print(is_leap(2020))
print(days_in_month(2017,2)) #non leap
print(days_in_month(2020,2))   #leap years




# print(len('Test'))


