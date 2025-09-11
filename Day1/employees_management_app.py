employees = []

employee =('abc', 21, 40000, True)
employees.append(employee)

employee =('xyz', 22, 50000, True)
employees.append(employee)

print(employees)

i = 0
search = 'abc'
index = -1
for emp in employees:
    if emp[0] == search:
        index = i
        break
    i += 1

if index == -1:
    print("employee not found")
else:
    search_employee = employees[index]
    print(employees[index])
    salary = float(input('Salary'))
    employee = (search_employee[0], search_employee[1])
    employees[index] = employee
print('after search and update')

employee =('def', 21, 40000, True)
employees.append(employee)
print(employees)
employees.pop() 
print(employees)

position = 1
employees.pop(position)
print(employees)