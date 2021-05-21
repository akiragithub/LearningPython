# -*- encoding:utf-8 -*-
########################################################################################################################
#                                     This is Dialogs python file for Px                                               #
#                                             @author suXess                                                           #
########################################################################################################################
from functools import partial
from random import Random

from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

import dbmanager
import performx


class AddTeacherDialog(Popup):
    name_tf = ObjectProperty()
    surname_tf = ObjectProperty()
    mle_tf = ObjectProperty()
    classes_dd = ObjectProperty()
    subjects_tf = ObjectProperty()
    diploma_dd = ObjectProperty()
    date_tf = ObjectProperty()
    birth_city_tf = ObjectProperty
    countries_dd = ObjectProperty()
    classrooms_gl = ObjectProperty
    # selected_classrooms = []
    pass_date = False

    def __init__(self):
        super(AddTeacherDialog, self).__init__()

    def save_date(self, date_to_save):
        pass

    def on_classroom_selected(self):
        current_class = self.classes_dd
        performx.add_btn_to_layout(current_class, self.classrooms_gl)

    def valid_data(self, teacher_diploma, teacher_subject, teacher_classes, dt, pass_date, teacher_mle,
                   teacher_name,
                   teacher_surname):
        teacher_id = None
        try:
            teacher_id = int(teacher_mle)
        except Exception as e:
            pass

        if teacher_diploma == "Diplome":
            info = "Choisissez le diplome"
            dialog = MDDialog(title="Renseignements incomplets",
                              auto_dismiss=False,
                              size_hint=(0.5, 0.5),
                              text=info,
                              text_button_ok="Compris",
                              )
            dialog.open()
            return False

        elif teacher_subject == "Matiere enseignee":
            info_label = MDLabel()
            info = "Quelle est la matiere enseignee ?"
            dialog = MDDialog(title="Renseignements incomplets",
                              auto_dismiss=False,
                              size_hint=(0.5, 0.5),
                              text=info,
                              text_button_ok="Compris",
                              )
            dialog.open()
            return False

        elif not teacher_classes:
            info = "Ce professeur n'intervient dans aucune classe ?"
            dialog = MDDialog(title="Renseignements incomplets",
                              auto_dismiss=False,
                              size_hint=(0.5, 0.5),
                              text=info,
                              text_button_ok="Compris",
                              )
            dialog.open()
            return False

        elif not dt and not pass_date:
            info = "La date entrée n'est pas correcte. Elle ne sera donc pas validée si elle était maintenue"
            dialog = MDDialog(title="Date non correcte",
                              auto_dismiss=False,
                              size_hint=(0.5, 0.5),
                              text=info,
                              text_button_ok="Compris",
                              # on=,
                              )
            pass_date = True

            dialog.open()
            return False

        elif not teacher_mle or not teacher_name or not teacher_surname or teacher_id is None:
            info = "Veuillez vérifier les informations personnelles de ce professeur"
            dialog = MDDialog(title="Renseignements incomplets",
                              auto_dismiss=False,
                              size_hint=(0.5, 0.5),
                              text=info,
                              text_button_ok="Compris",
                              )
            dialog.open()
            return False
        else:
            return True

    def save_teacher(self):
        teacher_name = self.name_tf.text
        teacher_surname = self.surname_tf.text
        teacher_mle = self.mle_tf.text
        teacher_classes_btn_lst = performx.get_selected_items_from_gl(self.classrooms_gl)
        teacher_classes = []
        for item in teacher_classes_btn_lst:
            teacher_classes.append(item.text)
        teacher_subject = self.subjects_dd.current_item
        teacher_diploma = self.diploma_dd.current_item
        teacher_date = self.date_tf.text

        # Only for test purpose
        teacher_name = "Milliardaire"
        teacher_surname = "Success"
        rand = Random()
        teacher_mle = rand.randrange(start=0, stop=10000)
        print("Id is :", teacher_mle)
        teacher_classes = ['4eme A']
        teacher_subject = "Dictee"
        teacher_diploma = "Doctorat"
        teacher_date = "2020/12/12"

        dt = performx.format_date(teacher_date)
        valid = self.valid_data(teacher_diploma, teacher_subject, teacher_classes, dt, self.pass_date, teacher_mle,
                                teacher_name,
                                teacher_surname)
        if valid:
            print("teacher_name:", teacher_name, "\n",
                  "teacher_surname:", teacher_surname, "\n",
                  "teacher_mle", teacher_mle, "\n",
                  "teacher_classes", teacher_classes, "\n",
                  "teacher_date", teacher_date, "\n",
                  "teacher subjects", teacher_subject, "\n",
                  "teacher_diploma", teacher_diploma, "\n"
                  )
            self.dismiss()
            teacher = dbmanager.DbTeacher(id=teacher_mle, name=teacher_name, surname=teacher_surname,
                                          topic_name=teacher_subject, diploma=teacher_diploma, entry_date=dt)
            dbmanager.additem(teacher)
            intervenir_entries = []
            for classroom in teacher_classes:
                relation_intervenir = dbmanager.DbIntervenir(class_id=classroom, teacher_id=teacher_mle, isPP=False)
                intervenir_entries.append(relation_intervenir)
            dbmanager.add_all(intervenir_entries)


class AddStatsDialog(Popup):
    name_tf = ObjectProperty()
    surname_tf = ObjectProperty()
    mle_tf = ObjectProperty()
    classes_tf = ObjectProperty()
    subjects_tf = ObjectProperty()
    diploma_dd = ObjectProperty()
    date_tf = ObjectProperty()
    birth_city_tf = ObjectProperty
    countries_dd = ObjectProperty()

    def __init__(self):
        super(AddStatsDialog, self).__init__()

    def save_date(self, date_to_save):
        pass

    def save_stats(self):
        pass
        # teacher_name = self.name_tf.text
        # teacher_surname = self.surname_tf.text
        # teacher_mle = self.mle_tf.text
        # teacher_classes = self.classes_tf.text
        # teacher_subjects = self.subjects_tf.text
        # teacher_diploma = self.diploma_dd.current_item
        # teacher_date = self.date_tf.text
        # print("teacher_name:", teacher_name, "\n",
        #       "teacher_surname:", teacher_surname, "\n",
        #       "teacher_mle", teacher_mle, "\n",
        #       "teacher_classes", teacher_classes, "\n",
        #       "teacher_date", teacher_date, "\n",
        #       "teacher subjects", teacher_subjects, "\n",
        #       "teacher_diploma", teacher_diploma, "\n"
        #       )
        # if teacher_diploma == "Diplome":
        #     info_label = MDLabel()
        #     info = "Choisissez le diplome"
        #     dialog = MDDialog(title="Renseignements incomplets",
        #                       auto_dismiss=False,
        #                       size_hint=(0.5, 0.5),
        #                       text=info,
        #                       text_button_ok="Compris",
        #                       )
        #     dialog.open()
        # else:
        #     self.dismiss()


class AddStudentDialog(Popup):
    name_tf = ObjectProperty()
    surname_tf = ObjectProperty()
    mle_tf = ObjectProperty()
    classes_dd = ObjectProperty()
    date_tf = ObjectProperty()
    birth_city_tf = ObjectProperty()
    countries_dd = ObjectProperty()

    def __init__(self):
        super(AddStudentDialog, self).__init__()

    def show_countries_drop_down(self):
        pass

    def save_date(self, date_to_save):
        pass

    def valid_data(self, student_name, student_surname, student_mle, student_classe, student_country, student_date):

        valid_name = performx.is_valid_name(student_name)
        valid_surname = performx.is_valid_name(student_surname)
        valid_mle = performx.is_valid_number(student_mle)
        valid_classe = student_classe != self.classes_dd.items[0]
        valid_country = student_country != self.countries_dd.items[0]
        formatted_date = performx.format_date(student_date)
        valid_date = formatted_date is not None
        info = None
        if not valid_name or not valid_surname or not valid_mle or not valid_date or not valid_classe \
                or not valid_country:

            if not valid_name:
                info = "Veuillez verifier le nom"
            elif not valid_surname:
                info = "Veuillez verifier le prenom"
            elif not valid_mle:
                info = "Veuillez verifier le matricule"
            elif not valid_classe:
                info = "Veuillez verifier la classe"
            elif not valid_country:
                info = "Revoyez le pays"
            elif not valid_date:
                info = "Revoyez la date de naissance"

            dialog = MDDialog(title="Renseignements incomplets",
                              auto_dismiss=False,
                              size_hint=(0.5, 0.5),
                              text=info,
                              text_button_ok="Compris",
                              )
            dialog.open()
            return False
        else:
            return True

    def save_student(self):
        student_name = self.name_tf.text
        student_surname = self.surname_tf.text
        student_mle = self.mle_tf.text
        student_classe = self.classes_dd.current_item
        student_date = self.date_tf.text
        student_city = self.birth_city_tf.text
        student_country = self.countries_dd.current_item

        student_name = "Me " + str(Random().randrange(0, 100))
        student_surname = "Success " + str(Random().randrange(0, 100))
        student_mle = Random().randrange(0, 100)
        student_classe = my_app.px_model.classrooms[Random().randrange(1, 15)]
        student_date = "2014/02/07"
        student_city = "Bohicon"
        student_country = my_app.px_model.countries[Random().randrange(1, 7)]

        if self.valid_data(student_name, student_surname, student_mle, student_classe, student_country, student_date):
            print("student_name:", student_name, "\n",
                  "student_surname:", student_surname, "\n",
                  "student_mle", student_mle, "\n",
                  "student_classe", student_classe, "\n",
                  "student_date", student_date, "\n",
                  "student_city", student_city, "\n",
                  "student_country", student_country, "\n"
                  )

            student = dbmanager.DbStudent(id=int(student_mle), name=student_name, surname=student_surname,
                                          class_id=student_classe, birthday=performx.format_date(student_date),
                                          city=student_city, country=student_country)
            dbmanager.additem(student)
            self.dismiss()


class AddClassDialog(Popup):
    name_dd = ObjectProperty()
    p_teacher_dd = ObjectProperty()
    number_of_students_tf = ObjectProperty()
    majors_dd = ObjectProperty()
    topics_gl = ObjectProperty()
    topics_dict = {}

    def __init__(self):
        super(AddClassDialog, self).__init__()

    def add_topic_to_layout(self, dropdown_src, layout):
        current = dropdown_src.current_item
        first_item = dropdown_src.items[0]
        if current != first_item:
            # bl = BoxLayout(pos_hint={'top': 1})
            coeff_tf = performx.MyMDTextFieldRound(size_hint_x=None, width=dp(150))
            coeff_tf.hint_text = "coeff. de " + current
            coeff_tf.icon_type = 'right'
            coeff_tf.icon_right = 'playlist-remove'
            coeff_tf.icon_callback = partial(self.remove_topic_from_layout, layout, coeff_tf)
            layout.add_widget(coeff_tf)
            self.topics_dict[coeff_tf] = current

    def remove_topic_from_layout(self, layout, textfield, x, y):
        layout.remove_widget(textfield)
        print("topics len :", len(self.topics_dict))
        del self.topics_dict[textfield]
        print("topics len after :", len(self.topics_dict))

    def on_major_selected(self):
        current_dd = self.majors_dd
        self.add_topic_to_layout(current_dd, self.topics_gl)

    def are_valid_topics(self):
        if len(self.topics_dict) == 0:
            return False, None
        for topic, coeff in self.topics_dict.items():
            if not isinstance(topic, performx.MyMDTextFieldRound):
                if not performx.is_valid_number(coeff):
                    return False, topic
        return True

    def valid_data(self, classe_name, p_teacher, classe_number_of_students):
        valid_name = classe_name != self.name_dd.items[0]
        valid_teacher = p_teacher != self.p_teacher_dd.items[0]
        valid_number_of_students = performx.is_valid_number(classe_number_of_students)
        valid_topics = self.are_valid_topics()
        topic_validity = valid_topics
        if isinstance(valid_topics, tuple):
            topic_validity = valid_topics[0]
        if valid_name and valid_teacher and valid_number_of_students and topic_validity:
            return True
        elif not topic_validity:
            reason = valid_topics[1]
            if reason is None:
                info = "Veuillez renseigner les matières de cette classe"
            else:
                info = "Le coefficient de %s n'est pas correct" % (reason)
        else:
            info = "Verifiez les informations insérées"
        dialog = MDDialog(title="Renseignements incorrects",
                          auto_dismiss=False,
                          size_hint=(0.5, 0.5),
                          text=info,
                          text_button_ok="Compris",
                          )
        dialog.open()
        return False

    def save_class(self):
        classe_name = self.name_dd.current_item
        p_teacher = self.p_teacher_dd.current_item
        classe_number_of_students = self.number_of_students_tf.text
        classe_majors = performx.get_selected_items_from_gl(self.topics_gl)
        # for topic in classe_majors:
        #     coeff = topic.text  # Then get the coefficient from the textfield
        #     topic_nm = self.topics_dict[topic]                # first get the associated topic wiht the textfield id
        #     self.topics_dict[topic_nm] = coeff                # Add new entry to the dixt
        #     # del self.topics_dict[topic]
        # print("classe_name:", classe_nm, "\n",
        #       "classe_main_teacher:", p_teacher, "\n",
        #       "classe_number_of_students", classe_number_of_students, "\n",
        #       "classe_majors", classe_majors, "\n"
        #       )
        classe_name = my_app.px_model.classrooms[Random().randrange(1, 15)]
        p_teacher = "Success Milliardaire - 8305"
        topic_nm = "Dictee"
        classe_number_of_students = dbmanager.get_number_of_students_of_given_class(classe_name)
        coeff = self.topics_dict[topic_nm] = Random().randrange(start=1, stop=6)

        if self.valid_data(classe_name, p_teacher, classe_number_of_students):
            classroom = dbmanager.DbClassroom(id=classe_name, nb_students=int(classe_number_of_students))
            dbmanager.additem(classroom)
            posseder_relation = dbmanager.DbPosseder(class_id=classe_name, topic_name=topic_nm, coeff_classe=coeff)
            dbmanager.additem(posseder_relation)
            teacher_mle = int(p_teacher.split('-')[1])
            intervenir_relation = dbmanager.DbIntervenir(class_id=classe_name, teacher_id=teacher_mle, isPP=True)
            dbmanager.additem(intervenir_relation)
            self.dismiss()

my_app = performx.PxApp