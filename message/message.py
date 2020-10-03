import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    ## if you are using some other sms bulk service just paste the whole python code here and the place where number and message is inset replace it with number and message.
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'YOUR_AUTHENTICATION_KEY',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    #print(dic)
    return dic.get('return')


def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


# Creating GUI
root = Tk()
root.title("Message Sender ")
photo = PhotoImage(file = "C:\\Users\\abhay\\Desktop\\ChatBot\\engine\\profile.png") ## YOur icon path
root.iconphoto(False, photo)
root.geometry("400x350")
font = ("Helvetica", 22, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textNumber.insert(0,"Moblie Number")
textNumber.configure(state=DISABLED)

textMsg = Text(root,height=10,font=("Helvatica",14))
textMsg.pack(fill=X)
textMsg.insert(END,"Enter Message")
def on_click(event):
    textNumber.configure(state=NORMAL)
    textNumber.delete(0,END)
    textNumber.unbind('<Button-1>',on_click_id)

on_click_id = textNumber.bind('<Button-1>',on_click)

sendBtn = Button(root, text="SEND SMS",pady=5,padx=3, command=btn_click)
sendBtn.pack()
root.mainloop()
