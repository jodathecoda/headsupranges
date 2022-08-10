import os
from tkinter import *
from PIL import ImageTk,Image  

global cwd
cwd = os.getcwd()

root = Tk()
root.title('1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')

hu2x_img                    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\slumbot2x.png"))
pushfold_img                = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\pushfold.png"))
hu3x_img                    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\slumbot3x.png"))
custom_img                  = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\custom.png")) 

# A Radiobutton to toggle between images
bigblinds = IntVar()

def call():
    canvas.delete(ALL)
    #heads up
    if bigblinds.get() == 10:
        canvas.create_image((2, 2), image=pushfold_img, anchor=NW)
    elif bigblinds.get() == 11:
        canvas.create_image((2, 2), image=hu2x_img, anchor=NW)
    elif bigblinds.get() == 12:
        canvas.create_image((2, 2), image=hu3x_img, anchor=NW)
    elif bigblinds.get() == 13:
        canvas.create_image((2, 2), image=custom_img, anchor=NW)
    else:
        pass      

#Description
#L1=Label(root, text ="R=raise  G=call  B=fold").grid(row=0, column=0, columnspan=5, sticky=S)
#Big blinds selection
R4=Radiobutton(root, text="s", variable=bigblinds, value=10, command=call)
R4.grid(row=1, column=0, sticky=N+E)
R5=Radiobutton(root, text="m", variable=bigblinds, value=11, command=call)
R5.grid(row=2, column=0, sticky=N+E)
R6=Radiobutton(root, text="p", variable=bigblinds, value=12, command=call)
R6.grid(row=3, column=0, sticky=N+E)
R7=Radiobutton(root, text="o", variable=bigblinds, value=13, command=call)
R7.grid(row=4, column=0, sticky=N+E)
#L1=Label(text="hello")
#L1.grid(row=4, column=0, sticky=N+E)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=455, width=455,)
canvas.grid(column=5, row=0, rowspan=6, sticky=W)
canvas.create_image((2, 2), image=hu3x_img, anchor=NW)

# Enter event loop
root.mainloop()