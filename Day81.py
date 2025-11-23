# import module as mm # here module is improred from module.py as name as mm for easy 
#  # now we want to import specific function from module 
#  # we can do that by using 
#  # from module_name import function_name 

# from module import find_index 

# ourses = ['History','Math','Physics','CompSci']c

# # index = module.find_index(courses,'Physics') id as na vayarw direct vya sidhai module lekhnu parhteyo 

# index = mm.find_index(courses,'Physics')
# index = find_index(courses,'Physics')
# print(index)






# yaha bata only funtion find_index is imported # not test 
# so to acess test also we using , and after that name
from module import find_index ,test 


courses = ['History','Math','Physics','CompSci']
index = find_index(courses,"Math")
print(index)
print(test) 

from module import * 
# this import all the function from the module named module 
import sys
print(sys.path)
# this is the path that py looks for the module 

