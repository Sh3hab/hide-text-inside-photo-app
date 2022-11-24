from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb
from tkinter import font
import webbrowser
from tkinter import messagebox

root=Tk()
root.title("hide text inside photo")
root.geometry("390x700")
root.resizable(False,False)
root.configure(bg="black")



def close():
    message = messagebox.askquestion('hide text inside photo', "Do you want to exit.")
    if message == "yes":
        root.quit()


def view_help():
    webbrowser.open('https://github.com/Sh3hab/Sh3hab/tree/main')

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select image file',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def save():
    secret.save("hide text inside photo app.png")

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename), message)

def Show():
    clear_massage = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_massage)


#icon
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="black").place(x=310,y=0)

Label(root,text="إخفاء النص في الصورة",bg="black",fg="#126161",font="Tahoma 25").place(x=10,y=15)

#first frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#second frime
frame2=Frame(root,bd=3,width=340,height=180,bg="white",relief=GROOVE)
frame2.place(x=10,y=380)

text1=Text(frame2,font='Tahoma 20',bg='#126161',fg='black',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
frame3=Frame(root,bd=3,bg='black',width=250,height=85,relief=GROOVE)
frame3.place(x=10,y=570)

B1 = Button(frame3,text='افتح الصورة',width=9,height=3,bg="#126161",fg="black",font='Tahoma 11 bold',command=showimage).place(x=150,y=5)
B2 = Button(frame3,text='احفظ الصورة',width=10,height=2,bg="#0B4040",fg="black",font='Tahoma 16 bold',command=save).place(x=5,y=5)
#Label(frame3,text='picture, image, photo file',bg='#2f4155',fg='yellow').place(x=20,y=5)

#fourth frame
frame4=Frame(root,bd=3,bg='black',width=95,height=85,relief=GROOVE)
frame4.place(x=265,y=570)

B3 = Button(frame4,text='إخفاء النص',width=8,height=1,bg="#126161",fg="black",font='Tahoma 11 bold',command=Hide).place(x=5,y=5)

B4 = Button(frame4,text='إظهار النص',width=8,height=1,bg="#126161",fg="black",font='Tahoma 11 bold',command=Show).place(x=5,y=45)
#Label(frame4,text='picture, image, photo file',bg='black',fg='yellow').place(x=20,y=5)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=close)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label="View Help",command=view_help)



root.mainloop()