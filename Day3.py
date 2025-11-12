courses = ['History','math','Physics','CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])

print(courses[-1]) #last index
print(courses[-2]) 
# print(courses[10])

print(courses[0:2])  #1st index chai hamro staring point vyo 
#second lai stoping point
#1st is inclusive 2nd index is exclusive

print(courses[:3]) #if no starting index so it start from zero index
print(courses[1:4])

print (courses[0:]) # if no stoping index so its goes to last index
print(courses[1:])


## Adding items in list
# append  = add item in list to end of the list
courses.append('Art')
courses.append('Chem')
print(courses)

#insert it add item to the list in any location of list 
#insert add item on list doesnot overwrite in list 
courses.insert(0,'Bio')
courses.insert(1,'nepali')
courses.insert(4,'newari')
print(courses)

course =  ['History','math','Physics','CompSci']
course1 = ['Art', 'Education']
course.insert(0,course1)
print(course)
print(course[0])
#this output is not what we want 
# we want to add both item of 2nd list to 1st list as two seperate item 
# not one item but here it shows both as one item

#to slove this problem we have 
##extend()
course =  ['History','math','Physics','CompSci']
course1 = ['Art', 'Education']
course.extend(course1)
print(course)
print(course[-1])



## Remove item from list
#remove("name") is used to remove item named 'name'
course =  ['History','math','Physics','CompSci']
course.remove('math')
print(course)

#pop() is ued to remove item from list but it default to remove item from last index
#pop() return the value it remove
course =  ['History','math','Physics','CompSci']
popped = course.pop() # remove value is return
print(popped)
print(course)


## Sorting of list
# reverse()  is used to reverse the item in list 
course =  ['History','math','Physics','CompSci']
course.reverse()
print(course)

#sort() is used for sorting the 
# for sting it sort acc to alphabetical order
# for numberic it sort in ascending orderm
course =  ['History','math','Physics','CompSci']
course.sort()
print(course)

num = [0,1,110,250,6,9]
num.sort()
print(num)

# for decending sorting we can do sort 1st and use reverse 
num.reverse()
print(num)
#OR this 
num = [0,1,110,250,6,9]
num.sort(reverse = True)
print(num)


#when we call sort method it alter our original list
#for not altering the orginal list
# we call sorted funtion insted of sort method
course =  ['History','math','Physics','CompSci']
sortedlist = sorted(course)
print(course)
print(sortedlist)


num = [0,1,110,250,6,9]
print(min(num)) #lminimum or least valued 
print(max(num))#maxmum or higgtest value
print(sum(num)) # add the number in list


##find the index of item in list
# .index()
course =  ['History','math','Physics','CompSci']
print(course.index('math'))
# print(course.index('art')) # error

# to check whether the item is in list or not 
# use in
print('art'in course)
print('CompSci'in course)

 #forin is for loop that run every item in list
 #acess each value
for item in course:
    print(item)

 #where as enumerate  give the index of the value in list
#  index and value can be acess using enumerate 
for index,item in enumerate(course):
    print(index,item)

# if we don't want to start from zero we can give starting number 
#start = 1;
for index,item in enumerate(course,start=1):
    print(index,item)


#list to string
#we use .join()
#",",join means the item is seperated by comma in string
course_str = ', '.join(course)
course_str = ' - '.join(course)
print(course_str)

# string to list 
new_list = course_str.split(' - ')
print(new_list)


# tuples and list are similer one major different is we can't modified tuples 
# tuple are inmutable ie. can't modified
# list are mutable

#mutable 
course =  ['History','math','Physics','CompSci']
course1 = course
print(course)
print(course1)

course[0] = 'Art';
print(course)
print(course1)


#tuples looks like same as list but insted of [] we use ()
tuple1 =  ('History','math','Physics','CompSci')
tuple2 = tuple1
print(tuple1)
print(tuple2)

# tuple1[0] = 'Art';
# print(tuple1)
# print(tuple2)




###Sets 
# sets remove duplicate item 
# justai math doublle vyo tei vyarw 1choti matra dekhayo

couresset = {"History", "Math", "Physics","CompSci",'Math'}
couresset1 = {'History','Math','Art','Design'}
# print(couresset)

# print('Math' in couresset)

print(couresset.intersection(couresset1))
print(couresset.difference(couresset1))
print(couresset.union(couresset1))



#Empty Lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets 
empty_set = {} #this isn't correct its create empty dict
empty_set = set()

















