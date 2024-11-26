class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
 
    def rate_lecturer(self, lecturer, course, grade):
        if not (1 <= grade <= 10):
            return 'Ошибка: оценка должна быть в диапазоне от 1 до 10.'
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_count = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_count = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade:.1f}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if not (1 <= grade <= 10):
            return 'Ошибка: оценка должна быть в диапазоне от 1 до 10'
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка: неверный курс или объект'
 
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student2 = Student('John', 'Doe', 'male')
student2.courses_in_progress += ['Python']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Alice', 'Smith')
reviewer2.courses_attached += ['Python']

lecturer1 = Lecturer('Ruoy', 'Eman')
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer('Jane', 'Doe')
lecturer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 2)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student2, 'Python', 9)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 6)
student2.rate_lecturer(lecturer2, 'Python', 7)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

def average_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print(f'Средняя оценка за домашние задания по курсу Python: {average_hw_grade(students_list, "Python"):.1f}')
print(f'Средняя оценка за лекции по курсу Python: {average_lecture_grade(lecturers_list, "Python"):.1f}')