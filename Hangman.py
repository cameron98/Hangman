"""
Create a GUI hangman game for STEM day/school
Begin with window to type in word, hidden with *.
Must display list of letters, hangman screen and _ for letters.

Created by Cameron
cameron.finnie@yahoo.co.uk
"""
import tkinter as tk
import turtle, time
from sys import exit

def EXIT():
    window.destroy()
    exit()

def restart():
    t.reset()
    window.wm_state('iconic')
    Word()


#code to find monitor resolutions
res = tk.Tk()
Sheight = res.winfo_screenheight()
Swidth = res.winfo_screenwidth()
res.destroy()
res.mainloop()

def test(guess):
    print(guess)

#function to check if guess is in word
def check(guess):
    global wordList, correct, attempt
    occurences = word.count(guess)
    if occurences > 0:
        while occurences > 0:
            location = word.index(guess)
            word[location] = "!"
            wordList[location] = guess
            occurences -= 1
            correct += 1
        wordDisplay.config(text=wordList)
        if correct == total:
            wordList = ("Correct! The word was " + final)
            wordDisplay.config(text=wordList)
    else:
        attempt += 1
        draw(attempt)
    #attatch new function to this to trigger drawing
    
def draw(step):
    if step ==1:
        t.penup()
        t.goto(-300, -200)
        t.pendown()
        t.forward(600)
        t.penup()
        t.goto(-100,-200)
    elif step ==2:
        t.left(90)
        t.pendown()
        t.forward(400)
    elif step ==3:
        t.right(90)
        t.forward(250)
    elif step ==4:
        t.penup()
        t.goto(-100, 160)
        t.left(45)
        t.pendown()
        t.forward(56.56854249)
    elif step ==5:
        t.penup()
        t.goto(150,200)
        t.setheading(270)
        t.pendown()
        t.forward(40)
    elif step ==6:
        angle = 0
        t.seth(0)
        while angle < 360:
            t.right(1)
            t.forward(0.3)
            angle +=1
    elif step == 7:
        t.penup()
        t.goto(150,125)
        t.pendown()
        t.seth(270)
        t.forward(80)
    elif step ==8:
        t.penup()
        t.goto(120, 100)
        t.seth(0)
        t.pendown()
        t.forward(60)
    elif step ==9:
        t.penup()
        t.goto(150,45)
        t.right(45)
        t.pendown()
        t.forward(45)
    elif step ==10:
        t.penup()
        t.goto(150, 45)
        t.right(90)
        t.pendown()
        t.forward(45)
        wordDisplay.config(text="OUT OF LIVES! The word was " + final)
        
        
        
    
    
colour = "#538bad"



def START():
    #note insert refresh options for window in START to allow replayable program
    global word, ready, wordDisplay, wordList, total, correct, attempt, final
    word = box.get()
    final = word
    final.upper()
    word = word.upper()
    word = list(word)
    wordList = []
    ready = True
    entry.destroy()
    for n in range(len(word)):
        wordList.append("_")
    ', '.join(wordList)
    wordDisplay.config(text=wordList)
    total = len(word)
    correct = 0
    t.penup()
    t.goto(-300,-200)
    attempt = 0
    window.deiconify()
        
    
#function for button that takes word to enter
def Word():
    global box, entry
    entry = tk.Toplevel()
    
    label = tk.Label(entry, text="Enter word:")
    label.pack()
    box = tk.Entry(entry, show="*")
    box.pack()
    enter = tk.Button(entry, text="START", command=START)
    enter.pack()
    entry.mainloop
    

ready = False



window = tk.Tk()
window.title("Hangman")
window.attributes('-fullscreen', 'True')
#To add a background colour 
window.configure(background=colour)
#To set the window icon window.wm_iconbitmap('icon.ico')

#To add a background colour bg= for forgeground fg=
title = tk.Label(window, text="HANGMAN", bg=colour, font=("Arial", 50))
title.place(relx=0.38, rely=0.05)

#creation of exit button
EXIT = tk.Button(window, text="EXIT", bg=colour, command=EXIT)
EXIT.place(relx=0.5, rely=0.95)

#layout variables for alphabet
FONT = ("Arial", 20)
row1 = 0.3
row2 = 0.4
row3 = 0.5
row4 = 0.6
row5 = 0.7
row6 = 0.8
column1 = 0.05
column2 = 0.1
column3 = 0.15
column4 = 0.2
column5 = 0.25
A = tk.Button(window, text="A", bg=colour, font=FONT, command=lambda : check('A')) #lambda use to stop command triggering on startup
A.place(relx=column1, rely=row1)

B = tk.Button(window, text="B", bg=colour, font=FONT, command=lambda : check('B'))
B.place(relx=column2, rely=row1)

C = tk.Button(window, text="C", bg=colour, font=FONT, command=lambda : check('C'))
C.place(relx=column3, rely=row1)

D = tk.Button(window, text="D", bg=colour, font=FONT, command=lambda : check('D'))
D.place(relx=column4, rely=row1)

E = tk.Button(window, text="E", bg=colour, font=FONT, command=lambda : check('E'))
E.place(relx=column5, rely=row1)

F = tk.Button(window, text="F", bg=colour, font=FONT, command=lambda : check('F'))
F.place(relx=column1, rely=row2)

G = tk.Button(window, text="G", bg=colour, font=FONT, command=lambda : check('G'))
G.place(relx=column2, rely=row2)

H = tk.Button(window, text="H", bg=colour, font=FONT, command=lambda : check('H'))
H.place(relx=column3, rely=row2)

I = tk.Button(window, text="I", bg=colour, font=FONT, command=lambda : check('I'))
I.place(relx=column4, rely=row2)

J = tk.Button(window, text="J", bg=colour, font=FONT, command=lambda : check('J'))
J.place(relx=column5, rely=row2)

K = tk.Button(window, text="K", bg=colour, font=FONT, command=lambda : check('K'))
K.place(relx=column1, rely=row3)

L = tk.Button(window, text="L", bg=colour, font=FONT, command=lambda : check('L'))
L.place(relx=column2, rely=row3)

M = tk.Button(window, text="M", bg=colour, font=FONT, command=lambda : check('M'))
M.place(relx=column3, rely=row3)

N = tk.Button(window, text="N", bg=colour, font=FONT, command=lambda : check('N'))
N.place(relx=column4, rely=row3)

O = tk.Button(window, text="O", bg=colour, font=FONT, command=lambda : check('O'))
O.place(relx=column5, rely=row3)

P = tk.Button(window, text="P", bg=colour, font=FONT, command=lambda : check('P'))
P.place(relx=column1, rely=row4)

Q = tk.Button(window, text="Q", bg=colour, font=FONT, command=lambda : check('Q'))
Q.place(relx=column2, rely=row4)

R = tk.Button(window, text="R", bg=colour, font=FONT, command=lambda : check('R'))
R.place(relx=column3, rely=row4)

S = tk.Button(window, text="S", bg=colour, font=FONT, command=lambda : check('S'))
S.place(relx=column4, rely=row4)

T = tk.Button(window, text="T", bg=colour, font=FONT, command=lambda : check('T'))
T.place(relx=column5, rely=row4)

U = tk.Button(window, text="U", bg=colour, font=FONT, command=lambda : check('U'))
U.place(relx=column1, rely=row5)

V = tk.Button(window, text="V", bg=colour, font=FONT, command=lambda : check('V'))
V.place(relx=column2, rely=row5)

W = tk.Button(window, text="W", bg=colour, font=FONT, command=lambda : check('W'))
W.place(relx=column3, rely=row5)

X = tk.Button(window, text="X", bg=colour, font=FONT, command=lambda : check('X'))
X.place(relx=column4, rely=row5)

Y = tk.Button(window, text="Y", bg=colour, font=FONT, command=lambda : check('Y'))
Y.place(relx=column5, rely=row5)

Z = tk.Button(window, text="Z", bg=colour, font=FONT, command=lambda : check('Z'))
Z.place(relx=column3, rely=row6)

canvas = tk.Canvas(window, height=Sheight*0.6, width=Swidth*0.6)
canvas.place(relx=0.35, rely=row1)

t = turtle.RawTurtle(canvas)
screen = t.getscreen()
screen.bgcolor=("white")

wordDisplay = tk.Label(window, text="WORD", font=("Arial",30), bg=colour)
wordDisplay.place(relx=0.1, rely=0.2)

RESTART = tk.Button(bg=colour, text="RESTART", command=restart)
RESTART.place(relx=0.7, rely=0.95)

Word()

window.mainloop()


