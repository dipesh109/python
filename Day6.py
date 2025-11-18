##Loops and iterations

nums = [1,2,3,4,5]
for value in nums:
    print(value)


# Break and coutine
# Break will completly break the loop come out 
# Countinue will move on to next iterations of loops

for value in nums:
    if value == 3:
        print('found')
        break
    print(value)


for value in nums:
    if value == 3:
        print('found')
        continue
    print(value)


# loop within loop nested loop
for value in nums:
    for values in 'abc':
        print(value,values)


for i in range(10):
    print(i)
for i in range(1,10):
    print(i)


x = 0 
while x < 10:
    print(x)
    x +=1

x = 0 
while x < 10:
    if x == 5:
        break
    print(x)
    x +=1



# when you want infinte loop until conditionis meet such as user enter a data 
# we simple use True 
x = 0 
while True:
    # if x == 5:
    #     break
    print(x)
    x +=1