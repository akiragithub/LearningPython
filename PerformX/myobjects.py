# -*- encoding:utf-8 -*-
################################################################################
# @ author : suXess                                                            #
# @ date : 31/12/2020                                                          #
################################################################################
"""
    This object contains my classes for Performx management
    Theses classes are : Student, Teacher, Classroom,.....
"""


class Student:
    # name = None
    # surname = None
    # mle = None
    # classroom = None
    # birthday = None
    # city = None
    # country = None

    def __init__(self, name, surname, mle, classroom, birthday, city, country="Benin"):
        self.name = name
        self.surname = surname
        self.mle = mle
        self.classroom = classroom
        self.birthday = birthday
        self.city = city
        self.country = country


class Teacher:

    def __init__(self, name, surname, mle, classrooms, majors, diploma, pmb_entry_date=None):
        self.name = name
        self.surname = surname
        self.mle = mle
        self.classrooms = classrooms
        self.majors = majors
        self.diploma = diploma
        self.pmb_entry_date = pmb_entry_date


class Classroom:

    def __init__(self, name, responsible_teacher, number_of_students, majors, students=[]):
        self.name = name
        self.responsible_teacher = responsible_teacher
        self.number_of_students = number_of_students
        self.majors = majors
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_mle):
        for student in self.students:
            if int(student.mle) == int(student_mle):
                self.students.remove(student)
                break


class Stats:

    def __init__(self, year, percent_bac, percent_bepc, high_grade_bac, high_grade_bepc, low_grade_bac, low_grade_bepc,
                 percent_tle, percent_premiere, percent_seconde, percent_troisieme, percent_quatrieme,
                 percent_cinquieme, percent_sixieme,
                 high_grade_tle, high_grade_premiere, high_grade_seconde, high_grade_troisieme, high_grade_quatrieme,
                 high_grade_cinquieme, high_grade_sixieme,
                 low_grade_tle, low_grade_premiere, low_grade_seconde, low_grade_troisieme, low_grade_quatrieme,
                 low_grade_cinquieme, low_grade_sixieme):
        self.year = year
        self.percent_bac = percent_bac
        self.percent_bepc = percent_bepc
        self.high_grade_bac = high_grade_bac
        self.high_grade_bepc = high_grade_bepc
        self.low_grade_bac = low_grade_bac
        self.low_grade_bepc = low_grade_bepc
        self.percent_tle = percent_tle
        self.percent_premiere = percent_premiere
        self.percent_seconde = percent_seconde
        self.percent_troisieme = percent_troisieme
        self.percent_quatrieme = percent_quatrieme
        self.percent_cinquieme = percent_cinquieme
        self.percent_sixieme = percent_sixieme
        self.high_grade_tle = high_grade_tle
        self.high_grade_premiere = high_grade_premiere
        self.high_grade_seconde = high_grade_seconde
        self.high_grade_troisieme = high_grade_troisieme
        self.high_grade_quatrieme = high_grade_quatrieme
        self.high_grade_cinquieme = high_grade_cinquieme
        self.high_grade_sixieme = high_grade_sixieme
        self.low_grade_tle = low_grade_tle
        self.low_grade_premiere = low_grade_premiere
        self.low_grade_seconde = low_grade_seconde
        self.low_grade_troisieme = low_grade_troisieme
        self.low_grade_quatrieme = low_grade_quatrieme
        self.low_grade_cinquieme = low_grade_cinquieme
        self.low_grade_sixieme = low_grade_sixieme
