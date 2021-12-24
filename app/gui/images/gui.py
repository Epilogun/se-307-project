from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image

from user import username
from button import btn
from label import lbl
from popup import show_popup
from scr import screen

Window.clearcolor = (0.1, 0.6, 0.2, 0.6)

class DBApp(App):
    def build(self):
        self.img = Image(source ='user.png')
        self.img.size_hint_x = 0.1
        self.img.size_hint_y = 0.1
        self.img.pos = (183, 314)
        btn.bind(on_press = self.callback)
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
        else:
            show_popup()
        
        

DBApp().run()