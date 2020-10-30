#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class InterfaceManager(BoxLayout):

    def __init__(self, **kwargs):
        super(InterfaceManager, self).__init__(**kwargs)

        self.first = Button(text='first')
        self.first.bind(on_press = self.show_second)

        self.second = Button(text='second')
        self.second.bind(on_press = self.show_final)

        self.third = Button(text='third')

        self.final = Label(text='Hello World')
        self.add_widget(self.first)
        self.add_widget(self.third)

    def show_second(self, button):
        self.clear_widgets()
        self.add_widget(self.second)

    def show_final(self, button):
        self.clear_widgets()
        self.add_widget(self.final)

class MyApp(App):
    
    def build(self):
        return InterfaceManager(orientation = 'vertical')

if __name__ == '__main__':
    MyApp().run()


