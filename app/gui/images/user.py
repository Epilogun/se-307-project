from kivy.uix.textinput import TextInput

username = TextInput(hint_text = "Enter Username",
                            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                            background_color =(1, 1, 1, 1),
                            size_hint = (0.5, 0.06),
                            multiline = False)