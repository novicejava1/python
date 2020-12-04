#!/usr/bin/env python

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox

class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    FloatLayoutApp().run()

