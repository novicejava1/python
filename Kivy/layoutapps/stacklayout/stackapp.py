#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MyStackLayout(StackLayout):
    pass

class MyFloatLayout(FloatLayout):
    pass


class StackApp(App):
    def build(self):
        mystack = MyStackLayout(orientation='lr-bt')
        for i in range(25):
            btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
            mystack.add_widget(btn)
        myfloat = MyFloatLayout()
        myfloat.add_widget(mystack)
        return myfloat

if __name__ == '__main__':
    StackApp().run()

