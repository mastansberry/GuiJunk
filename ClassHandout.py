#Import random for my SimpleProgram
import random

#Step 1of 3 to Tkinter window creation
import Tkinter

#Step 2 of 3 to Tkinter window creation
master = Tkinter.Tk()

#Simple program where I get the users response
#Compare then print out the result to a label
#UserEntry.get() will always return a string
#If you want an integer then do int(UserEntry.get)
def SimpleProgram():
    #I am just making a dice roll game
    roll=random.randint(1,6)
    if int(UserEntry.get()) == roll:
        LabelVariable.set("Correct Guess")
    else:
        LabelVariable.set("Wrong Guess, my roll was " + str(roll))
   
#Creating my button        
btn = Tkinter.Button(master, text="Click me", command=SimpleProgram)
btn.grid(row=3, column=0)

#Creating my directions label  
#I added the \n because it means new line.
IntroLabel = Tkinter.Label(master, text="Welcome,\n Guess the dice roll")
IntroLabel.grid(row=1, column=0)

#Creating my entry to get the users response 
#Create StringVar() because it is a changing variable
EntryVariable=Tkinter.StringVar() 
UserEntry= Tkinter.Entry(master,textvariable=EntryVariable)
UserEntry.grid(row=2, column=0)

#Creating my resulting label 
#Create StringVar() because it is a changing variable
LabelVariable=Tkinter.StringVar()
ResultLabel= Tkinter.Label(master, textvariable=LabelVariable)
ResultLabel.grid(row=4, column=0)

#Step 3 of 3 to Tkinter window creation
master.mainloop()