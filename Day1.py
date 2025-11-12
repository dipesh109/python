print("hello world")
message = 'hello world'
print(message)
m = 'booby\'s world'
 #using \ we can solve it 
print(m)
m1 = """booby's
world"""
print(m1)
print(len(message))
print(message[6])

# slicing 
print(message[0:5]) #1st index is incluive and last index is exclusive

# lowercase and uppercase
print(message.upper())
print(message.lower())


#count
print(message.count('l')) #= 3  count the letter in sentence

#find
print(message.find('l'))

#replace
message =message.replace("world","Universe")
print(message)

# concartnation
greeting = "Hello"
name = "Dipesh"
# text = greeting + ' '+ name
# text = "{} {}".format(greeting,name)
text = f"{greeting} {name.upper()}"
print(text)

print(dir(name))
print(help(str.lower))





