import os
from tkinter import *
from PIL import ImageTk,Image  

global cwd
cwd = os.getcwd()

root = Tk()
root.iconbitmap("hud_icon_small.ico")
root.title('Rangers')

ug                           = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\ug.png"))
hj                           = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\hj.png"))
co                           = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\co.png"))
db                           = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\db.png"))
sb                           = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\sb.png"))
pushfold_img                 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\pushfold.png"))
bb_vs_btn                    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\bb_vs_btn.png"))
bb_vs_utg                    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\bb_vs_utg.png"))


# A Radiobutton to toggle between images
bigblinds = IntVar()

def call():
    canvas.delete(ALL)
    #heads up
    if bigblinds.get() == 1:
        canvas.create_image((2, 2), image=ug, anchor=NW)
    elif bigblinds.get() == 2:
        canvas.create_image((2, 2), image=hj, anchor=NW)
    elif bigblinds.get() == 3:
        canvas.create_image((2, 2), image=co, anchor=NW)
    elif bigblinds.get() == 4:
        canvas.create_image((2, 2), image=db, anchor=NW)
    elif bigblinds.get() == 5:
        canvas.create_image((2, 2), image=sb, anchor=NW)
    elif bigblinds.get() == 6:
        canvas.create_image((2, 2), image=pushfold_img, anchor=NW)
    elif bigblinds.get() == 7:
        canvas.create_image((2, 2), image=bb_vs_btn, anchor=NW)
    elif bigblinds.get() == 8:
        canvas.create_image((2, 2), image=bb_vs_utg, anchor=NW)
    else:
        pass      

#Description
R1=Radiobutton(root, text="UG", variable=bigblinds, value=1, command=call)
R1.grid(row=1, column=0, sticky=N+E)
R2=Radiobutton(root, text="HJ", variable=bigblinds, value=2, command=call)
R2.grid(row=2, column=0, sticky=N+E)
R3=Radiobutton(root, text="CO", variable=bigblinds, value=3, command=call)
R3.grid(row=3, column=0, sticky=N+E)
R4=Radiobutton(root, text="DB", variable=bigblinds, value=4, command=call)
R4.grid(row=4, column=0, sticky=N+E)
R5=Radiobutton(root, text="SB", variable=bigblinds, value=5, command=call)
R5.grid(row=5, column=0, sticky=N+E)
R6=Radiobutton(root, text="push-fold", variable=bigblinds, value=6, command=call)
R6.grid(row=6, column=0, sticky=N+E)
R7=Radiobutton(root, text="bb_vs_btn", variable=bigblinds, value=7, command=call)
R7.grid(row=7, column=0, sticky=N+E)
R8=Radiobutton(root, text="bb_vs_utg", variable=bigblinds, value=8, command=call)
R8.grid(row=8, column=0, sticky=N+E)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=455, width=455,)
canvas.grid(column=5, row=0, rowspan=6, sticky=W)
canvas.create_image((2, 2), image=bb_vs_btn, anchor=NW)

# Enter event loop
root.mainloop()