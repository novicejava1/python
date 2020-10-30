#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.slider import Slider

class MySlider(Slider):
    pass

class SliderApp(App):
    def build(self):
        return MySlider()

if __name__ == '__main__':
    sa = SliderApp()
    sa.run()
