# techolution_assignment
Modularized Object Oriented Python Coding Assessment - Techolution X MU

# Report: Student and Course Management System

The code shows an implementation of a Student and Course Management System. It defines two classes: Student and Course, serving to model students and courses. The system facilitates user interaction for inputting student details, enrolling students in a course, assigning grades, and computing the average GPA for the enrolled students.


## Code Explanation
### 1. Student Class
- Initializes a Student instance with a unique student_id and name.
- Creates an empty dictionary to hold course grades.

#### Add Grade Method
- Appends a grade for a specified course (course) to the student's grades dictionary.

#### Calculate GPA Method
- Computes the GPA for the student based on the stored grades in the grades dictionary.
- Returns the computed GPA or 0.0 if no grades are available.
---
### 2. Course Class
- Initializes a Course instance with a course_name.
- Creates an empty list (enrolled_students) to store enrolled students.

#### Add Student Method
- Inserts a student into the list of enrolled students.

#### Remove Student Method
- Deletes a student from the list of enrolled students.

#### Calculate Average GPA Method
- Computes the average GPA for all enrolled students in the course.
- Returns the computed average GPA or 0.0 if no students are enrolled.
---
### 3. User Interaction
- The code prompts users to input information for three students and a course.
- Students are enrolled in the course, and grades are entered for each student in the course.
- The average GPA for the course is calculated and displayed.
