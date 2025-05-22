class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (
            course in (self.courses_in_progress or self.finished_courses)
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print(
                "Ошибка: лектор не закреплен за этим курсом или студент не записан на этот курс"
            )

    def __str__(self):
        return (
            f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\n"
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        )

    def average_grade(self):
        avg = 0
        cnt = 0
        for grade in self.grades.values():
            avg += sum(grade)
            cnt += len(grade)
        return avg / cnt

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def average_grade(self):
        avg = 0
        cnt = 0
        for grade in self.grades.values():
            avg += sum(grade)
            cnt += len(grade)
        return avg / cnt

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_grade_students(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grades / total_students if total_students > 0 else 0


def average_grade_lecturers(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    return total_grades / total_lecturers if total_lecturers > 0 else 0


student_1 = Student("Ivan", "Ivanov", "male")
student_1.courses_in_progress += ["Python", "web_dev"]
student_1.finished_courses += ["Git"]
student_2 = Student("Anna", "Rozhkova", "female")
student_2.courses_in_progress += ["Python", "Git"]
student_2.finished_courses += ["web_dev"]

lecturer_1 = Lecturer("Oleg", "Bulygin")
lecturer_1.courses_attached += ["Python", "web_dev"]
lecturer_2 = Lecturer("Andrey", "Melnikov")
lecturer_2.courses_attached += ["Python", "Git"]

reviewer_1 = Reviewer("Igor", "Smirnov")
reviewer_1.courses_attached += ["Python", "web_dev"]
reviewer_2 = Reviewer("Oksana", "Karpova")
reviewer_2.courses_attached += ["Python", "Git"]

student_1.rate_lecturer(lecturer_1, "Python", 10)
student_1.rate_lecturer(lecturer_2, "Python", 9)
student_2.rate_lecturer(lecturer_1, "web_dev", 8)
student_2.rate_lecturer(lecturer_2, "Git", 6)

reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "web_dev", 9)
reviewer_2.rate_hw(student_2, "Python", 8)
reviewer_2.rate_hw(student_2, "Git", 6)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_1 == student_2)
print(lecturer_1 < lecturer_2)


lst_students = [student_1, student_2]
lst_lecturers = [lecturer_1, lecturer_2]

print(
    "Средняя оценка студентов по курсу Python:",
    average_grade_students(lst_students, "Python"),
)
print(
    "Средняя оценка студентов по курсу web_dev:",
    average_grade_students(lst_students, "web_dev"),
)
print(
    "Средняя оценка студентов по курсу Git:",
    average_grade_students(lst_students, "Git"),
)
print(
    "Средняя оценка лекторов по курсу Python:",
    average_grade_lecturers(lst_lecturers, "Python"),
)
print(
    "Средняя оценка лекторов по курсу web_dev:",
    average_grade_lecturers(lst_lecturers, "web_dev"),
)
print(
    "Средняя оценка лекторов по курсу Git:",
    average_grade_lecturers(lst_lecturers, "Git"),
)
