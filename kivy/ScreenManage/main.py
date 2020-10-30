#!/usr/bin/env python

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class MyScreen(ScreenManager):
    pass

class ScreenApp(App):
    def build(self):
        self.sm = MyScreen()
        return self.sm

Window.softinput_mode = "below_target"

if __name__ == '__main__':
    ScreenApp().run()

