#from Tkinter import *
import Tkinter

#from yep import chip
import yep

from hangman import hang
import hangman


master = Tkinter.Tk()

w =Tkinter.Canvas(master, width=200, height=100)
w.grid(row=0,column=0)

def callback():
    print "click!"
    gg="new version222"
    v.set(gg)
    #print guess.get()
    
def update():
    #hangtheletters()
    #print guess.get()
    hang(guess.get(),'earth boi')
    #hangtheletters()
    
    v.set(hangman.hangingGui.vv)
    
    

b = Tkinter.Button(master, text="OK", command=update)
b.grid(row=1, column=0)

global guess



guess=Tkinter.StringVar()

lab= Tkinter.Entry(master,textvariable=guess).grid(row=3, column=0)
global gg
global v
global vset
global vv
v = Tkinter.StringVar()
vv = Tkinter.StringVar()
yeep = Tkinter.Label(master, textvariable=v)
yeep.grid(row=2, column=0)
#vv="test"
v.set(yep.hangingGui.vv)
gg=v.get()
vset= v.set('')

master.mainloop()