from kivy.properties import DictProperty 
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout

class Interface_2(MDFloatLayout):
    data = DictProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data={"Copy":["content-copy", "on_press", lambda x: self.copying()], "Printer": "printer", "Share": "share-variant"}    
    def copying(self):
        print("copying")
class WidgetsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.material_style="M2"

WidgetsApp().run()