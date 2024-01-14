# from turtle import *
# import random
# import turtle
# turtle.colormode(255)
# Kevin=Turtle()
# Kevin.screen.canvheight
# Kevin.shape("turtle")
# Kevin.color("green")


# def pattern(gap):
#     for _ in range(int(360/gap)):
#         Kevin.color(random_color())
#         Kevin.circle(50)
#         Kevin.speed("fastest")
#         Kevin.setheading(Kevin.heading()+gap)


# def random_color():
#     red = random.randint(0,255)
#     green =random.randint(0,255)
#     blue = random.randint(0,255)
#     color= (red, green, blue)
#     return color

# pattern(10)

# Kevin.screen.bye(exitonclick())


# Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with 
# max_speed and mileage instance attributes.

# class Vehicle:
#     def __init__(self, milage, max_speed):
#         self.car_dist=milage
#         self.car_speed=max_speed

# toyota=Vehicle('10000', '250')
# print(toyota.car_speed)

# Create a Vehicle class without any variables and methods

# class Vehicle:
#     pass

# Create class Student with attributes student_id, student_name, student_class. 
# Create an object class student, amd print all the attributes. 
# HINT- print(student.__dict__)

# # # class Student:
# # #     def __init__(self, student_id, student_name, student_class):
# # #         self.id = student_id
# # #         self.name = student_name
# # #         self.clas = student_class
# # #         self.grade = 0
# # #         self.professors=[]
    
# # #     def choose_professor(self, professor_name):
# # #         self.professors.append(professor_name)


# # # class Professor:
# # #     def __init__(self, professor_name, teaching_class):
# # #         self.name = professor_name
# # #         self.teaching_class = teaching_class
# # #         self.list_of_students=[]
    
# # #     def accept_student(self, student_name):
# # #         self.list_of_students.append(student_name)

# # #     def grade_students(self, student_name, grade):
# # #         students_grade={}
# # #         students_grade[student_name]=grade
# # #         return students_grade
        

# # # alex=Student("001", "Alex", "A")
# # # eva=Student("002", "Eva", "B")

# # # professor1 = Professor("Dr. Smith", "Math")
# # # professor2 = Professor("Prof. Johnson", "Science")

# # # alex.choose_professor(professor1.name)
# # # professor1.accept_student(alex.name)
# # # alex.choose_professor(professor2.name)
# # # professor2.accept_student(alex.name)
# # # eva.choose_professor(professor2.name)
# # # professor2.accept_student(eva.name)

# # # for student_name in professor2.list_of_students:
# # #     grade_dict=professor2.grade_students(student_name, 90)
# # #     if student_name=="Alex":
# # #         alex.grade=grade_dict[student_name]
# # #     else:
# # #         eva.grade=grade_dict[student_name]

# # # print(f"Alex's garde is {alex.grade}")
# # # print(f"Eva's grade is {eva.grade}")
# # # print(f"Professor {professor1.name} has {professor1.list_of_students} as students")
# # # print(f"Professor {professor2.name} has {professor2.list_of_students} as students")

#make him grade students(list(three grades)). 
#create several student and create a function inside professor. let professor accept a list of students they have.

