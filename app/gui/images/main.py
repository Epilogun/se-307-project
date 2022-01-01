from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image

from user import username
from button import btn, btn2, btn3, btn4, btn5
from label import lbl
from popup import show_popup
from scr import screen
from dbsys import create_table, delete_table, insert_to_table, read_table

Window.clearcolor = (0.1, 0.6, 0.2, 0.6)

class DBApp(App):
    def build(self):
        self.img = Image(source ='user.png')
        self.img.size_hint_x = 0.1
        self.img.size_hint_y = 0.1
        self.img.pos = (183, 314)
        btn.bind(on_press = self.callback)
        btn2.bind(on_press = self.callback_create_table)
        btn3.bind(on_press = self.callback_delete_table)
        btn4.bind(on_press = self.callback_insert_table)
        btn5.bind(on_press = read_table)
        username.bind(on_text_validate = self.callback)
        username.foreground_color = (1,0,0,1)
        screen.add_widget(username)
        screen.add_widget(self.img)
        screen.add_widget(btn)
        return screen 

    def callback(self, event):
        if username.text.lower() == "admin" or username.text.lower() == "volkan":
            screen.remove_widget(username)
            screen.remove_widget(self.img)
            screen.remove_widget(btn)
            screen.add_widget(lbl)
            screen.add_widget(btn2)
            screen.add_widget(btn3)
            screen.add_widget(btn4)
            screen.add_widget(btn5)
        else:
            show_popup()

    def callback_create_table(self, event):
        create_table()

    def callback_delete_table(self, event):
        delete_table()
    
    def callback_insert_table(self, event):
        insert_to_table()

DBApp().run()