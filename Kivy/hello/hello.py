#!/usr/bin/env python

import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.button import Label

class helloApp(App):
    def build(self):
        return Label()

if __name__ ==  "__main__":
    helloApp().run()

