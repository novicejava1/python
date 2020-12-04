#!/usr/bin/env python

import kivy
from kivy.app import App
from kivy.uix.button import Label

class menuApp(App):
    def build(self):
        return Label(text="This is menu label")

if __name__ == "__main__":
    menuApp().run()
