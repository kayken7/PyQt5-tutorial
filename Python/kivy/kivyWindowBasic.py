from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        return Label(text='Hello from Kivy')


if __name__ == '__main__':
    app = MainApp()
    app.run()
