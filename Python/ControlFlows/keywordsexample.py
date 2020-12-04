#!/usr/bin/env python

def simplemessage(temperature, food="Pizza", location="at home", members="friends"):
    print("We are currently eating ", food, end=" ")
    print(location, end=" ")
    print("with ", members, end=" ")
    print("in a house with temperature ", temperature)

simplemessage("53'C")
simplemessage("25'C", location="at beach")
simplemessage("77'C", members="Army", location="at Army Cantonment", food="Chole Bathore")
simplemessage(members="Army", temperature="22'C")
# simplemessage(members="Army", "22'C")             # This will fail as positional argument follows keyword argument



