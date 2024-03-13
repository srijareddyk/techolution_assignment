  
from student_class import Student
from course_class import Course

#taking input from user to create students
input_student_id_1 = int(input("Enter Student 1 ID: "))
input_name_1 = input("Enter Student 1 Name: ")
student1 = Student(input_student_id_1, input_name_1)

input_student_id_2 = int(input("Enter Student 2 ID: "))
input_name_2 = input("Enter Student 2 Name: ")
student2 = Student(input_student_id_2, input_name_2)

input_student_id_3 = int(input("Enter Student 3 ID: "))
input_name_3 = input("Enter Student 3 Name: ")
student3 = Student(input_student_id_3, input_name_3) #can add more student inputs here if needed

#taking input from user to create a course
input_course_name = input("Enter Course Name: ")
course_math = Course(input_course_name)

#enrolling students in the course
course_math.add_student(student1)
course_math.add_student(student2)
course_math.add_student(student3)

#taking input from user for student grades
input_grade_1 = float(input(f"Enter {student1.name}'s grade for {course_math.course_name}: "))
student1.add_grade(course_math.course_name, input_grade_1)

input_grade_2 = float(input(f"Enter {student2.name}'s grade for {course_math.course_name}: "))
student2.add_grade(course_math.course_name, input_grade_2)

input_grade_3 = float(input(f"Enter {student3.name}'s grade for {course_math.course_name}: "))
student3.add_grade(course_math.course_name, input_grade_3)

#calculating and printing gpa 
average_gpa_math = course_math.calculate_average_gpa()
print(f"The average GPA for {course_math.course_name}: {average_gpa_math}")
