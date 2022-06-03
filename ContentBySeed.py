###
#Created by Derek Gooding | June 1, 2022
#Shows a working proof of concept example for using random generation instead of hard coding color values.
###
import tkinter as tk
import random
from contextlib import suppress #allows for an inlined try/except that doesn't need an "except: pass". BaseException suppresses all exceptions

#change this variable to increase or decrease seed variance
RandomLimit = 10000 

def RandomColor():
    return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) 
      
def RandomSeed():
    input = inputbox.get()
    inputbox.delete(0, tk.END)
    with suppress(BaseException): 
        if  1 <= int(input) <= RandomLimit: 
            return int(input)
    random.seed()
    return random.randint(1,RandomLimit)

def ShuffleEnter(event):
    Shuffle()

def Shuffle():
    seed = RandomSeed()
    random.seed(seed)   
    label.config(text="Seed = " + str(seed))
    [x.config(background=RandomColor()) for x in buttonArray]

#Prepare visuals
mainWindow = tk.Tk()
mainWindow.geometry('100x250')
inputbox = tk.Entry(width=10)
inputbox.bind('<Return>', ShuffleEnter)
label = tk.Label()
shuffleButton = tk.Button(text="Shuffle", command=lambda: Shuffle)
buttonArray = [tk.Button(text=x, width=5, command=lambda n=x: print(n)) for x in range(6)]


#Pack everything
inputbox.pack(pady=2)
label.pack()
shuffleButton.pack(pady=1)
[x.pack(pady=1) for x in buttonArray]

Shuffle()
mainWindow.mainloop()
