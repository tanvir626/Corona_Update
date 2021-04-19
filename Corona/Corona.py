from tkinter import *
from PIL import ImageTk,Image
import requests
import json

#taking corona info
a=requests.get("https://coronavirus-19-api.herokuapp.com/all")
x=json.loads(a.content)
#putting info to variables
print(a.text)
cases=(x["cases"])
deaths=(x["deaths"])
recovered=(x["recovered"])

#Creating window
root=Tk()
root.iconbitmap(r"logo.ico")
root.title("Corona Update")
root.geometry("700x490")
root.resizable(0,0)#new thing
root.configure(background="#ffffff")

#Seting up the canvas and background
bg=ImageTk.PhotoImage(Image.open("t.jpg"))
can=Canvas(root,width=700,height=490)
can.pack(fill="both",expand=True)
can.create_image(0,0, image=bg,anchor="nw")

#header
can.create_text(350,50,text="Corona",font="arial 50 bold",fill="black")
can.create_text(350,60,text="______",font="arial 50 ",fill="black")

#death image
bg1=ImageTk.PhotoImage(Image.open("death1.png"))
can.create_image(100,130, image=bg1,anchor="nw")

#death entry
db=Entry(root,font="arial 20",width=20,fg="red",bd=0,justify="center")
db.insert(0,deaths)
dbv=can.create_window(360,165,window=db)

#infected image
bg2=ImageTk.PhotoImage(Image.open("infa.png"))
can.create_image(120,220, image=bg2,anchor="nw")

#infected entry
ib=Entry(root,font="arial 20",width=20,fg="#800080",bd=0,justify="center")
ib.insert(0,cases)
ibv=can.create_window(360,255,window=ib)

#safe image
bg3=ImageTk.PhotoImage(Image.open("safe.png"))
can.create_image(120,310,image=bg3,anchor="nw")

#safe entry
sb=Entry(root,font="arial 20",width=20,fg="green",bd=0,justify="center")
sb.insert(0,recovered)
sv=can.create_window(360,345,window=sb)

root.mainloop()