#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader

class MyWidget(Widget):
    def playsound(self):
        sound = SoundLoader.load('click.wav')
        sound.play()

class SoundTestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    SoundTestApp().run()
