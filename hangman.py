#from hangingGui import *
#import hangingGui
#global guess
import BasicOutline


#global vv
global string


def hang(guess,secret):
    flag= False
    global string
    string= ""
    for s in secret:
        for g in guess:
            if s==g or s == ' ':
                flag =True
        if flag == True:
            string += s
            flag = False
        else:
            string += "_ "
            flag = False
    
    print string
    
    #previous methods not used in this one
    #hangingGui.vv=string
    #BasicOutline.vv=string
