# -*- encoding:utf-8 -*-
########################################################################################################################
#                                     This is Screens python file for Px                                               #
#                                             @author suXess                                                           #
########################################################################################################################
from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivy import app

import dbmanager
import my_dialogs
import performx


class MyScreens:
    scr_mgr = None
    class_screen = ""
    students_screen = ""
    teachers_screen = ""
    stats_screen = ""
    cur_screen = ""
    login_screen = ""
    welcome_screen = ""
    class_students_screen = ""

    def __init__(self):
        my_app = App.get_running_app()
        self.scr_mgr = my_app.main_layout.main_scr_manager
        scr_mgr = self.scr_mgr
        self.class_screen = scr_mgr.class_screen
        self.students_screen = scr_mgr.students_screen
        self.teachers_screen = scr_mgr.teachers_screen
        self.stats_screen = scr_mgr.stats_screen
        self.login_screen = scr_mgr.login_screen
        self.welcome_screen = scr_mgr.welcome_screen
        self.class_students_screen = scr_mgr.class_students_screen
        self.cur_screen = scr_mgr.current

    def setcurrent(self, cur_scr):
        self.scr_mgr.current = cur_scr.name
        self.cur_screen = cur_scr.name

    def getcurrent(self):
        return self.cur_screen

    def getscrmgr(self):
        return self.scr_mgr


class MyLoginScreen(Screen):
    username = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def check_login(self):
        my_app = App.get_running_app()
        scr_manager = my_app.main_layout.main_scr_manager
        welcome_screen_str = scr_manager.welcome_screen.name
        user = self.username.text
        password = self.pwd.text
        print("(username, pass)", '(', user, password, ')')
        user = 'admin'
        password = 'admin'
        if user == 'admin' and password == 'admin':
            print("credentials are matching")
            scr_manager.current = welcome_screen_str


class MyWelcomeScreen(Screen):

    def __init__(self, **kwargs):
        my_app = App.get_running_app()
        my_app.my_welcome_scr = self
        # self.current_element = StringProperty()
        super(MyWelcomeScreen, self).__init__(**kwargs)

    def switch_to_entities_screen(self, btn_name):
        my_screens = MyScreens()
        if btn_name == "reports_btn":
            print("button name is 1 : ", btn_name)
            my_screens.setcurrent(my_screens.stats_screen)
        elif btn_name == "students_btn":
            print("button name is 2 : ", btn_name)
            my_screens.setcurrent(my_screens.students_screen)
        elif btn_name == "class_btn":
            print("button name is 3 :", btn_name)
            # print("previous data : " + str(performx.PxApp.get_running_app()
            #                                .my_student_teacher_classe_screen.cst_rv.data))
            classes = dbmanager.get_all(dbmanager.DbClassroom)
            classes_data = []
            for classe in classes:
                name = classe.id
                # updating number of students in the classroom
                classe.nb_students = dbmanager.get_number_of_students_from_given_class(name)
                nb_students = classe.nb_students
                pp_id = dbmanager.get_principal_teacher_mle(name)
                pp_name_surname = ""
                if pp_id:
                    pp = dbmanager.get_teacher_by_id(pp_id)[0]
                    print("pp is : "+str(pp))
                    pp_name_surname = pp.name + " " + pp.surname
                    pp_name_surname = 'Professeur principal : ' + pp_name_surname
                entry = {'text_1': 'Classe : ' + name, 'text_2': 'Effectif : ' + str(nb_students), 'text_3': pp_name_surname}
                classes_data.append(entry)
            performx.PxApp.get_running_app().change_cst_rv_data(classes_data)
            print("clock here ? ")
            my_screens.setcurrent(my_screens.class_screen)
        elif btn_name == "teachers_btn":
            print("button name is 4 : ", btn_name)
            my_screens.setcurrent(my_screens.teachers_screen)
        else:
            #   This should never occur
            pass


class MyClassScreen(Screen):

    cst_rv = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MyClassScreen, self).__init__(**kwargs)

    def add_element(self):
        dialog = my_dialogs.AddClassDialog()
        dialog.open()


class MyStudentScreen(Screen):

    def __init__(self, **kwargs):
        super(MyStudentScreen, self).__init__(**kwargs)

    def add_element(self):
        # self.get_center_x()
        dialog = my_dialogs.AddStudentDialog()
        dialog.open()


class MyTeacherScreen(Screen):
    def __init__(self, **kwargs):
        super(MyTeacherScreen, self).__init__(**kwargs)

    def add_element(self):
        # self.get_center_x()
        dialog = my_dialogs.AddTeacherDialog()
        dialog.open()


class MyStatsScreen(Screen):
    def __init__(self, **kwargs):
        super(MyStatsScreen, self).__init__(**kwargs)

    def add_element(self):
        dialog = my_dialogs.AddStatsDialog()
        dialog.open()


class MyClassRoomStudentsScreen(Screen):
    rv = ObjectProperty()
    grades_cells = ListProperty()
    grades_table = ObjectProperty()
    grades_layout = ObjectProperty()
    # nb_of_students: ""
    # nb_of_topics: ""

    def __init__(self, **kwargs):
        super(MyClassRoomStudentsScreen, self).__init__(**kwargs)

    def fill_rows(self):
        self.rv.data = [{'text_int_1': str(x), 'text_int_2': str(x)} for x in range(10)]
        pass

    def setup_display(self, classe_name):
        classe_students = []
        classe_students = dbmanager.get_all_students_from_given_classe(classe_name)
        classe_topics = dbmanager.get_all_topics_of_given_classe(classe_name)

