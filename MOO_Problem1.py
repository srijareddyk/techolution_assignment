
#defining the student class 
class Student:
    
#constructor method to initialize the student object with student_id and student name
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

#method to add a grade for a specific course
    def add_grade(self, course, grade):
        self.grades[course] = grade
        
#method calculate gpa
    def calculate_gpa(self):
        if not self.grades:
            return 0.0

        total_points = sum(self.grades.values())
        num_courses = len(self.grades)
        return total_points / num_courses

#defining the course class
class Course:
    
#constructor method to initialize the course object with course_name
    def __init__(self, course_name):
        self.course_name = course_name
        self.enrolled_students = []
        
#method to add a student to the course
    def add_student(self, student):
        self.enrolled_students.append(student)
        
#method to remove a student from the course
    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            
#calculating the average gpa of all students in the course
    def calculate_average_gpa(self):
        if not self.enrolled_students:
            return 0.0

        total_gpa = sum(student.calculate_gpa() for student in self.enrolled_students)
        num_students = len(self.enrolled_students)
        return total_gpa / num_students


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




