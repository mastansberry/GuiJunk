import Tkinter
master = Tkinter.Tk()
guess=Tkinter.StringVar()
v = Tkinter.StringVar()
def hi():
    print 'hi'    
b = Tkinter.Button(master, text="OK", command=hi)
b.grid(row=1, column=0)
yeep = Tkinter.Label(master, textvariable=v)
yeep.grid(row=2, column=0)
v.set('hi landon')
lab= Tkinter.Entry(master,textvariable=guess)
lab.grid(row=3, column=0)
master.mainloop()
master.quit()