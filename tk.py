from Tkinter import *
import sys
master = Tk() 
Label(master, text='cur').grid(row=0) 
Label(master, text='vol').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master)
sys.argv = [sys.argv[0],e1, e2]
print sys.argv[1]
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
 
mainloop() 
