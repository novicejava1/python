#!/usr/bin/env python

from collections import deque

queue = deque(["The man who knew infinity", "Inception", "The next three days", "Pursuit of Happyness", "Interstellar", "The independence day"])
print(queue)
print(type(queue))

queue.append("Titanic")
queue.append("The day after tomorrow")
print(queue)

queue.popleft()
print(queue)

