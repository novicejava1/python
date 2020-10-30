#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class MyFloatLayout(FloatLayout):
    pass

class LabelApp(App):
    def build(self):
        return MyFloatLayout()

if __name__ == '__main__':
    la = LabelApp()
    la.run()
