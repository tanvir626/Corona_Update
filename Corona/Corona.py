from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.iconbitmap(r"logo.ico")
root.title("Corona Update")
root.geometry("700x490")
root.resizable(1,1)#new thing
root.configure(background="#ffffff")
#background
bg=ImageTk.PhotoImage(Image.open("t.jpg"))
bgl=Label(root,image=bg)
bgl.place(x=0,y=0,relwidth=1,relheight=1)

#header
l1=Label(root,text="Corona",bg='#fff0ff',fg="#FF0010",font="arial 30",padx=30)
l1.grid(row=0,column=1,columnspan=2,pady=20,padx=140)

#Infected
l2=Label(root,text="Image",bg='#fff0ff',fg="#FF0010",font="arial 30",pady=20)
l2.grid(row=1,column=0,pady=30,padx=10)
e1=Entry(root,text="e")
e1.grid(row=1,column=1,pady=30,padx=10)

#recover
l2=Label(root,text="Image",bg='#fff0ff',fg="#FF0010",font="arial 30",pady=20)
l2.grid(row=1,column=2,pady=30,padx=10)
e1=Entry(root,text="e")
e1.grid(row=1,column=3,pady=30,padx=10)

#died
l2=Label(root,text="Image",bg='#fff0ff',fg="#FF0010",font="arial 30",pady=20)
l2.grid(row=2,column=0,pady=30,padx=10)
e1=Entry(root,text="e")
e1.grid(row=2,column=1,pady=30,padx=10)
root.mainloop()