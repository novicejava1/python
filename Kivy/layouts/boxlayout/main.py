#!/usr/bin/env python

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    pass

class LayoutsApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == "__main__":
    LayoutsApp().run()
