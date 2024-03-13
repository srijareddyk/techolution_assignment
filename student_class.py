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
