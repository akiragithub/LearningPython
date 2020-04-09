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
from kivymd.uix.label import MDLabel

Builder.load_string(
    """
<RV>:
    viewclass: 'SelectableRow'
    SelectableRecycleBoxLayout:
        default_size: None, dp(100)
        default_size_hint: 1, None
        size_hint_y : None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
        
<SelectableRow>:
    size_hint_x: 1
    orientation: 'horizontal'
    padding: dp(20)
    canvas.before:
        Color: 
            rgba: (0.1, 0.9, 0.1, 0.3) if self.selected else (0, 0, 0, 1)
    MDIconButton: 
        pos_hint: {'top': 1.25}
        icon: "class_px.png"
    BoxLayout:
        orientation: 'vertical'
        # spacing: dp(20)
        # padding: dp(100)
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
        HLine:
        
<HLine>
    canvas:
        Color:
            rgba: app.theme_cls.primary_color
        Line:
            width: 1.5
            rectangle: (self.parent.x, self.y, self.parent.width, 0)

            
            
<mainScreen>:
    rv:rv
    RV:
        id: rv
    Button:
        text: 'reverse list'
        on_release: app.reverse_list()
    """)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    """ adds selection and focus behavior to the view"""


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
            print("selection changed to {} ".format(rv.data[index]))
            # rv.data.clear()
            # rv.refresh_from_data()
        else:
            print("selection removed for {}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
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