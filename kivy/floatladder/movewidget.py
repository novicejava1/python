#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class RectBlock(Widget):

    def __init__(self, **kwargs):
        super(RectBlock, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        print("Touched the Widget")
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True
        return super(RectBlock, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        print("Moving the Widget")
        if touch.grab_current is self:
            if touch.x < self.width:
                self.x = touch.x
            else:
                self.x = touch.x - self.width
            return True
        return super(RectBlock, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        print("Releasing the Widget")
        if touch.grab_current is self:
            touch.ungrab(self)
            return True
        return super(RectBlock, self).on_touch_up(touch)

class MyWidget(Widget):
    ladder1 = ObjectProperty()
    ladder2 = ObjectProperty()


    def floatWidget(self, dt):
        self.ladder1.x = self.ladder1.x + 5
        self.ladder2.x = self.ladder2.x - 5

        if self.ladder1.x > self.width:
            self.ladder1.x = 0
            self.ladder1.x = self.ladder1.x + 5
        elif self.ladder2.x < self.x:
            self.ladder2.x = self.width
            self.ladder2.x = self.ladder2.x - 5
        

        

class MoveWidgetApp(App):
    def build(self):
        mw = MyWidget()
        Clock.schedule_interval(mw.floatWidget, 1.0/60.0)
        return mw

if __name__ == '__main__':
    MoveWidgetApp().run()
