#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Rectangle, Color

class MyButton(Button):
    def __init__(self, **kwargs):

        super(MyButton, self).__init__(**kwargs)

        #with self.canvas:
        #    Color(1, 1, 0, 1)
        #    self.rect = Rectangle(size=self.size)

class MyStackLayout(StackLayout):
    pass

class StackRock(App):
    def build(self):
        mystack = MyStackLayout(orientation='lr-bt')
        for i in range(25):
            mystone = MyButton(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
            mystack.add_widget(mystone)
        
        return mystack

if __name__ == '__main__':
    StackRock().run()

