from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
import valores


class Screen_1(MDScreen):
    my_text = StringProperty("D")
    aux = 3.5
    my_text = str(valores.mqtt_broker_configs["MSG"])
  

"""     def imprimir(self):
       
        self.my_text = "dfgdfgd"
        print(valores.mqtt_broker_configs["MSG"]) """
        
    

class Screen_2(MDScreen):
    msg = "bexandrex"
    my_text2 = StringProperty(msg)
   

class Screen_3(MDScreen):
    pass



class Interface_3(MDBoxLayout):
    def back(self):
        print("dsfsd")

class Interface(MDFloatLayout):
    pass
     

class BottomNavegationApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
      
     
 
    def build(self):
        self.theme_cls.primary_palette="Amber"
        self.theme_cls.accent_palette="Gray"
        self.theme_cls.accent_hue="900"
        self.theme_cls.material_style="M2"
        self.theme_cls.theme_style="Dark"

    

BottomNavegationApp().run()