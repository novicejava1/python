#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class MyGridLayout(GridLayout):
    cols=3
    rows=3

class ButtonApp(App):
    def build(self):
        #gl = MyGridLayout()
        #gl.add_widget(Button(text="Python"))
        #gl.add_widget(Button(text="Django"))
        #gl.add_widget(Button(text="Python"))
        #gl.add_widget(Button(text="Django"))
        #gl.add_widget(Button(text="Python"))
        #gl.add_widget(Button(text="Django"))
        #return gl

        gl = MyGridLayout()
        value = gl.cols * gl.rows
        for i in range(value):
            if i % 2 == 0:
                gl.add_widget(Image(source='appicon.png'))
            else:
                gl.add_widget(Image(source='appicon.png'))
        return gl

if __name__ == '__main__':
    ba = ButtonApp()
    ba.run()
