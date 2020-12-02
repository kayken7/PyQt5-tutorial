
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import time

class TimeShow(Label):
    def update(self, *args):
        self.text = time.asctime()


fontk = 'font/Cafe24Dangdanghae.ttf'

class KivyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(KivyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.clock = TimeShow()
        self.clock.font_size = 50
        Clock.schedule_interval(self.clock.update, 1)
        self.add_widget(self.clock)

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='제목: ', font_name=fontk, font_size=30))
        self.title = TextInput(multiline=False, font_name=fontk, font_size=30)
        self.inside.add_widget(self.title)

        self.inside.add_widget(Label(text='내용: ', font_name=fontk, font_size=30))
        self.content = TextInput(multiline=True, font_name=fontk, font_size=30)
        self.inside.add_widget(self.content)

        self.inside.add_widget(Label(text='글쓴이: ', font_name=fontk, font_size=30))
        self.writer = TextInput(multiline=False, font_name=fontk, font_size=30)
        self.inside.add_widget(self.writer)

        self.add_widget(self.inside)

        self.submit = Button(text='제출하기', font_name=fontk, font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        title = self.title.text
        content = self.content.text
        writer = self.writer.text
        print('title: ', title, ' content: ', content, ' writer: ', writer)

        self.title.text = ''
        self.content.text =''
        self.writer.text = ''

class KivyApp(App):
    def build(self):
        return KivyGrid()

if __name__ == '__main__':
    KivyApp().run()
