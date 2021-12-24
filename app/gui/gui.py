from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Window.clearcolor = (1, 1, 1, 1)
screen = Screen()

username = TextInput(text = "Enter Username",
                            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                            size_hint = (0.5, 0.06))

btn = Button(text = "Log In",
                     font_size ="20sp",
                     background_color =(0.88, 0.67, 1, 1),
                     color =(1, 0.83, 0.03, 1),
                     size =(32, 16),
                     size_hint =(0.1, 0.05),
                     pos =(199, 250))

lbl = Label(text = "[b]Graduate Thesis System Database Manager[/b]", 
            font_size ='20sp',
            color =[0.41, 0.42, 0.74, 1],
            pos = (0, 280),
            markup = True)

class P(FloatLayout):
    pass

def show_popup():
    show = P() 
    popupWindow = Popup(title="Error. The username does not exist.", 
    content = show, size_hint = (None,None), size = (200, 100)) 
    popupWindow.open()

class DBApp(App):
    def build(self):
        self.img = Image(source ='user.png')
        self.img.size_hint_x = 0.1
        self.img.size_hint_y = 0.1
        self.img.pos = (183, 314)
        btn.bind(on_press = self.callback)
        username.foreground_color = (1,0,0,1)
        screen.add_widget(username)
        screen.add_widget(self.img)
        screen.add_widget(btn)
        return screen 
    def callback(self, event):
        if username.text == "admin" or username.text == "volkan" or username.text == "yavuz":
            screen.remove_widget(username)
            screen.remove_widget(self.img)
            screen.remove_widget(btn)
            screen.add_widget(lbl)
        else:
            show_popup()

DBApp().run()