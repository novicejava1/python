#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.core.audio import SoundLoader

class MyStackLayout(StackLayout):
    def playsound(self):
        sound = SoundLoader.load('click.wav')
        sound.play()


class StackApp(App):

    def build(self):
        return MyStackLayout()

if __name__ == '__main__':
    StackApp().run()
