# -*- encoding:utf-8 -*-
# simple test app for
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty, StringProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.app import MDApp
import my_screens as m_screens
import dbmanager
import performx
from datatable import DataTableLayout

Builder.load_string(
    """
#:set color_shadow  [0, 0, 0, .299]
<StudentTeacherClasseRV>:
    viewclass: 'SelectableRow'
    SelectableRecycleBoxLayout:
        default_size: None, dp(100)
        default_size_hint: 1, None
        size_hint_y : None
        height: self.minimum_height
        orientation: 'vertical'
        # multiselect: False
        touch_multiselect: False
        
<SelectableRow>:
    size_hint_x: 1
    orientation: 'horizontal'
    canvas.before:
        Color: 
            rgba: color_shadow if self.selected  else (0.95, 0.95, 0.95, 1)
        RoundedRectangle:
            size: self.width, self.height
            pos: self.x, self.y
            radius: [20, 20, 20, 20]
    MDIconButton: 
        pos_hint: {'top': .75}
        icon: "class_px.png"
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            size_hint_y: None
            height: dp(30)
            text: root.text_1
        MDLabel:
            size_hint_y: None
            height: dp(30)
            text: root.text_2
        MDLabel:     
            size_hint_y: None
            height: dp(30)
            text: root.text_3
        # HLine:
        
<HLine>
    canvas:
        Color:
            rgba: app.theme_cls.primary_color
        Line:
            width: 1.5
            rectangle: (self.parent.x, self.y, self.parent.width, 0)

            
<mainScreen>:
    rv:rv
    StudentTeacherClasseRV:
        id: rv
    Button:
        text: 'reverse list'
        on_release: app.reverse_list()
    """)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    """ adds selection and focus behavior to the view"""


def display_class_students(class_name):
    my_screens = m_screens.MyScreens()
    students = dbmanager.get_all_students_from_given_classe(class_name)
    number_of_students = len(students)
    topics = dbmanager.get_all_topics_of_given_classe(class_name)
    number_of_topics = len(topics)
    number_of_topics = 10
    number_of_students = 6
    performx.PxApp.get_running_app().main_layout.main_scr_manager.class_students_screen.classe_name = class_name
    performx.PxApp.get_running_app().main_layout.main_scr_manager.class_students_screen.topics = topics
    performx.PxApp.get_running_app().main_layout.main_scr_manager.class_students_screen.students = students
    performx.PxApp.get_running_app().main_layout.main_scr_manager.class_students_screen.nb_of_topics = \
        str(number_of_topics)
    performx.PxApp.get_running_app().main_layout.main_scr_manager.class_students_screen.nb_of_students = \
        str(number_of_students)
    cells_dt = [{'cells': [[str(x) for x in range(0, 5)] for y in range(number_of_topics*number_of_students)],
                 'nb_of_topics': number_of_topics, 'nb_of_students': number_of_students}]
    cells_dt = [{'text_int_1': str(x), 'text_int_2': str(x + 1)} for x in range(10)]
    # performx.PxApp.get_running_app().main_layout.main_scr_manager.class_students_screen.rv.data = cells_dt
    dt = DataTableLayout(cols=4, rows=5)
    dt.size_hint_y = 5
    performx.PxApp.get_running_app().main_layout.main_scr_manager.class_students_screen.grades_layout.add_widget(dt)
    # performx.PxApp.get_running_app().main_layout.main_scr_manager.class_students_screen.dt = dt
    print("data in cells are : "+str(cells_dt))
    my_screens.setcurrent(my_screens.class_students_screen)


class SelectableRow(RecycleDataViewBehavior, BoxLayout):
    """  adds selection support to the label """
    index = None
    selectable = BooleanProperty(True)
    selected = BooleanProperty(False)
    text_1 = StringProperty()
    text_2 = StringProperty()
    text_3 = StringProperty()

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        super(SelectableRow, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super(SelectableRow, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if is_selected:
            # print("selection changed to {} ".format(rv.data[index]))
            classe_name = rv.data[index]['text_1'].split(':')[1].strip()
            # classe_name = 'essai'
            display_class_students(classe_name)
        else:
            pass
            # print("selection removed for {}".format(rv.data[index]))


class StudentTeacherClasseRV(RecycleView):
    def __init__(self, **kwargs):
        super(StudentTeacherClasseRV, self).__init__(**kwargs)
        self.data = [{'text_1': 'text_1 : '+str(x), 'text_2': 'text_2 : '+str(x), 'text_3': 'text_3 : '+str(x)} for x in range(100)]


class MainScreen(BoxLayout):
    orientation = 'vertical'


class HLine(BoxLayout):
    pass


class TestApp(MDApp):
    m_screen = ObjectProperty(None)

    def build(self):
        scr = MainScreen()
        self.m_screen = scr
        return scr

    def reverse_list(self):
        TestApp.get_running_app().m_screen.rv.data.reverse() #= [{'text': 'new' + str(x)} for x in range(100)]


if __name__ == "__main__":
    TestApp().run()