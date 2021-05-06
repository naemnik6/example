# Создание и запуск приложения, программирование интерфейса экранов и действий на них
from kivy.app import App
from kivy.uix.button import Button # кнопка
from kivy.uix.label import Label # надпись
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout # макет (это тоже виджет!)
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from instructions import txt_instructions, txt_instructions1, txt_instructions2
from ruffier import *
from kivy.uix.popup import Popup
from kivy.core.window import Window
from coloredLayout import ColoredLayout
from coloredLayout1 import ColoredLayout1
# Здесь должен быть твой код

window_color = (.53, .53, .53, 1)
Window.clearcolor = window_color
age = 7
name = ""
p1 = 0
p2 = 0
p3 = 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_instructions)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        txt = '[i][color=#003300]'+'Введите имя:'+'[/color][/i]'
        lbl1 = Label(text=txt, halign='right', markup=True)
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text='Введите возраст:', halign='right')
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        btn_color = (1, 1, 0, .5)
        self.btn.background_color = btn_color
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global age, name
        name = self.in_name.text
        age = self.in_age.text
        age = check_int(age)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
            popup = Popup(title='Error', content=Label(text='Возраст должен быть больше 7'), size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
            popup.open()
        else:
            self.manager.current='pulse1'



class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_instructions1)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        lbl1 = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(multiline=False)
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn_back = Button(text="Назад", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn_back.on_press = self.back
        line1 = ColoredLayout(lcolor=(0, 0.5, 0.01, 1))
        # line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_result)
        line2 = ColoredLayout(lcolor=(0.5, 0.5, 0.5, 1))
        line2.add_widget(self.btn_back)
        line2.add_widget(self.btn)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        self.add_widget(outer)

    def next(self):
        global p1
        p1 = self.in_result.text
        p1 = check_int(p1)
        if p1 == False or p1 <= 0:
            p1 = 0
            self.in_result.text = str(p1)
        else:
            self.manager.current='pulse2'

    def back(self):
        self.manager.current = self.manager.previous()   

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_instructions2)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        lbl1 = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(multiline=False)
        self.in_result1 = TextInput(multiline=False)
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        # line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1 = ColoredLayout(lcolor=(0.44, 0.44, 0.44, 1))
        line1.add_widget(lbl1)
        line1.add_widget(self.in_result)
        line1.add_widget(self.in_result1)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global p2, p3
        p2 = self.in_result.text
        p2 = check_int(p1)
        p3 = self.in_result1.text
        p3 = check_int(p3)
        if p2 == False or p2 <= 0:
            p2 = 0
            self.in_result.text = str(p2)
        elif p3 == False or p3 <= 0:
            p3 = 0
            self.in_result1 = p3
        else:
            self.manager.current='result'

class Check(Screen):
    pass

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global p1, p2, p3
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        result = test(p1, p2, p3, age)
        info = Label(text='Результат:' + str(result), halign='right')
        self.outer.add_widget(info)
        self.add_widget(self.outer)


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Check(name='check'))
        sm.add_widget(Result(name='result'))
        return sm

app = HeartCheck()
app.run()
