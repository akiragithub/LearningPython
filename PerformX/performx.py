# -*- encoding: utf-8 -*-
# from kivy.config import Config
# # Changing configuration must be the very first thing if it must happen
# Config.set('graphics', 'borderless', '1')
from functools import partial
from random import Random

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import ThreeLineAvatarIconListItem, MDList, ThreeLineAvatarListItem, ImageLeftWidget
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextFieldRound, MDTextField

from kivy_garden.SimpleTableLayout import SimpleTableLayout

import dbmanager

from datetime import datetime

import my_screens
import my_screens as m_screens

import student_teacher_classe_rv_layout


class MyContentNavigationDrawer(BoxLayout):
    pass


class MyCircledImage(BoxLayout):
    pass


class MyToolbar(BoxLayout):
    pass


class MyMDTextFieldRound(MDTextFieldRound):
    pass


def is_valid_name(name_to_check):
    return name_to_check is not None and len(name_to_check) > 0


def is_valid_number(number_to_check):
    try:
        int(number_to_check)
        return True
    except Exception as e:
        return False


def format_date(date_str):
    data = str.split(date_str, sep="/")
    try:
        year = data[0]
        month = data[1]
        day = data[2]
        return datetime(int(year), int(month), int(day))
    except Exception as e:
        print("Exception is :", e)
        return None


def add_btn_to_layout(dropdown_src, layout):
    btn_to_add = MDRoundFlatButton(pos_hint={'top': 1})  # pos_hint={'center_x':0, 'center_y':0.5})
    current = dropdown_src.current_item
    first_item = dropdown_src.items[0]
    if current != first_item:
        btn_to_add.text = dropdown_src.current_item
        btn_to_add.bind(on_release=lambda x: remove_btn_from_layout(layout, btn_to_add))
        btn_to_add.color = "Primary"
        layout.add_widget(btn_to_add)


def remove_btn_from_layout(layout, btn):
    print("we are removing widget")
    layout.remove_widget(btn)


def get_selected_items_from_gl(grid_layout):
    children = grid_layout.children
    selected_items = []
    for child in children:
        selected_items.append(child)
    return selected_items


class MyPopUpBackground(Widget):
    pass


class MySearchBar(BoxLayout):
    pass


class MyListItem(ThreeLineAvatarListItem):
    pass


class MyAvatarList(BoxLayout):
    cst_rv = ObjectProperty(None)
    current_list = None

    def add_item(self, table_to_fetch):
        # avatars_list = self.avatars_list
        self.current_list = table_to_fetch
        first_line_text = None
        second_line_text = None
        third_line_text = None
        if table_to_fetch == "DbStudent":
            self.display_students()
        elif table_to_fetch == "DbTeacher":
            self.display_teachers()
        elif table_to_fetch == "DbClassroom":
            self.display_classrooms()

        # cst_rv = self.cst_rv

    def display_students(self):
        first_line_text = "Nom : {}"
        second_line_text = "Prénoms : {}"
        third_line_text = "Mle : {} Classe {}"
        table_entries = dbmanager.get_all(dbmanager.DbStudent)
        for entry in table_entries:
            text = first_line_text.format(entry.name)
            secondary_text = second_line_text.format(entry.surname)
            tertiary_text = third_line_text.format(entry.id, entry.class_id)
            self.cst_rv.data.append({'text': text, 'secondary_text': secondary_text, 'tertiary_test': tertiary_text})

    def display_teachers(self):
        first_line_text = "Nom : {}"
        second_line_text = "Prénoms : {}"
        third_line_text = "Matiere : {}"
        table_entries = dbmanager.get_all(dbmanager.DbTeacher)
        for entry in table_entries:
            item = ThreeLineAvatarListItem()
            item.text = first_line_text.format(entry.name)
            item.secondary_text = second_line_text.format(entry.surname)
            item.tertiary_text = third_line_text.format(entry.topic_name)
            item.secondary_theme_text_color = 'Primary'
            item.tertiary_theme_text_color = "Primary"
            # item.width = self.parent.width/2
            icon = ImageLeftWidget()
            icon.source = f"teacher_px.png"
            item.add_widget(icon)
            self.avatars_list.add_widget(widget=item)


class MyRoundedImageButton(BoxLayout):
    pass


class GradesCell(BoxLayout):
    text_int_1 = StringProperty()
    text_int_2 = StringProperty()
    text_int_3 = StringProperty()
    text_dev_1 = StringProperty()
    text_dev_2 = StringProperty()
    # int_1, int_2, int_3, dev_1, dev_2

    def __init__(self, **kwargs):
        super(GradesCell, self).__init__(**kwargs)


class HLine(BoxLayout):
    pass


class MyLayout(BoxLayout):
    main_scr_manager = ObjectProperty(None)
    # welcome_screen = ObjectProperty(None)
    # login_screen = ObjectProperty(None)


class MyScreenManager(ScreenManager):
    pass


class Px:
    def __init__(self, **kwargs):
        self.topics_names = ['Anglais', 'Allemand', 'Comm. Ecrite', 'Dictee', 'EPS', 'Espagnol', 'Hist-Géo', 'IM',
                             'Lecture', 'PCT', 'Philosophie', 'SVT']
        self.classrooms = ["6eme", "5eme", "4eme A", "4eme B", "3eme A", "3eme B", "2nde A", "2nde C",
                           "2nde D", "1ere A", "1ere C", "1ere D", "Tle A", "Tle C", "Tle D"]
        self.countries = ["Benin", "Burkina-Faso", "Centrafrique", "Cote d\'Ivoire", "Niger", "Senegal", "Tchad",
                          "Togo"]
        self.initialize_db()
        self.teachers = get_teachers_name_surnames_mle(dbmanager.get_all_teachers())
        print("teachers list :", self.teachers)
        self.registered_classrooms = dbmanager.get_all(dbmanager.DbClassroom)
        print("classes list :", self.registered_classrooms)
        self.registered_class_name = []
        for cl in self.registered_classrooms:
            self.registered_class_name.append(cl.id)
        print("classes names list : ", self.registered_class_name)

    def initialize_db(self):
        topics = []
        for topic in self.topics_names:
            topics.append(dbmanager.DbTopic(name=topic))
        dbmanager.add_all(topics)

    def save_to_db(self, element):
        dbmanager.additem(element)


def get_teachers_name_surnames_topics(teachers_list):
    li = []
    for item in teachers_list:
        entry = item.surname + " " + item.name + " - " + item.topic_name
        li.append(entry)
    return li


def get_teachers_name_surnames_mle(teachers_list):
    li = []
    for item in teachers_list:
        entry = item.surname + ' ' + item.name + " " + str(item.id)
        li.append(entry)
    return li


class PxApp(MDApp):
    main_layout = ObjectProperty(None)
    my_welcome_scr = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.title = "PerformX"
        self.theme_cls = ThemeManager()
        self.px_model = Px()
        super().__init__(**kwargs)

    def build(self):
        Builder.load_file('my_widgets.kv')
        Builder.load_file('my_screens.kv')
        Builder.load_file('my_dialogs.kv')
        self.main_layout = MyLayout()
        return self.main_layout

    def show_password(self):
        pass

    def go_back(self):
        my_screens = m_screens.MyScreens()
        cur_scr = my_screens.getcurrent()
        if cur_scr == my_screens.class_screen.name or cur_scr == my_screens.teachers_screen.name \
                or cur_scr == my_screens.students_screen.name or cur_scr == my_screens.stats_screen.name:
            my_screens.setcurrent(my_screens.welcome_screen)
        elif cur_scr == my_screens.welcome_screen.name:
            my_screens.setcurrent(my_screens.login_screen)
        elif cur_scr == my_screens.class_students_screen.name:
            my_screens.setcurrent(my_screens.class_screen)

    def change_cst_rv_data(self, new_data):
        self.main_layout.main_scr_manager.class_screen.cst_rv.data = new_data

    def change_classes_data(self):
        self.main_layout.main_scr_manager.class_students_screen.rv.data = [{'text_int_1': str(x), 'text_int_2': str(x)} for x in range(10)]


if __name__ == '__main__':
    # read_config_file()
    PxApp().run()
