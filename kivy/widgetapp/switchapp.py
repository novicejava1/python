#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.switch import Switch

class MySwitch(Switch):
    pass

class SwitchApp(App):
    def build(self):
        return MySwitch()

if __name__ == '__main__':
    sa = SwitchApp()
    sa.run()

