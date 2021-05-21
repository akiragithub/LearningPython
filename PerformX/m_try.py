from kivy.app import App
from kivy.factory import Factory
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_string("""
<LoginScreen>:
    nbr: 0
    BoxLayout:
        orientation:'vertical'
        Label:
            text: 'I am LoginScreen'
        Label:
            id: lbl1
            # text: 'value received is '+str(app.MY_NUMBER)
        Button:
            text: 'Read'
            on_press: root.press_read()
        Button:
            text: 'Change'
            on_press:
                app.MY_NUMBER = app.MY_NUMBER + 1
                root.ids.lbl1.text = 'SharedVar is ' + str(app.MY_NUMBER)
        Button:
            text: 'Go to ScreenTwo'
            on_press: app.sm.current = "screen_2"
<MenuScreen>:
    nbr: 0
    BoxLayout:
        orientation:'vertical'
        Label:
            text: 'I am MenuScreen'
        Label:
            id: lbl2
            # text: 'value received is '+str(app.MY_NUMBER)            
        Button:
            text: 'Read'
            on_press: root.press_read()
        Button:
            text: 'Change'
            on_press:
                app.MY_NUMBER = app.MY_NUMBER + 1
                root.ids.lbl2.text = 'SharedVar is ' + str(app.MY_NUMBER)
        Button:
            text: 'Go to ScreenOne'
            on_press: app.sm.current = "screen_1"
            
<MScreenManager>:
    m_s: m_s
    l_s: l_s
    LoginScreen:
        id: l_s
        name: 'screen_1'
    MenuScreen:
        id: m_s
        name: 'screen_2'
            """)


class LoginScreen(Screen):
    nbr = NumericProperty(None)

    def press_read(self):
        app = App.get_running_app()
        # self.ids.lbl1.text = "SharedVar is " + str(app.MY_NUMBER)
        self.nbr = self.nbr + 1
        self.ids.lbl1.text = "Shared is "+str(self.nbr)
        App.get_running_app().sm.m_s.ids.lbl2.text = "Shared from l_s is "+str(self.nbr)


class MenuScreen(Screen):

    nbr = NumericProperty(None)

    def press_read(self):
        app = App.get_running_app()
        # self.ids.lbl2.text = "SharedVar is now " + str(app.MY_NUMBER)
        self.nbr = self.nbr + 1
        self.ids.lbl2.text = "Shared is "+str(self.nbr)
        App.get_running_app().sm.l_s.ids.lbl1.text = "Shared from m_s is "+str(self.nbr)


class MScreenManager(ScreenManager):
    pass


class HandSetApp(App):
    MY_NUMBER = 0
    sm = MScreenManager()

    def build(self):
        # HandSetApp.sm.add_widget(LoginScreen(name='screen_1', id='l_s'))
        # HandSetApp.sm.add_widget(MenuScreen(name='screen_2', id='m_s'))
        self.root = Factory.MScreenManager()
        return HandSetApp.sm


if __name__ == '__main__':
    HandSetApp().run()
