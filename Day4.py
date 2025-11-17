#Dictionaries
student = {'name':'Dipesh','age':25,'courses':['Compsci','Math'],25:'number'}
print(student)
print(student['name'])
print(student['courses'])
print(student[25])
#print(student['phone'])  #throw error ie Keyerror
# we don't alwyas want keyerror thrown when the key is not 
#so to handle this we use .get()
print(student.get('name'))
print(student.get('phone')) #here we try to acess the key that doesn't exist 
# but .get doesn't give error it gives output as none
# here we can set default value for the key that doesn't exist 
# we can do this by using second argument
print(student.get('phone','not found phone'))

#adding a enties to the dict 
student['phone'] = '985535355363'
# print(student)
print(student.get('phone','not found phone'))

student.update({'name':'Deepesh','age':24,'phone':'99999'})
print(student)
## here .update() method is use to update the dict for eg when we want to update multiple key
#add new key on the dict we can do this easliy on one line using this 


#deleting the key:value
#del is used

del student['name'] 
print(student)  # here name key is deleted

# anothe way is using pop
# pop() method is used to delete the keyvalue But the catch is pop() 
# methood return the deleted value
a = student.pop('age') # here age is deleted 
print(student)
print(a) # deleted age 24 is return and stored on a 


# looping
#  to see how many keys are this in dict we use len(dict_name)
print(len(student))
# to sees keys we use .keys()
print(student.keys())
# to get value we use .values()
print(student.values())
# to get both key with values we use .items() method
print(student.items())


#this only loop throught key on dict
for key in student:
    print(key)

# to loop throught key and value  we should use .items() method
for key,value in student.items():
    print(key,value)
  
# we can also use the method we learn in list to loop 
for key,value in enumerate(student):
    print(key,value)

