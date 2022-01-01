from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

class P(FloatLayout):
    pass

def show_popup():
    show = P() 
    popupWindow = Popup(title = "Failed to log in.\nThe username does not exist.", 
    content = show, size_hint = (None,None), size = (200, 100)) 
    popupWindow.open()

def show_popup2():
    show = P() 
    popupWindow = Popup(title = "Table is created.", 
    content = show, size_hint = (None,None), size = (200, 100)) 
    popupWindow.open()

def show_popup3():
    show = P() 
    popupWindow = Popup(title = "Table is deleted.", 
    content = show, size_hint = (None,None), size = (200, 100)) 
    popupWindow.open()

def show_popup4():
    show = P() 
    popupWindow = Popup(title = "There is no table to delete.", 
    content = show, size_hint = (None,None), size = (200, 100)) 
    popupWindow.open()

def show_popup5():
    show = P() 
    popupWindow = Popup(title = "There is no table to read.", 
    content = show, size_hint = (None,None), size = (200, 100)) 
    popupWindow.open()