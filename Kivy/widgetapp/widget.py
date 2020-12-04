#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget(Widget):
    pass

class WidgetApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    la = WidgetApp()
    la.run()
