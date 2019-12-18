import Tkinter
from BasicOutline import runBO
master = Tkinter.Tk()
guessm=Tkinter.StringVar()
vm = Tkinter.StringVar()
global string
def hi():
    print 'hi'    
b = Tkinter.Button(master, text="Game 1", command=runBO)
b.grid(row=1, column=0)
b2 = Tkinter.Button(master, text="Game 2", command=hi)
b2.grid(row=2, column=0)
b3 = Tkinter.Button(master, text="Game 3", command=hi)
b3.grid(row=3, column=0)
yeep = Tkinter.Label(master, textvariable=vm)
yeep.grid(row=4, column=0)
vm.set('hi landon')
labelm= Tkinter.Entry(master,textvariable=guessm)
labelm.grid(row=5, column=0)
master.mainloop()
master.quit()