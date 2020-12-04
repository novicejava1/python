#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)


    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        #self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))
        self.ball.velocity = vel
    
    def update(self, dt):
        self.ball.move()
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce left and right
        #if (self.ball.x < 0) or (self.ball.right > self.width):
        #    self.ball.velocity_x *= -1

        if self.ball.x < self.x:
            self.player2.score += 1
            self.server_ball(vel=(4,0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

class PongBall(Widget):

    # velocity of ball on x and y axis
    velocity_x = NumericProperty()
    velocity_y = NumericProperty()

    # Reference list property
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # move the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    PongApp().run()

