#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget

class MyApp(Widget):
    pass

class simple1App(App):
    def build(self):
        return MyApp()

if __name__ == "__main__":
    simple1App().run()
