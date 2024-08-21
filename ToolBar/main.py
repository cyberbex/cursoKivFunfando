from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


Window.size=(480,600)

class MI(MDBoxLayout):
    pass
class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Ambar"
        self.theme_cls.theme_style="Dark"
        return 0
    
MyApp().run()

