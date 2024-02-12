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

window.iconphoto(False, PhotoImage(file='AB-Logo.png'))
#window.iconbitmap("./AB-Icon.ico")

# Serial Connect/Disconnect Row
################################
lbl1 = Label(window, text="Port: ")
lbl1.grid(column=0, row=0, padx=5, pady=5)

combo = Combobox(window, width=13)

#combo['values']= (1, 2, 3, 4, 5, "Text")
combo['values']=ports

#combo.current(1) #set the selected item

combo.grid(column=1, row=0, padx=5, pady=5)


def clicked():
    ports = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.name)
    
    combo['values'] = ports

btn1 = Button(window, text="Refresh", command=clicked)
btn1.grid(column=2, row=0, padx=5, pady=5)


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
        
        if(c3_v1.get()==1):
            c3.invoke()  # Clear checkbox
        if(c4_v1.get()==1):
            c4.invoke()  # Clear checkbox
        if(c5_v1.get()==1):
            c5.invoke()  # Clear checkbox
        if(c6_v1.get()==1):
            c6.invoke()  # Clear checkbox
            
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
        
        if(c3_v1.get()==1):
            c3.invoke()  # Clear checkbox
        if(c4_v1.get()==1):
            c4.invoke()  # Clear checkbox
        if(c5_v1.get()==1):
            c5.invoke()  # Clear checkbox
        if(c6_v1.get()==1):
            c6.invoke()  # Clear checkbox

btn2 = Button(window, text="Connect", command=clicked2)
btn2.grid(column=3, row=0, padx=5, pady=5)


# Button 1 Update Row
######################

lbl3 = Label(window, text="B1: ")
lbl3.grid(column=0, row=1, padx=5, pady=5)

txt3 = Entry(window,width=15,show='*')
txt3.grid(column=1, row=1, padx=5, pady=5)

c3_v1=IntVar(value=0)

def show_txt3():
    if(c3_v1.get()==1):
        txt3.config(show='')
    else:
        txt3.config(show='*')
        
c3 = Checkbutton(window,text='Show',variable=c3_v1, command=show_txt3,
	onvalue=1,offvalue=0)
c3.grid(column=2,row=1) 

def clicked_b1():
    global ser
    B1_String = "b1: " + txt3.get()
    ser.write(bytearray(B1_String,'ascii')) # Write button value to serial
    txt3.delete(0, END) # Clear entry field
    txt3.config(show='*') # Reset hidden field
    if(c3_v1.get()==1):
    	c3.invoke()  # Clear checkbox

btn3 = Button(window, text="Update", command=clicked_b1)
btn3.grid(column=3, row=1, padx=5, pady=5)


# Button 2 Update Row
######################

lbl4 = Label(window, text="B2: ")
lbl4.grid(column=0, row=2, padx=5, pady=5)

txt4 = Entry(window,width=15,show='*')
txt4.grid(column=1, row=2, padx=5, pady=5)

c4_v1=IntVar(value=0)

def show_txt4():
    if(c4_v1.get()==1):
        txt4.config(show='')
    else:
        txt4.config(show='*')
        
c4 = Checkbutton(window,text='Show',variable=c4_v1, command=show_txt4,
	onvalue=1,offvalue=0)
c4.grid(column=2,row=2) 

def clicked_b2():
    global ser
    B2_String = "b2: " + txt4.get()
    ser.write(bytearray(B2_String,'ascii'))
    txt4.delete(0, END) # Clear entry field
    txt4.config(show='*') # Reset hidden field
    if(c4_v1.get()==1):
    	c4.invoke()  # Clear checkbox

btn4 = Button(window, text="Update", command=clicked_b2)
btn4.grid(column=3, row=2, padx=5, pady=5)


# Button 3 Update Row
######################

lbl5 = Label(window, text="B3: ")
lbl5.grid(column=0, row=3, padx=5, pady=5)

txt5 = Entry(window,width=15,show='*')
txt5.grid(column=1, row=3, padx=5, pady=5)

c5_v1=IntVar(value=0)

def show_txt5():
    if(c5_v1.get()==1):
        txt5.config(show='')
    else:
        txt5.config(show='*')
        
c5 = Checkbutton(window,text='Show',variable=c5_v1, command=show_txt5,
	onvalue=1,offvalue=0)
c5.grid(column=2,row=3) 

def clicked_b3():
    global ser
    B3_String = "b3: " + txt5.get()
    ser.write(bytearray(B3_String,'ascii'))
    txt5.delete(0, END) # Clear entry field
    txt5.config(show='*') # Reset hidden field
    if(c5_v1.get()==1):
    	c5.invoke()  # Clear checkbox

btn5 = Button(window, text="Update", command=clicked_b3)
btn5.grid(column=3, row=3, padx=5, pady=5)


# Button 4 Update Row
######################

lbl6 = Label(window, text="B4: ")
lbl6.grid(column=0, row=4, padx=5, pady=5)

txt6 = Entry(window,width=15,show='*')
txt6.grid(column=1, row=4, padx=5, pady=5)

c6_v1=IntVar(value=0)

def show_txt6():
    if(c6_v1.get()==1):
        txt6.config(show='')
    else:
        txt6.config(show='*')
        
c6 = Checkbutton(window,text='Show',variable=c6_v1, command=show_txt6,
	onvalue=1,offvalue=0)
c6.grid(column=2,row=4) 

def clicked_b4():
    global ser
    B4_String = "b4: " + txt6.get()
    ser.write(bytearray(B4_String,'ascii'))
    txt6.delete(0, END) # Clear entry field
    txt6.config(show='*') # Reset hidden field
    if(c6_v1.get()==1):
    	c6.invoke()  # Clear checkbox

btn6 = Button(window, text="Update", command=clicked_b4)
btn6.grid(column=3, row=4, padx=5, pady=5)

# Text Area
#######################

txt7 = Text(width=50,height=14)
txt7.grid(column=0, row=5, padx=5, pady=5, columnspan=4)

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

