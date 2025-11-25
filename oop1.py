class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Dipesh'
emp_1.last = 'Marasini'
emp_1.email = 'marasinidipesh@gmail.com'
emp_1.pay  = 4000

emp_2.first = 'Deviram'
emp_2.last = 'Marasini'
emp_2.email = 'marasinideviram@gmail.com'
emp_2.pay  = 40000

print(emp_1.first)
print(emp_2.first)


class employee:

    def __init__(self,first,last,pay):
        self.fname = first
        self.last = last
        self.pay = pay
        self.email = last+first+"@gmail.com"

    def fullname(self):
        return ('{} {}'.format(self.fname,self.last))

emp_1 = employee('dipesh','marasini',5000)
emp_2 = employee('deviram','marasini',10000)
print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(employee.fullname(emp_1))
