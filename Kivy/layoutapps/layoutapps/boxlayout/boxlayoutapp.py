#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    pass

class BoxLayoutApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    BoxLayoutApp().run()
