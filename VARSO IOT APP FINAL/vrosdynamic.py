import csv
from email.mime import image
from email.utils import localtime
from threading import Thread, local
import threading
from time import time
from turtle import speed
import requests
import cmd
import imghdr
import smtplib
from email.message import EmailMessage
from PIL import Image, ImageTk, Image
import pyqrcode
from codecs import latin_1_decode
from email import message
from enum import unique
from fileinput import filename
import json
from multiprocessing import context
from tkinter import *
from curses import window
import tkinter as tk
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
from unicodedata import name
from urllib import request
import qrcode
from traceback import format_exc
import time
import os


################################### Tkinter window configure ##############################3

window = Tk()
window.state('zoomed')
window.geometry("800x800")
window.title("Welocme to Varso Technologies .....")


#########################################################   

#filename = PhotoImage(file='s22.png')
#limg= Label(window, i=filename)
#limg.pack()

window.configure(background="#3F3F3F")

lb = Label(window, text="𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆 𝕍𝔸ℝ𝕆𝕊 𝕋𝔼ℂℍℕ𝕆𝕃𝕆𝔾𝕀𝔼𝕊.",  bg="#FAEFAE", fg="red", font=("Arial Bold", 30))
lb.grid(padx=280, pady=10, row=6,column=7)
#lb.place(anchor = CENTER, relx = .5, rely = .2)




#Canvas = tk.Canvas(window, height=800, width=800, bg="#263D42")
#Canvas.pack()


########################################################################## function Start ########################



def esp_fun(esp_no):
    try:
        ESP_NO = {"ESP_NO": str(esp_no)}
        n_data = json.dumps(ESP_NO)
        URL = "http://13.233.196.149:3000/esptrack/getautoincrement"
        r = requests.get(url=URL, data=ESP_NO)
        data = r.json()
        employee_dict = json.dumps(data)
        res_data = json.loads(employee_dict)
        main_data = res_data['result']
        esp_no = main_data['ESP_NO']
        unique_id = main_data['unique_id']
        POP = main_data['POP']


        print(f"esp no: {esp_no}")
        print(f"unique_id : {unique_id}")
        print(f"POP: {POP}")
        context = {'unique_id': unique_id, 'POP':POP}
        return context
    except ValueError:
        messagebox.showerror("showerror", "ENTER THE IOT NO :")


def eeprom_func():
    try:
        int(textentery1.get())
        #int(textentery2.get())

        os.system('cmd /c "sh eeprom.sh"')

    except ValueError:
        messagebox.showerror("showerror", "ENTER THE IOT NO.")


def parse():
    try:
        int(textentery1.get())
        ESP = textentery1.get()
        data = esp_fun(ESP)
        print(data)

        textentery2.insert(0,data['unique_id'])
        cliptext = textentery2.clipboard_get()
        textentery3.insert(0,data['POP'])
        cliptext = textentery3.clipboard_get()
    except ValueError:
        messagebox.showerror("showerror","Enter the IOT NO")

    


##############################################  QRCODE GENR FUNCTION  ################################################


def qr_generate():
    try:
        int(textentery1.get())
        ESP_NO = textentery1.get()
        unique_id = textentery2.get()
        POP = textentery3.get()

        filename1 = ("ESP NO" + (f"{ESP_NO}")),
        filename2 = ("unique_id :" + (f"{unique_id}")),
        filename3 = ("POP :" + (f"{POP}")),

        filename4 ={
            "ESP_NO":(f"{ESP_NO}"),
            "unique_id": (f"{unique_id}"),
            "POP": (f"{POP}")
        } 

        filename5 = json.dumps(filename4)
        url = pyqrcode.create(filename5)
        file_name = (f"{unique_id}") + ".png"
        url.png(file_name, scale=3)

        image = ImageTk.PhotoImage(Image.open(file_name))
        image_label = Label(image=image)
        image_label.image = image

        #frame = tk.image_label(window, bg="white")
        image_label.place(relwidth=0.2, relheight=0.4, relx=0.6, rely=0.2)

        
       # frame.place(400,100,frame=image_label)
        print("IOT_ID"+unique_id),"abcd1234"

####################################



############################################## data insert csv file ###########################################


        localtime = time.asctime(time.localtime(time.time()))
        print(localtime)

        zip_object = zip(( f"{ESP_NO}"), (f"{unique_id}"), (f"{POP}"), localtime)

        esp_count = 0
        with open ('D:\\varos system app\\VAROS PRDOUCTION IOT APP\\VARSO IOT APP FINAL\\New.csv','a')as csvfile:
            
             fieldnames = ['ESP_NO','unique_id','POP','TIME']
             thewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)

          
             d = {'ESP_NO':(f"{ESP_NO}"),'unique_id':(f"{unique_id}"),'POP':(f"{POP}"), 'TIME':localtime}
             thewriter.writerow(d)

        csvfile.close()

####################################  Email data send ##########################################


        msg = EmailMessage()

        msg['Subject'] = f"Varso Device ({ESP_NO,unique_id,POP})"
        
        msg['From'] = 'Varso Production'
        msg['To'] =  'varsoiot@gmail.com'

        with open((f"{file_name}"),"rb") as f:
            file_data = f.read()
            print("file send",file_data)
            filetype = imghdr.what(f.name)
            file_name_img = f.name
            print("File name is",file_name_img)
            msg.add_attachment(file_data, maintype="image", subtype=filetype, filename=file_name_img)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
             server.login("varsoiot@gmail.com","tcxixcyhvkxxalit")
             server.send_message(msg)
        print("mail sent")       

    except ValueError:
        messagebox.showerror("showerror","Enter the IOT NO")

####################################################################################################################### 

####################################################################   

def generate():
    try:
        int(textentery1.get())
        ESP_NO = textentery1.get()
        unique_id = textentery2.get()
        POP = textentery3.get()

        filename1 = ("ESP NO" + (f"{ESP_NO}")),
        filename2 = ("unique_id :" + (f"{unique_id}")),
        filename3 = ("POP :" + (f"{POP}")),

        filename4 ={
            "ESP_NO":(f"{ESP_NO}"),
            "unique_id": (f"{unique_id}"),
            "POP": (f"{POP}")
        } 

        filename5 = json.dumps(filename4)
        url = pyqrcode.create(filename5)
        file_name = (f"{unique_id}") + ".png"
        url.png(file_name, scale=3)

        image = ImageTk.PhotoImage(Image.open(file_name))
        image_label = Label(image=image)
        image_label.image = image

        #frame = tk.image_label(window, bg="white")
        image_label.place(relwidth=0.2, relheight=0.4, relx=0.6, rely=0.2)

        
       # frame.place(400,100,frame=image_label)
        print("IOT_ID"+unique_id),"abcd1234"

####################################



############################################## data insert csv file ###########################################


        localtime = time.asctime(time.localtime(time.time()))
        print(localtime)

        zip_object = zip(( f"{ESP_NO}"), (f"{unique_id}"), (f"{POP}"), localtime)

        esp_count = 0
        with open ('D:\\varos system app\\VAROS PRDOUCTION IOT APP\\VARSO IOT APP FINAL\\New.csv','a')as csvfile:
            
             fieldnames = ['ESP_NO','unique_id','POP','TIME']
             thewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)

          
             d = {'ESP_NO':(f"{ESP_NO}"),'unique_id':(f"{unique_id}"),'POP':(f"{POP}"),'TIME':localtime}
             thewriter.writerow(d)

        csvfile.close()

####################################  Email data send ##########################################


        msg = EmailMessage()

        msg['Subject'] = f"Varso Device ({ESP_NO,unique_id,POP})"
        
        msg['From'] = 'Varso Production'
        msg['To'] =  'varsoiot@gmail.com'

        with open((f"{file_name}"),"rb") as f:
            file_data = f.read()
            print("file send",file_data)
            filetype = imghdr.what(f.name)
            file_name_img = f.name
            print("File name is",file_name_img)
            msg.add_attachment(file_data, maintype="image", subtype=filetype, filename=file_name_img)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
             server.login("varsoiot@gmail.com","tcxixcyhvkxxalit")
             server.send_message(msg)
        print("mail sent")

        os.system('cmd /k "sh burn.sh"')       

    except ValueError:
        messagebox.showerror("showerror","Enter the IOT NO")


####################################################################################  clear all box and code #################3


def delete_listbox():
    textentery1.delete(0,END)
    textentery1.delete(0,END)
    textentery2.delete(0,END)
    textentery3.delete(0,END)


#####################################################  USER INTERFACE ###############################################



frame = tk.Frame(window, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
frame.configure(background="#5D6D7E")



text1 = Label(frame, text="IOT_NO:")
text1.configure(background="#5D6D7E", fg= 'black', font=("𝑿𝑹  𝑩𝑨𝑫  𝑩𝑶𝒀", 15, "bold" ))
text1.grid(padx=40, pady=20,row=4,column=0)

textentery1 = Entry(frame, font = "Helvetica")
textentery1.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 10, "bold" ))
textentery1.grid(pady= 10,row=4, column=1)

text2 = Label(frame, text="IOT_DEVICE_ID")
text2.configure(background="#5D6D7E", fg= 'black', font=("𝑿𝑹  𝑩𝑨𝑫  𝑩𝑶𝒀", 15, "bold" ))
text2.grid(padx= 20, pady= 10,row=5,column=0)

textentery2 = Entry(frame, font = "Helvetica")
textentery2.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 10, "bold" ))
textentery2.grid(padx= 20,pady= 10,row=5, column=1)


##################################################################################################################

text3 = Label(frame, text="IOT_POP")
text3.configure(background="#5D6D7E", fg= 'black', font=("𝑿𝑹  𝑩𝑨𝑫  𝑩𝑶𝒀", 15, "bold" ))
text3.grid(padx= 20, pady= 10,row=6,column=0)

textentery3 = Entry(frame, font = "Helvetica")
textentery3.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 10, "bold" ))
textentery3.grid(padx= 20,pady= 10,row=6, column=1)

#text4 = Label(frame, text="Text4")
#text4.configure(background="#5D6D7E", fg= 'black', font=("𝑿𝑹  𝑩𝑨𝑫  𝑩𝑶𝒀", 15, "bold" ))
#text4.grid(padx= 20, pady= 10,row=7,column=0)

#textentery4 = Entry(frame, font = "Helvetica")
#textentery4.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 10, "bold" ))
#textentery4.grid(padx= 20,pady= 10,row=7, column=1)

################################################################################################################################

button1=Button(frame,text='GET_DATA')
button1.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ), command=threading.Thread(target=parse).start)
button1.grid(padx=5,pady= 10,row=8, column=0)


button2=Button(frame,text='EEPROM')
button2.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ), command=threading.Thread(target=eeprom_func).start)
button2.grid(padx=5,pady= 10,row=8, column=1)

button3=Button(frame,text='BURN IOT')
button3.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ), command=threading.Thread(target=generate).start)
button3.grid(padx=5,pady= 10,row=8, column=2)


button4=Button(frame,text='QRCODE_GENERATOR')
button4.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ), command=threading.Thread(target=qr_generate).start)
button4.grid(padx=5,pady= 10,row=10, column=1)



button5=Button(frame,text='DELETE_ENTRY')
button5.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ), command=delete_listbox)
button5.grid(padx=15,pady= 10,row=11, column=0)



button6=Button(frame,text='EXIT')
button6.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ), command=exit)
button6.grid(padx=5,pady= 10,row=11, column=1)


window.mainloop()
