#Libraries
from tkinter import *
from tkinter import colorchooser,filedialog,dialog,messagebox,simpledialog

#Application Setup
root = Tk()
root.title("Toggle Switch")
root.geometry("400x600+360+60")
root.resizable(False,False)
root.configure(bg="white")

#Functions
button_mode = True
def color(event):
    cls = colorchooser.askcolor(title="Select color to change")
    root.configure(bg=cls[1])
    btn.config(bg=cls[1],activebackground=cls[1])
    l1.config(bg=cls[1],activebackground=cls[1]);

def customize():
    global button_mode
    if(button_mode):
        btn.config(image=off,bg="#26242f",activebackground="#26242f")
        root.config(bg="#26242f"); l1.config(bg="#26242f")
        l1.config(fg="lime")
        button_mode = False
    else:
        btn.config(image=on,bg="white",activebackground="white")
        root.config(bg="white"); l1.config(bg="white")
        l1.config(fg="black")
        button_mode = True

#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\toggle.png")
on = PhotoImage(file="E:\\pyImages\\light.png")
off = PhotoImage(file="E:\\pyImages\\dark.png")
root.iconphoto(False,img1)
btn = Button(root,image=on,bd=0,activebackground="white",bg="white",command=customize)
btn.pack(padx=50,pady=50)
l1 = Label(root,text="This is a GUI application named as\n Toggle Switch to change the\n the light theme to"
    "dark theme\n and another mode from dark to light theme.\n You can change the background into\n different colors using color event\n function. You can simply click on\n Clt+g and the title select color\n to change will be open.\n Now you can change the background color\n of the GUI application.",bg="white",fg="black",activebackground="white",font="TimesNewRoman 10 bold")
l1.place(x=60,y=300)
root.bind('<Control-g>',color)
root.mainloop()
