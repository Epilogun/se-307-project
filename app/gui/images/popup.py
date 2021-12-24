from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

class P(FloatLayout):
    pass

def show_popup():
    show = P() 
    popupWindow = Popup(title="Failed to log in.\nThe username does not exist.", 
    content = show, size_hint = (None,None), size = (200, 100)) 
    popupWindow.open()