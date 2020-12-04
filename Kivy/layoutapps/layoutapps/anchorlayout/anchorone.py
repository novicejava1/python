#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class MyAnchorLayout(AnchorLayout):
    pass

class AnchorOneApp(App):
    def build(self):
        return MyAnchorLayout()

if __name__ == '__main__':
    aa = AnchorOneApp()
    aa.run()
