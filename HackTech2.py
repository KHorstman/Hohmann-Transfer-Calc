from astropy.io import fits 
import numpy as np  
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from tkinter import messagebox
from AnimatedGif import *
import sys
import os

#Animation      

window = Tk()

window.title("Earth to Planet Hohmann Transfer Simulator")
 
window.geometry('2000x1700')

window.maxsize(2000, 1700)

window.minsize(2000, 1700)

#Background image
#background_image=tk.PhotoImage(file='star.png')
#background_label = tk.Label(window, image=background_image)
#background_label.image = background_image
#background_label.place(x=1, y=1, relwidth=1, relheight=1)

mycolor= '#2A003F'

myother= '#42296B'

window.configure(background=mycolor)

#Planet gif
#lbl_with_my_gif = AnimatedGif(window, 'solar_system.gif', 0.0001)  # (tkinter.parent, filename, delay between frames)
#lbl_with_my_gif.grid()  # Packing the label with the animated gif (grid works just as well)
#lbl_with_my_gif.start_thread()  # Shows gif at first frame and we are ready to go

#lbl_with_my_gif.stop_thread() 

solar_image=tk.PhotoImage(file='sun.gif')
solar_label = tk.Label(window, image=solar_image, borderwidth=0, highlightthickness=0)
solar_label.image = solar_image
solar_label.place(relx=.5, rely=.65, anchor='c')

default_font = font.Font(family='Helvetica', size=30, weight='bold')

lbl2 = Label(window, text="Please Select Planet", font=('Helvetica',50,'bold'), borderwidth=2, relief='solid')

lbl2.config(background=mycolor, foreground='white',borderwidth=0)

lbl2.grid(column=0, row=2)

lbl2.place(relx=.5, rely=.1, anchor="c")

combo = Combobox(window, font =('Helvetica',50,'bold'), state='readonly', justify='center')
 
combo['values']= ("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
 
combo.current(1) #set the selected item
 
combo.grid(column=0, row=3, ipady=50, ipadx=175)

combo.place(relx=.5, rely=.2, anchor="c")

combo.config(background='white', foreground=mycolor)

window.option_add("*TCombobox*Listbox*Font", default_font)

def clicked2():
 
    res2 = "Destination = " + combo.get()
 
    lbl2.configure(text= res2)

    hehe = combo.get() + ".png"

    planet_image=tk.PhotoImage(file=hehe)
    planet_label = tk.Label(window, image=planet_image)
    planet_label.image = planet_image
    planet_label.place(relx=.5, rely=.65, anchor='c')

    cute_image=tk.PhotoImage(file='fart.gif')
    cute_label = tk.Label(window, image=cute_image)
    cute_label.image = cute_image
    cute_label.place(relx=.15, rely=.1, anchor='n')

    #sun_image=tk.PhotoImage(file='sun3.gif')
    #sun_label = tk.Label(window, image=sun_image, height=200, width=100)
    #sun_label.image = sun_image
    #sun_label.place(relx=.85, rely=.1, anchor='n')
    def restart_program():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    reset = tk.Button(window, text="Reset", command = restart_program, font=("Helvetica", 30), bg=myother, fg='white')

    reset.grid(column=0, row=5, ipady=50, ipadx=200)

    reset.place(relx=.85, rely=.18, anchor="n")


btn2 = tk.Button(window, text="Confirm Hohmann Transfer Destination", command = clicked2, font=("Helvetica", 30), bg=mycolor, fg='white')

btn2.grid(column=0, row=5, ipady=50, ipadx=200)

btn2.place(relx=.5, rely=.3, anchor="c")

window.mainloop()