from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout


class Interface(MDFloatLayout):
    def confTemp(self):
        
        print(self.ids.campo1.text)         
     

class WidgetsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style="Light"
        self.theme_cls.material_style="M2"

    

WidgetsApp().run()