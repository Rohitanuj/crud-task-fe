class Student:
    def __init__(self,name , grade , precentage):
        self.name= name
        self.grade= grade
        self.percent = precentage

    def student_details(self):
       print(f"{self.name} is  the name of student {self.grade} is the grade and percent {self.percent}%" )
    
    def get_precent(self):
        if self.percent == 70:
            return "no value found"
        else:
            return self.percent
    

class Graduate_Stu(Student):
    def __init__(self, name, grade, precentage,stream):
        super().__init__(name, grade, precentage)
        self.stream = stream
    def student_details(self):
   #    print(f"{self.name} is  the name of student {self.grade} is the grade and percent {self.percent}% with {self.stream}" )    
        super().student_details()
        print(f"Stream: {self.stream}")

student1=Student("Manav",11, 90)
student2=Student("Man",12, 70)
# print(student2.student_details())
# print(student2.get_precent())
# print(student2.get_precent())
graduate_stu = Graduate_Stu("Anuj", 13, 90,"ec")
graduate_stu.student_details()


student = {
1: "Class-X",
"name": "Madhav",
"age": 20
}

for key in student:
    print(key)

for all in student.items():
    print(all)



  
a= [1,2,3]
b = a 
a.append(5)
print(a)
print(b)
n= 45
try:
    result = 45/0
except ZeroDivisionError:
    print("The code have an error of infinite")
finally:
    print("Finally its end")

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog:
    def make_sound(self):
        print("Bark")

a1 = Dog()
a1.make_sound()
