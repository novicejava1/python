#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGridLayout(GridLayout):

    cols=3
    rows=3

class MyButton(Button):

    text='hello'
    background_normal=''

    def callback(self, instance):
        print("Button is pressed!!!")


class ButtonApp(App):

    def build(self):

        gl = MyGridLayout()
        value = gl.cols * gl.rows

        for i in range(value):
            if i % 2 == 0:
                btn = MyButton(background_color=[1, 1, 0, 1])
                btn.bind(on_press=btn.callback)
                gl.add_widget(btn)
            else:
                btn = MyButton(background_color=[1, 1, 1, 1])
                btn.bind(on_press=btn.callback)
                gl.add_widget(btn)
        return gl

if __name__ == '__main__':
    ba = ButtonApp()
    ba.run()
