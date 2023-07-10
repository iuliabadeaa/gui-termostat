from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("700x450")
root.configure(bg="#1D2951")

temp_global="23"
current_temp=int(temp_global)

frame=Frame(root,width=100,height=100)
frame.place(x=420,y=210)
circle_img=ImageTk.PhotoImage(Image.open("circle.png"))
circle=Label(frame,image=circle_img,bg="#1D2951").pack()


def raise_tmp():
    global current_temp
    current_temp=current_temp+1
    temp_global=str(current_temp)

    temp_label=Label(root,text=temp_global,font=("Arial",30),bg="#FFFFFF")
    temp_label.place(x=448,y=238)

    return temp_global



def lower_tmp():
    global current_temp
    current_temp=current_temp-1
    temp_global=str(current_temp)

    temp_label=Label(root,text=temp_global,font=("Arial",30),bg="#FFFFFF")
    temp_label.place(x=448,y=238)

    return temp_global



frame1=Frame(root,width=20,height=20)
frame1.place(x=420,y=100)

circle_img1=ImageTk.PhotoImage(Image.open("circle2.png"))
circle1=Label(frame1,image=circle_img,bg="#1D2951").pack()

plus=Button(root,text="+",font=("Arial",20),bg="#FFFFFF",borderwidth=0,relief="solid", state=NORMAL,command=raise_tmp)
plus.place(x=454,y=123)


temp_lbl=Label(root,text=temp_global,font=("Arial",30),bg="#FFFFFF")
temp_lbl.place(x=448,y=238)


frame2=Frame(root,width=20,height=20)
frame2.place(x=418,y=330)

circle_img2=ImageTk.PhotoImage(Image.open("circle3.png"))
circle2=Label(frame2,image=circle_img,bg="#1D2951").pack()

minus=Button(root,text="-",font=("Arial",20),bg="#FFFFFF",borderwidth=0,relief="solid",state=NORMAL ,command=lower_tmp)
minus.place(x=454,y=353)

global status
status=True

def switch():
    global status
    if status==True:
        status=False
        plus.configure(state=DISABLED)
        minus.configure(state=DISABLED)
    else:
        plus.configure(state=NORMAL)
        minus.configure(state=NORMAL)
        status=True


toggle=Button(root,text="ON/OFF",font=("Arial",20),bg="#FFFFFF",borderwidth=0,relief="raised",command=switch)
toggle.place(x=415,y=30)

global room_temp
room_temp="22"

frame3=Frame(root,width=20,height=20)
frame3.place(x=100,y=100)

circle_img3=ImageTk.PhotoImage(Image.open("circle4.png"))
circle3=Label(frame3,image=circle_img3,bg="#1D2951").pack()

room_temp_label=Label(root,text=room_temp,font=("Arial",30),bg="#FFFFFF")
room_temp_label.place(x=128,y=125)

global humidity
humidity="90"

frame4=Frame(root,width=20,height=20)
frame4.place(x=100,y=250)

circle_img4=ImageTk.PhotoImage(Image.open("circle5.png"))
circle4=Label(frame4,image=circle_img4,bg="#1D2951").pack()

humidity_label=Label(root,text=humidity,font=("Arial",30),bg="#FFFFFF")
humidity_label.place(x=128,y=276)





mainloop()