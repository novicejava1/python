#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout):
    pass

class DrawingApp(App):
    def build(self):
        return DrawingSpace()

if __name__ == '__main__':
    da = DrawingApp()
    da.run()



