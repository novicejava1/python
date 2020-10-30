#!/usr/bin/env python

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
