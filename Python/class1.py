class person:
    def __init__ (self,name,age,cgpa):
        self.name=name
        self.age=age
        self.cgpa=cgpa
student = person("aju",23,8)
print(student.name,student.age,student.cgpa)
name=raw_input("enter the name")
age=raw_input("age")
cgpa=raw_input("enter cgpa")
student1=person(name,age,cgpa)
print(student1.name,student1.age,student1.cgpa)

