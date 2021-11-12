import os
from tkinter import *
from PIL import ImageTk,Image  

global cwd
cwd = os.getcwd()

root = Tk() 

hu_img                      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\headsup.png"))
pushfold_img                = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\pushfold.png"))
notsupported_img            = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\range_not_supported.png"))

# A Radiobutton to toggle between images
bigblinds = IntVar()

def call():
    canvas.delete(ALL)
    #heads up
    if bigblinds.get() == 10:
        canvas.create_image((2, 2), image=pushfold_img, anchor=NW)
    else:
        canvas.create_image((2, 2), image=hu_img, anchor=NW)          

#Description
#L1=Label(root, text ="R=raise  G=call  B=fold").grid(row=0, column=0, columnspan=5, sticky=S)
#Big blinds selection
R4=Radiobutton(root, text="10", variable=bigblinds, value=10, command=call)
R4.grid(row=1, column=0, sticky=N+E)
R5=Radiobutton(root, text="11", variable=bigblinds, value=11, command=call)
R5.grid(row=1, column=1, sticky=N+E)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=330, width=330,)
canvas.grid(column=5, row=0, rowspan=6, sticky=W)
canvas.create_image((2, 2), image=hu_img, anchor=NW)

# Enter event loop
root.mainloop()