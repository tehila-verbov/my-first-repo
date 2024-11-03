from Student import Student
from Employee import Employee

student = Student("Mike", 22, "Engeneering", 1, 80)
print("This is from programmer 1, 123, hi from github")
# student.foo()

print("This is from programmer 2")
employee = Employee("Tehila", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()









