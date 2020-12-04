#! /usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
  def build(self):
    return Label(text='Hello World!!')

if __name__ == '__main__':
  MyApp().run()
