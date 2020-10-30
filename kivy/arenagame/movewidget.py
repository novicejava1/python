#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget

class MoveWidget(Widget):
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("Child Widget touched")
        else:
            print("Parent Widget touched")

    def on_touch_move(self, touch):
        if touch.x < self.width:
            self.x = touch.x
        else:
            self.x = touch.x - self.width


class MyWidget(Widget):
    pass

class MoveWidgetApp(App):

    def build(self):
        my = MyWidget()
        return my

if __name__ == '__main__':
    MoveWidgetApp().run()
