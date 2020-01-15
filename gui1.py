from tkinter import *
import requests
import jsons
from tkinter import messagebox

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

#gui for the first window
window=Tk()
window.geometry("500x300")
window.configure(background='aqua')

#function to send the message

#open an account in way2sms and get the apikey and secret key
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


#function for the button 'send_sms' from the first window
def send_sms():

    #function for the button send from the second window
    def send():
        if(e1.get()==""):
            messagebox.showinfo("Warning","Recipient should not be empty")#displays an info box with warning as title and the message
        else:
            response = sendPostRequest(URL, 'apikey', 'secretkey', 'stage', e1.get(), 'your email id', e2.get() )
   
    def reset():
        message.set("")#resets the entry to  "" use the textvariable of the entry and no the entry variable
        text.set("")


    window.destroy()#once send sms is clicked the first window is closed and new window is opened
    sms=Tk()
    sms.geometry("400x350")
    sms.configure(background='pink')  

    l2 = Label(sms,text="SENDING SMS",font="times 20")
    l2.grid(row=1,column=2,padx=20)

    l3=Label(sms,text="Recipient",font="times 20")
    l3.grid(row=4,column=0,pady=10)

    text=StringVar()#this variable is used in resetting like text.set("")

    e1= Entry(sms,textvariable=text)
    e1.grid(row=4,column=2,pady=10)
    
    l4=Label(sms,text="Message",font="times 20")
    l4.grid(row=6,column=0,pady=10)

    message=StringVar()
    e2=Entry(sms,textvariable=message)
    e2.grid(row=6,column=2,pady=10)

    b3=Button(sms,text="SEND",font="times 18",width=10,command=send)
    b3.grid(row=8,column=2,padx=0)

    b4=Button(sms,text="RESET",font="times 18",width=10,command=reset)
    b4.grid(row=12,column=2,padx=0)


#the labels and buttons in first window this gets executed first
l1= Label(window,text="GUI FOR SENDING MESSAGE",font="times 20")
l1.grid(row=1,column=2,columnspan=2,padx=50)

b1=Button(window,text="SEND SMS",font="times 18",width=10,command=send_sms)
b1.grid(row=20,column=2,padx=70,pady=50)

b2= Button(window,text="EXIT",font="times 18",width=10,command="exit")#exit command can be directly used instead of using function
b2.grid(row=22,column=2,padx=70,pady=10)

window.mainloop()