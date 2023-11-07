import json
import copy


class Course:
    id = 0
    name = ""
    units = 0
    score = 0.0
    courses = []

    def __init__(self, id, name, units):
        self.id = id
        self.name = name
        self.units = units
        self.score = 0.0

    def setScore(self, score):
        self.score = score

    @staticmethod
    def addCourse(course):
        if isinstance(course, Course):
            if Course.indexOf(course.id) == -1:
                Course.courses.append(course)
            else:
                print("Course already exists.")
        else:
            print("Argument is not a Course object.")

    @staticmethod
    def removeCourse(id):
        if isinstance(id, int):
            index = Course.indexOf(id)
            if index != -1:
                Course.courses.pop(index)
                print("Course removed successfully.")
            else:
                print("Course does not exist.")
        else:
            print("Argument should be an int.")

    @staticmethod
    def printCourses():
        print("ID\tName\tUnits")
        for course in Course.courses:
            print(f"{course.id}\t{course.name}\t{course.units}")

    @staticmethod
    def indexOf(id):
        for i, course in enumerate(Course.courses):
            if course.id == id:
                return i
        return -1

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Units: {self.units}"

    def __eq__(self, other):
        return self.id == other.id


class Student:
    id = 0
    name = ""
    family = ""
    courses = ""
    students = []
    selected = None

    def __init__(self, id, name, family, courses):
        self.id = id
        self.name = name
        self.family = family
        self.courses = courses

    @staticmethod
    def addStudent(student):
        if isinstance(student, Student):
            if Student.indexOf(student.id) == -1:
                Student.students.append(student)
            else:
                print("Student already exists.")
        else:
            print("Argument is not a Student object.")

    @staticmethod
    def removeStudent(id):
        if isinstance(id, int):
            index = Student.indexOf(id)
            if index != -1:
                Student.students.pop(index)
                print("Student removed successfully.")
            else:
                print("Student does not exist.")
        else:
            print("Argument should be an int.")

    @staticmethod
    def indexOf(id):
        for i, student in enumerate(Student.students):
            if student.id == id:
                return i
        return -1

    @staticmethod
    def editStudent(student):
        if isinstance(student, Student):
            index = Student.indexOf(student.id)
            if index != -1:
                Student.students[index] = student
                print("Student updated successfully.")
            else:
                print("Student does not exist.")
        else:
            print("Argument is not a Student object.")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Family: {self.family}"

    def __eq__(self, other):
        return self.id == other.id


class Teacher:
    id = 0
    name = ""
    family = ""
    courses = []
    teachers = []

    def __init__(self, id, name, family, courses):
        self.id = id
        self.name = name
        self.family = family
        self.courses = courses

    @staticmethod
    def addTeacher(teacher):
        if isinstance(teacher, Teacher):
            if Teacher.indexOf(teacher.id) == -1:
                Teacher.teachers.append(teacher)
            else:
                print("Teacher already exists.")
        else:
            print("Argument is not a Teacher object.")

    @staticmethod
    def removeTeacher(id):
        if isinstance(id, int):
            index = Teacher.indexOf(id)
            if index != -1:
                Teacher.teachers.pop(index)
                print("Teacher removed successfully.")
            else:
                print("Teacher does not exist.")
        else:
            print("Argument should be an int.")

    @staticmethod
    def indexOf(id):
        for i, teacher in enumerate(Teacher.teachers):
            if teacher.id == id:
                return i
        return -1

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Family: {self.family},Course: {self.courses}"

    def __eq__(self, other):
        return self.id == other.id


class Classroom:
    id = 0
    name = ""
    teacher = None
    course = None
    students = []
    classrooms = []

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.teacher = None
        self.course = None
        self.students = []

    @staticmethod
    def addClassroom(classroom):
        if isinstance(classroom, Classroom):
            if Classroom.indexOf(classroom.id) == -1:
                Classroom.classrooms.append(classroom)
            else:
                print("Classroom already exists.")
        else:
            print("Argument is not a Classroom object.")

    @staticmethod
    def removeClassroom(id):
        if isinstance(id, int):
            index = Classroom.indexOf(id)
            if index != -1:
                Classroom.classrooms.pop(index)
                print("Classroom removed successfully.")
            else:
                print("Classroom does not exist.")
        else:
            print("Argument should be an int.")

    @staticmethod
    def indexOf(id):
        for i, classroom in enumerate(Classroom.classrooms):
            if classroom.id == id:
                return i
        return -1

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    def __eq__(self, other):
        return self.id == other.id
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {
                "id": obj.id,
                "name": obj.name,
                "family": obj.family,
                "courses": obj.courses
            }
        elif isinstance(obj, Teacher):
            return {
                "id": obj.id,
                "name": obj.name,
                "family": obj.family,
                "courses": obj.courses
            }
        elif isinstance(obj, Course):
            return {
                "id": obj.id,
                "name": obj.name,
                "units": obj.units,
                "score": obj.score
            }
        elif isinstance(obj, Classroom):
            return {
                "id": obj.id,
                "name": obj.name,
                "teacher": obj.teacher,
                "course": obj.course,
                "students": obj.students
            }
        return super().default(obj)


f1 = open("data.json", "rt")
s = f1.read()
ms = json.loads(s)
for student in ms["students"]:
    Student.addStudent(
        Student(student["id"], student["name"], student["family"], student["courses"]))
for teacher in ms["teachers"]:
    Teacher.addTeacher(
        Teacher(teacher["id"], teacher["name"], teacher["family"], teacher["courses"]))
for course in ms["courses"]:
    Course.addCourse(Course(course["id"], course["name"], course["units"]))
level = "root"
while True:
    if level == "root":
        print("1-students")
        print("2-teachers")
        print("3-courses")
        print("4-classrooms")
        print("5-save")
        print("6-exit")
        cmd = int(input("Enter command: "))
        if cmd == 1:
            level = "students"
        elif cmd == 2:
            level = "teachers"
        elif cmd == 3:
            level = "courses"
        elif cmd == 4:
            level = "classrooms"
        elif cmd == 5:
            data = {
                "students": Student.students,
                "teachers": Teacher.teachers,
                "courses": Course.courses,
                "classrooms": Classroom.classrooms
                }
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4, cls=CustomEncoder)
            print("Data saved successfully.")
        elif cmd == 6:
            break
    elif level == "students":
        print("1-show students")
        print("2-add student")
        print("3-edit student")
        print("4-delete student")
        print("5-select student")
        print("6-back")
        cmd = int(input("Enter command: "))
        if cmd == 1:
            for student in Student.students:
                print(student)
        elif cmd == 2:
            student_id = int(input("id: "))
            student_name = input("name: ")
            student_family = input("family: ")
            student_courses = []  # You can add logic here to populate the student's courses
            student = Student(student_id, student_name, student_family, student_courses)
            Student.students.append(student)
            print("Student added successfully!")
        elif cmd == 3:
            student_id = int(input("id: "))
            index = Student.indexOf(student_id)
            if index != -1:
                student = Student.students[index]
                student_name = input("name: ")
                student_family = input("family: ")
                student.name = student_name
                student.family = student_family
            Student.editStudent(student)
        elif cmd == 4:
            student_id = int(input("id: "))
            Student.removeStudent(student_id)

        elif cmd == 5:
            for student in Student.students:
                print(student)
            id = int(input("id: "))
            Student.selected = Student.students[Student.students.index(
                Student(id, "", ""))]
            level = "select student"
        elif cmd == 6:
            level = "root"
    elif level == "select student":
        print("1-info")
        print("2-add course")
        print("3-delete course")
        print("4-set scores")
        print("5-back")
        cmd = int(input("Enter command: "))
        if cmd == 1:
            print(Student.selected.id)
            print(Student.selected.name)
            print(Student.selected.family)
            for course in Student.selected.courses:
                print(f"Course: {course.name}")
                print(f"Score: {course.score}")
        elif cmd == 2:
            for course in Course.courses:
                print(course)
            id = int(input("id: "))
            Student.selected.courses = copy.deepcopy(Student.selected.courses)
            Student.selected.courses.append(
                Course.courses[Course.courses.index(Course(id, "", ""))])
        elif cmd == 3:
            level = "delete course"
        elif cmd == 4:
            for course in Student.selected.courses:
                score = int(input(course))
                course.setScore(score)

        elif cmd == 5:
            level = "students"

    elif level == "classrooms":
        print("1-show classrooms")
        print("2-add classroom")
        print("3-back")
        cmd = int(input("Enter command: "))
        if cmd == 2:
            classroom_id = int(input("id: "))
            classroom_name = input("name: ")
            classroom = Classroom(classroom_id, classroom_name)
            Classroom.addClassroom(classroom)
            for course in Course.courses:
                print(course)
            id = int(input("id: "))
            classroom.course = Course.courses[Course.courses.index(
                Course(id, "", ""))]
            for teacher in Teacher.teachers:
                if int(classroom.course.id) in teacher.courses:
                    print(teacher)
            id = int(input("id: "))
            classroom.course = Course.courses[Course.courses.index(
                Course(id, "", ""))]
            for student in Student.students:
                for course in student.courses:
                    if course["id"] == classroom.course.id and course["score"] == 0:
                        print(student)
        if cmd == 3:
            level = "root"