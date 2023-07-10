#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *
import serial
import sys
import os
import serial.tools.list_ports
import time



ports = []
for port in serial.tools.list_ports.comports():
    ports.append(port.name)
#print(ports)

ser = serial.Serial()

window = Tk()

window.title("Admin Buddy")

window.geometry('425x450')

window.iconphoto(False, PhotoImage(file='AB.png'))


# Serial Connect/Disconnect Row
################################
combo = Combobox(window)

#combo['values']= (1, 2, 3, 4, 5, "Text")
combo['values']=ports

#combo.current(1) #set the selected item

combo.grid(column=0, row=0, padx=5, pady=5)


def clicked():
    ports = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.name)
    
    combo['values'] = ports

btn1 = Button(window, text="Refresh", command=clicked)
btn1.grid(column=1, row=0, padx=5, pady=5)


def clicked2():
    global ser
    port = combo.get()
    #print("value: " + port) 
    if(btn2['text'] == "Connect"):
        if(port[:3] == "COM"):
            ser = serial.Serial(port=port, baudrate=9600)
        else:
            ser = serial.Serial(port="/dev/" + port, baudrate=9600)
        btn2['text'] = "Disconnect"
        lbl3.configure(text="B1: ")
        txt3.delete(0, END)
        lbl4.configure(text="B2: ")
        txt4.delete(0, END)
        lbl5.configure(text="B3: ")
        txt5.delete(0, END)
        lbl6.configure(text="B4: ")
        txt6.delete(0, END)
        txt7.delete("1.0","end")
        

         
    else:
        ser.close()
        btn2['text'] = "Connect"
        lbl3.configure(text="B1: ")
        txt3.delete(0, END)
        lbl4.configure(text="B2: ")
        txt4.delete(0, END)
        lbl5.configure(text="B3: ")
        txt5.delete(0, END)
        lbl6.configure(text="B4: ")
        txt6.delete(0, END)
        txt7.delete("1.0","end")
        txt7.insert(END,"Port Disconnected\n")

btn2 = Button(window, text="Connect", command=clicked2)
btn2.grid(column=2, row=0, padx=5, pady=5)


# Button 1 Update Row
######################

lbl3 = Label(window, text="B1: ")
lbl3.grid(column=0, row=1, padx=5, pady=5)

txt3 = Entry(window,width=15)
txt3.grid(column=1, row=1, padx=5, pady=5)

def clicked_b1():
    global ser
    res3 = "B1: " + txt3.get()
    lbl3.configure(text= res3)
    B1_String = "b1: " + txt3.get()
    ser.write(bytearray(B1_String,'ascii'))

btn3 = Button(window, text="Update", command=clicked_b1)
btn3.grid(column=2, row=1, padx=5, pady=5)


# Button 2 Update Row
######################

lbl4 = Label(window, text="B2: ")
lbl4.grid(column=0, row=2, padx=5, pady=5)

txt4 = Entry(window,width=15)
txt4.grid(column=1, row=2, padx=5, pady=5)

def clicked_b2():
    res4 = "B2: " + txt4.get()
    lbl4.configure(text= res4)
    B2_String = "b2: " + txt4.get()
    ser.write(bytearray(B2_String,'ascii'))

btn4 = Button(window, text="Update", command=clicked_b2)
btn4.grid(column=2, row=2, padx=5, pady=5)


# Button 3 Update Row
######################

lbl5 = Label(window, text="B3: ")
lbl5.grid(column=0, row=3, padx=5, pady=5)

txt5 = Entry(window,width=15)
txt5.grid(column=1, row=3, padx=5, pady=5)

def clicked_b3():
    res5 = "B3: " + txt5.get()
    lbl5.configure(text= res5)
    B3_String = "b3: " + txt5.get()
    ser.write(bytearray(B3_String,'ascii'))

btn5 = Button(window, text="Update", command=clicked_b3)
btn5.grid(column=2, row=3, padx=5, pady=5)


# Button 4 Update Row
######################

lbl6 = Label(window, text="B4: ")
lbl6.grid(column=0, row=4, padx=5, pady=5)

txt6 = Entry(window,width=15)
txt6.grid(column=1, row=4, padx=5, pady=5)

def clicked_b4():
    res6 = "B4: " + txt6.get()
    lbl6.configure(text= res6)
    B4_String = "b4: " + txt6.get()
    ser.write(bytearray(B4_String,'ascii'))

btn6 = Button(window, text="Update", command=clicked_b4)
btn6.grid(column=2, row=4, padx=5, pady=5)

# Text Area
#######################

txt7 = Text(width=50,height=14)
txt7.grid(column=0, row=5, padx=5, pady=5, columnspan=3)

def task():
    global ser
    
    if(ser.isOpen() == True):
        if ser.inWaiting() > 5:
            txt7.delete("1.0","end")
        while ser.inWaiting() > 1: 
            msg = ser.readline().rstrip()
            msg=msg.decode('utf-8')
            if len(msg) > 0:
                #print(msg)
                txt7.insert(END,msg + "\n")
                
    #print("hello")
    #txt7.insert(END,"hello\n")
    
    window.after(250, task)  # reschedule event in .25 seconds

window.after(250, task)

window.mainloop()

