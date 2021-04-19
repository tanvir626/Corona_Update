from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.iconbitmap(r"logo.ico")
root.title("Corona Update")
root.geometry("700x490")
root.resizable(0,0)#new thing
root.configure(background="#ffffff")
#Seting up the canvas
bg=ImageTk.PhotoImage(Image.open("t.jpg"))
can=Canvas(root,width=700,height=490)
can.pack(fill="both",expand=True)
can.create_image(0,0, image=bg,anchor="nw")

#header
can.create_text(350,50,text="Corona",font="arial 50 bold",fill="black")
can.create_text(350,60,text="______",font="arial 50 ",fill="black")

bg1=ImageTk.PhotoImage(Image.open("death1.png"))
can.create_image(180,130, image=bg1,anchor="nw")

bg2=ImageTk.PhotoImage(Image.open("infa.png"))
can.create_image(200,220, image=bg2,anchor="nw")

bg3=ImageTk.PhotoImage(Image.open("safe.png"))
can.create_image(200,310, image=bg3,anchor="nw")


root.mainloop()