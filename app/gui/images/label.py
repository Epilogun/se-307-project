from kivy.uix.label import Label
from scr import screen


lbl = Label(text = "[b]Graduate Thesis System Database Manager[/b]", 
            font_size ='20sp',
            color =[1, 1, 1, 1],
            pos = (0, 280),
            markup = True)

def infos(myText):
    lbl2 = Label(text = myText, 
                    font_size ='20sp',
                    color =[1, 0, 1, 1],
                    pos = (-105, 100))
    list_info(lbl2)

def list_info(x):
    screen.add_widget(x)