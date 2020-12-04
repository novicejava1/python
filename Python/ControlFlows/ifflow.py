#!/usr/bin/env python

msg1 = input("Enter the message : ")
print("The message is : ", msg1)

if len(msg1) > 0 and len(msg1) <= 5:
    print("Message has been received and is small")
elif len(msg1) > 5:
    print("Message is huge")
else:
    print("Message not received")
