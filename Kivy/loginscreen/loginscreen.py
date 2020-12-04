#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(BoxLayout):
    pass

class LoginScreenApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginScreenApp().run()
