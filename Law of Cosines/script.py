import math
import tkinter
# -*- coding: utf-8 -*-
__author__ = 'ddsnowboard'
A = 0
B = 0
C = 0
c = 0
root = tkinter.Tk()


def assign():
    global A,B,C,c,root
    A = box1.get()
    B = box2.get()
    C = box3.get()
    c = box4.get()
    print(box1.get())
    # Get this line to work. It should destroy window or at least let code keep going.
    # And find out a way to get the outputs from the text boxes into floats.
    root.destroy

quest = None
warn = tkinter.Label(root,text="Give c in degrees, if applicable")

first = tkinter.Frame(root)
text1 = tkinter.Label(first, text="A=")
box1 = tkinter.Spinbox(first)

second = tkinter.Frame(root)
text2 = tkinter.Label(second, text="B=")
box2 = tkinter.Spinbox(second)

third = tkinter.Frame(root)
text3 = tkinter.Label(third, text="C=")
box3 = tkinter.Spinbox(third)

fourth = tkinter.Frame(root)
text4 = tkinter.Label(fourth, text="c=")
box4 = tkinter.Spinbox(fourth)

text1.pack()
box1.pack()
first.pack()

text2.pack()
box2.pack()
second.pack()

text3.pack()
box3.pack()
third.pack()

text4.pack()
box4.pack()
fourth.pack()

button = tkinter.Button(root,command=assign(), text="Go!")
button.pack()
root.mainloop()


def quad(g, e, f):
    return (-e+math.sqrt(e**2-4*g*f))/(2*g)

if A == '':
    quest = "A"
    B = float(B)
    C = float(C)
    c = float(c)
    A = None
if B == '':
    quest = "B"
    A = float(A)
    C = float(C)
    c = float(c)
    B = None
if C == '':
    quest  = "C"
    A = float(A)
    B = float(B)
    c = float(c)
    C = None
if c == '':
    quest = "c"
    A = float(A)
    B = float(B)
    C = float(C)
    c = None
# C^2 = A^2+B^2-2abcosc
if quest == "C":
    print(math.sqrt((A**2 + B**2)-(2*A*B*math.cos(math.radians(c)))))
elif quest == "A":
    print(quad(1, -1*(2*B*math.cos(math.radians(c))),B**2-C**2))
elif quest == "B":
    print(quad(1, -1*(2*A*math.cos(math.radians(c))),A**2-C**2))
elif quest == "c":
    deg = math.degrees(math.acos((C**2-A**2-B**2)/(-1*2*A*B)))
    minutes = (deg-int(deg))*60
    sec = (minutes-int(minutes))*60
    print(deg)
    print("or")
    print(str(int(deg)) + "°" + str(int(minutes)) + "'" + str(int(sec)) + '"')
print("Press enter to quit")
input("...")