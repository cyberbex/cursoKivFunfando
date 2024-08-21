from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock

class Demo1(MDScreen):
    pass

class Demo2(MDScreen):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("ui.kv")
        Clock.schedule_interval(self.update, 1)
        sm = ScreenManager()
        sm.add_widget(Demo1(name="demo1"))
        sm.add_widget(Demo2(name="demo2"))
        return sm
    

    def update(self, *args):
        pass
        

Main().run()    
