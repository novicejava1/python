#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition

class Manager(ScreenManager):
    pass

class ScreenApp(App):
    def build(self):
        return Manager(transition=FadeTransition())

if __name__ == '__main__':
    ScreenApp().run()
