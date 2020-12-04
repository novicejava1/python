#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Rectangle, Color

class MyWidget(Widget):
    def __init__(self, **kwargs):

        super(MyWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 0, 1)
            self.rect = Rectangle(size=(50, 50))

class MyStackLayout(StackLayout):
    pass

class StackRock(App):
    def build(self):
        mystack = MyStackLayout(orientation='lr-bt')
        #for i in range(25):
        #    myrock = MyWidget(pos=(i + 5, 0))
        #    mystack.add_widget(myrock)
        
        myrock1 = MyWidget()
        #myrock1.rect.pos = (100, 100)
        mystack.add_widget(myrock1)

        myrock2 = MyWidget()
        #myrock2.rect.pos = (100, 200)
        mystack.add_widget(myrock2)

        myrock3 = MyWidget()
        #myrock3.rect.pos = (100, 300)
        mystack.add_widget(myrock3)
        return mystack

if __name__ == '__main__':
    StackRock().run()

