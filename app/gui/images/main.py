from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image

from user import username
from button import btn, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10
from label import lbl
from popup import show_popup
from scr import screen
from dbsys import create_table, delete_table, insert_to_table, read_table, clear_table, order_by

Window.clearcolor = (0.1, 0.6, 0.2, 0.6)

class DBApp(App):

    def build(self):
        self.img = Image(source ='user.png')
        self.img.size_hint_x = 0.1
        self.img.size_hint_y = 0.1
        self.img.pos = (181, 314)
        self.ext = Image(source ='exit.png')
        self.ext.size_hint_x = 0.06
        self.ext.size_hint_y = 0.06
        self.ext.pos = (740, 550)
        self.sec = Image(source ='section.png')
        self.sec.size_hint_x = 0.9
        self.sec.size_hint_y = 0.9
        self.sec.pos = (340, -30)
        btn.bind(on_press = self.callback)
        btn2.bind(on_press = self.callback_create_table)
        btn3.bind(on_press = self.callback_delete_table)
        btn4.bind(on_press = self.callback_insert_table)
        btn5.bind(on_press = read_table)
        btn6.bind(on_press = clear_table)
        btn7.bind(on_press = order_by)
        username.bind(on_text_validate = self.callback)
        username.foreground_color = (1,0,0,1)
        screen.add_widget(username)
        screen.add_widget(self.img)
        screen.add_widget(self.ext)
        screen.add_widget(btn)
        return screen

    def callback(self, event):
        if username.text.lower() == "admin" or username.text.lower() == "volkan":
            screen.remove_widget(username)
            screen.remove_widget(self.img)
            screen.add_widget(self.sec)
            screen.remove_widget(btn)
            screen.add_widget(lbl)
            screen.add_widget(btn2)
            screen.add_widget(btn3)
            screen.add_widget(btn4)
            screen.add_widget(btn5)
            screen.add_widget(btn6)
            screen.add_widget(btn7)
            screen.add_widget(btn8)
            screen.add_widget(btn9)
            screen.add_widget(btn10)
        else:
            show_popup()

    def callback_create_table(self, event):
        create_table()

    def callback_delete_table(self, event):
        delete_table()
    
    def callback_insert_table(self, event):
        insert_to_table()

DBApp().run()