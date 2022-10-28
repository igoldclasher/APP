from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class ScreenOne(Screen):

    def __init__ (self,**kwargs):
        super (ScreenOne, self).__init__(**kwargs)
        my_box1 = FloatLayout()
        my_box1.add_widget(Label(text="Главное меню", color = (1,0,1,1), font_size='16dp', size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'top': 1}))
        my_box1.add_widget(Label(text="Выбери режим работы", font_size='24dp'))
        skypka = Button(text="Скупать", size_hint = (0.5, 0.1))
        prodaja = Button(text="Продавать", size_hint = (0.5, 0.1), pos_hint={'center_x': 0.75, 'v': 1})
        skypka.bind(on_press=self.skypka)
        prodaja.bind(on_press=self.prodaja)
        my_box1.add_widget(skypka)
        my_box1.add_widget(prodaja)
        self.add_widget(my_box1)

    def skypka(self,*args):
        self.manager.current = 'skypka'

    def prodaja(self,*args):
        self.manager.current = 'prodaja'

class режимскупки(Screen):

    def __init__(self,**kwargs):
        super (режимскупки,self).__init__(**kwargs)
        my_box1 = FloatLayout()
        skypka = Button(text="Главное меню", size_hint = (1, 0.1))
        skypka.bind(on_press=self.changer)
        my_box1.add_widget(Label(text="skypka", color = (1,0,1,1), font_size='16dp', size_hint = (1, 0.1), pos_hint = {'center_x': 0.5, 'top': 1}))
        my_box1.add_widget(Label(text="Режим скупки в разработке",font_size='24dp'))
        my_box1.add_widget(skypka)
        self.add_widget(my_box1)

    def changer(self,*args):
        self.manager.current = 'menu'


class режимпродажи(Screen):

    def __init__(self,**kwargs):
        super (режимпродажи,self).__init__(**kwargs)

        my_box1 = FloatLayout()
        my_box1.add_widget(
        Label(text="prodaja", color = (1,0,1,1), font_size='16dp', size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'top': 1}))
        my_label1 = Label(text="Режим продажи в разработке",font_size='24dp')
        skypka = Button(text="Главное меню", size_hint = (1, 0.1))
        skypka.bind(on_press=self.changer)
        my_box1.add_widget(my_label1)
        my_box1.add_widget(skypka)
        self.add_widget(my_box1)

    def changer(self,*args):
        self.manager.current = 'menu'


class TestApp(App):

        def build(self):
            my_screenmanager = ScreenManager()
            menu = ScreenOne(name='menu')
            skypka = режимскупки(name='skypka')
            prodaja = режимпродажи(name='prodaja')
            my_screenmanager.add_widget(menu)
            my_screenmanager.add_widget(skypka)
            my_screenmanager.add_widget(prodaja)
            return my_screenmanager

if __name__ == '__main__':
    TestApp().run()