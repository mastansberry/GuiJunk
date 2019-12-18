#from Tkinter import *
def runBO():
    import Tkinter

    from hangman import hang
    import hangman
    
    
    master = Tkinter.Tk()
    
    global string
    global gg
    global guess
    global v
    global vv
    
    
    guess=Tkinter.StringVar()
    v = Tkinter.StringVar()
    vv = Tkinter.StringVar()
    
    #v.set(yep.hangingGui.vv)    
    gg=v.get()
    
                            
    def update():
        hang(guess.get(),'earth boi')
        #v.set(hangman.BasicOutline.vv)
        v.set(hangman.string)
        
        
        
    w =Tkinter.Canvas(master, width=200, height=100)
    w.grid(row=0,column=0)
    
    b = Tkinter.Button(master, text="OK", command=update)
    b.grid(row=1, column=0)
    
    
    yeep = Tkinter.Label(master, textvariable=v)
    yeep.grid(row=2, column=0)
    
    lab= Tkinter.Entry(master,textvariable=guess)
    lab.grid(row=3, column=0)
    
    
    
    
    master.mainloop()
    master.quit()