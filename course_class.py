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

