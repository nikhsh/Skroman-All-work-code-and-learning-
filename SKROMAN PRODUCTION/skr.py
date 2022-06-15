from curses import window
from sys import modules
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import subprocess
import pyqrcode
from tkinter import filedialog
from shutil import copyfile
from tkinter import *
from PIL import ImageTk, Image
import time
import csv
import json
import os
import qrcode
import imghdr
import smtplib
from email.message import EmailMessage
import requests
import os


root=Tk()

root.title("WELCOME TO SKROMAN_PRODUCT NAME : ESP32")

#root.iconbitmap("D:\\skro.ico")
root.geometry("850x550")

#img = PhotoImage(file="skb.png")
#label = Label(
#    root,
 #   image=img
  #  )
#label.place(x=0, y=0)

root.configure(bg='#e3dac9')

modules = [
    "module2",
    "module4",
    "module6",
    "module8",
    "Two_Fan_module",
    "Mood_Switch",

    ]

submodules = [
    "23000",
    "44010",
    "45000",
    "46000",
    "65010",
    "67000",
    "87010",
    "89000",
    "88020",
    "Mood_Switch",
    ]


####### MODULE LIST CREATE#############

module_2 = ["23000"]
module_4 = ["44010", "45000", "46000"]
module_6 = ["65010", "67000"]
module_8 = ["87010", "89000"]
Two_Fan_module = ["88020"]
Mood_Switch = ["Mood_Switch"]
device_types = ["Swtich_Box", "SK_Blaze", "Temp Scan", "Punch Machine", "Mood_switch"]

heading = Label(text="SKROMAN MULTI TOUCH SERIES :-  ESP32", bg="#ffe4e1", fg="Black",font=("Times ", 15), width="80", height="2")
heading.pack()



percent = StringVar()
text = StringVar()
ESP_NO = StringVar()
unique_id = StringVar()
POP = StringVar()
my_combo = StringVar()
mod_combo = StringVar()

lbl = Label(root)
lbl.pack()

###################################33


def click_1():
    try:
        #filename = filedialog.askopenfilename(initialdir = "/home/skroman/esp/esp-idf/amol_codes/all_client/",
        filename = filedialog.askopenfilename(initialdir = "C:\esp\esp-idf\SK\SKSL_Common_RS_485_2Fan_2C_IR\spiffs_dir\sub",
     title = "Select a File",
     filetypes = (
     ("all files","."),("Text files","*.pem")))
      
        #copyfile(filename,'/home/skroman/esp/esp-idf/amol_codes/SKSL_Common/spiffs_dir/sub/AmazonRootCA1.pem')
        copyfile(filename,'C:\esp\esp-idf\SK\SKSL_Common_RS_485_2Fan_2C_IR\spiffs_dir\sub\AmazonRootCA11.pem')
        lbl.configure(text = "Uploaded Amazon Certificate")
    except ValueError:
        messagebox.showerror("showerror","Select the AmazonRootCA1.pem")

def click_2():
    filename1 = filedialog.askopenfilename(initialdir = "C:\esp\esp-idf\SK\SKSL_Common_RS_485_2Fan_2C_IR\spiffs_dir\sub",
    #filename1 = filedialog.askopenfilename(initialdir = "/home/skroman/esp/esp-idf/amol_codes/all_client/",
 title='Select a File',
 filetypes=(
 ("all files","."),("Text files","*.pem.crt")))
    copyfile(filename1, 'C:\esp\esp-idf\SK\SKSL_Common_RS_485_2Fan_2C_IR\spiffs_dir\sub\certificate1.pem.crt')

def click_3():
    filename2 = filedialog.askopenfilename(initialdir = "C:\esp\esp-idf\SK\SKSL_Common_RS_485_2Fan_2C_IR\spiffs_dir\sub",
    #filename2 = filedialog.askopenfilename(initialdir = "/home/skroman/esp/esp-idf/amol_codes/all_client/",
 title='Select a File',
 filetypes=(
 ("all files","."),("Text files","*.key")))
    copyfile(filename2, 'C:\esp\esp-idf\SK\SKSL_Common_RS_485_2Fan_2C_IR\spiffs_dir\sub\private1.pem.key') 



#######################333

####### pick up module ####

def pick_module(e):
    if my_combo.get() == "module2":
        mod_combo.config(value=module_2)
    if my_combo.get() == "module4":
        mod_combo.config(value=module_4)
        #mod_combo.current(0)
    if my_combo.get() == "module6":
        mod_combo.config(value=module_6)
        #mod_combo.current(0)
    if my_combo.get() == "module8":
        mod_combo.config(value=module_8)
        #mod_combo.current(0)
    if my_combo.get() == "Two_Fan_module":
        mod_combo.config(value=Two_Fan_module)
    if my_combo.get() == "Mood_Switch":
        mod_combo.config(value=Mood_Switch)
   # Create a dropdown Box
   # print(mod_combo.get())


my_combo = ttk.Combobox(root, value=modules)
# my_combo.current(0)
my_combo.place(x=30, y=55)
my_combo.bind("<<ComboboxSelected>>", pick_module)

mod_combo = ttk.Combobox(root, value=[""])
mod_combo.bind("<<ComboboxSelected>>", pick_module)
mod_combo.place(x=240, y=55)

device_combo = ttk.Combobox(root,value=device_types)
device_combo.place(x=430,y=55)
device_combo.set("Switch Box")
if device_combo == "":
     device_combo.set("Switch Box")
else:
     device_combo.get()


myprogress = ttk.Progressbar(root,orient=HORIZONTAL,length=800,mode="determinate")
myprogress.pack(pady=5)
percentLabel = Label(root,textvariable=percent).pack(padx=250)
taskLabel = Label(root,textvariable=text).pack(padx=250)

#######################33

###  Deleted list box 

def delete_listbox():
    my_list1.delete(0,END)
    name_entry1.delete(0,END)
    name_entry2.delete(0,END)
    name_entry3.delete(0,END)


################################# ESP NO FUNCTION#########
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
        print(f"unique id : {unique_id}")
        print(f"POP: {POP}")
        context = {'unique_id': unique_id, 'POP':POP}
        return context

    except ValueError:
        messagebox.showerror("showerror", "Enter the ESP NO :")
        
############# to defind EEPROM FUNCTIONALITY #############################
        
def eeprom_func():
    try:
        int(name_entry1.get())
       
        subprocess.call(['cmd','./eeprom.sh'])
        
    except ValueError:
        messagebox.showerror("showerror", "Enter the ESP NO")
        
    
################################ defined parse function #####

def parse():
    try:
        int(name_entry1.get())
        ESP = name_entry1.get()
        data = esp_fun(ESP)
        print(data)
        
        name_entry2.insert(0,data['unique_id'])
        cliptext = name_entry2.clipboard_get()
        name_entry3.insert(0,data['POP'])
        cliptext = name_entry2.clipboard_get()
    except ValueError:
        messagebox.showerror("showerror","Enter the ESP NO")

#####################################################################

def generate():
    try:
        int(name_entry1.get())
        ESP_NO = name_entry1.get()
        unique_id = name_entry2.get()
        POP = name_entry3.get()
        AWS = name_entry4.get()
        OTA = name_entry5.get()
        PRIVATE = name_entry6.get()


        file_name12 =("ModelNo:" + mod_combo.get())
        file_name2 = ("ESP NO :" + (f"{ESP_NO}"))
        file_name3 = ("unique_id :" + (f"{unique_id}"))
        file_name4 = ("POP:" + (f"{POP}"))
        file_name66 = ("Device Type:" + device_combo.get())



        filename1 = {
            "ModelNo":mod_combo.get(),
            "ESP_NO":(f"{ESP_NO}"),
            "unique_id": (f"{unique_id}"),
            "POP": (f"{POP}"),
            "DeviceType": device_combo.get()
            
            
            }

        filename5 = json.dumps(filename1)
        my_list1.insert(END, file_name12)
        my_list1.insert(END, file_name2)
        my_list1.insert(END, file_name3)
        my_list1.insert(END, file_name4)
        my_list1.insert(END, file_name66)
        
        url = pyqrcode.create(filename5)

        file_name = (f"{unique_id}") + ".png"
        url.png(file_name, scale=3)

        image = ImageTk.PhotoImage(Image.open(file_name))
        image_label = Label(image=image)
        image_label.image = image
        canvas.create_window(400,100,window=image_label)
        print("SKSL_"+unique_id),"abcd1234",AWS,OTA,PRIVATE,mod_combo.get()


        GB = 100
        download = 0
        speed = 0.2


        while (download < GB):
            time.sleep(0.001)
            myprogress['value'] += (speed / GB) * 100
            download += speed
            percent.set(str(int((download / GB) * 100)) + "%")
            root.update_idletasks()

        localtime = time.asctime(time.localtime(time.time()))
        print(localtime)

      
        zip_object = zip((f"{ESP_NO}"),(f"{unique_id}"), (f"{POP}"),localtime,mod_combo.get())

        esp_count = 0
        with open ('C:\\esp\\esp-idf\\amol_codes\\excelbackup.csv','a')as csvfile:
            
             fieldnames = ['ESP_NO','unique_id','POP','ModelNo','TIME']
             thewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)

          
             d = {'ESP_NO':(f"{ESP_NO}"),'unique_id':(f"{unique_id}"),'POP':(f"{POP}"),'ModelNo':mod_combo.get(),'TIME':localtime}
             thewriter.writerow(d)

        csvfile.close()
####################################################################################################################
###################  Mail send code ######################################
        msg = EmailMessage()
        msg['Subject'] = f"Skroman Device ({ESP_NO,unique_id,POP,mod_combo.get(),device_combo.get()})"
        
        msg['From'] = 'Skroman Production'
        msg['To'] =  'ns9625856@gmail.com'

        with open((f"{file_name}"),"rb") as f:
            file_data = f.read()
            print("file send",file_data)
            filetype = imghdr.what(f.name)
            file_name_img = f.name
            print("File name is",file_name_img)
            msg.add_attachment(file_data, maintype="image", subtype=filetype, filename=file_name_img)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
             server.login("ns9625856@gmail.com","mqujcgmpcqyjdhzh")
             server.send_message(msg)
        print("mail sent")

#########################################################################################################################
#################################
        subprocess.call(['cmd','./burn.sh'])

      

    except ValueError:
        messagebox.showerror("showerror","Enter the ESP NO  ")

###########################################################   
        
    

def generate_2mod():
    try:
        int(name_entry1.get())
        ESP_NO = name_entry1.get()
        unique_id = name_entry2.get()
        POP = name_entry3.get()
        AWS = name_entry4.get()
        OTA = name_entry5.get()
        PRIVATE = name_entry6.get()

        file_name12=("ModelNo: " + mod_combo.get())
        file_name2=("ESP NO: "+ (f"{ESP_NO}"))
        file_name3=("unique_id: " +(f"{unique_id}") )
        file_name4=("POP: "+ (f"{POP}"))
        file_name66 = ("Device Type: "+ device_combo.get())
      
        filename1 = {"ModelNo":mod_combo.get(),
                      "ESP_NO":(f"{ESP_NO}"),
                     "unique_id":(f"{unique_id}"),
                     "POP":(f"{POP}"),
                     "DeviceType":device_combo.get()
                    }
        filename5 = json.dumps(filename1)
        my_list1.insert(END,file_name12)
        my_list1.insert(END,file_name2)
        my_list1.insert(END,file_name3)
        my_list1.insert(END,file_name4)
        my_list1.insert(END,file_name66)
        url = pyqrcode.create(filename5)

       
        file_name = (f"{unique_id}")+".png"
        url.png(file_name,scale=3)
      
        image = ImageTk.PhotoImage(Image.open(file_name))
        image_label = Label(image=image)
        image_label.image = image
        canvas.create_window(400,100,window=image_label)
        
        print(("SKSL_"+unique_id),"abcd1234",AWS,OTA,PRIVATE,mod_combo.get())

        GB = 100
        download = 0
        speed = 0.2
        while (download < GB):
            time.sleep(0.001)
            myprogress['value'] += (speed / GB) * 100
            download += speed
            percent.set(str(int((download / GB) * 100)) + "%")
            root.update_idletasks()

        localtime = time.asctime(time.localtime(time.time()))
        print(localtime)

####################################################################################################################
#########################    Gmail code #########################################################
 
        msg = EmailMessage()
        msg['Subject'] = f"Skroman Device ({ESP_NO,unique_id,POP,mod_combo.get(),device_combo.get()})"
        msg['From'] = 'Skroman Production'
        msg['To'] =  'ns9625856@gmail.com'

        with open((f"{file_name}"),"rb") as f:
            file_data = f.read()
            print("file send",file_data)
            filetype = imghdr.what(f.name)
            file_name_img = f.name
            print("File name is",file_name_img)
            msg.add_attachment(file_data, maintype="image", subtype=filetype, filename=file_name_img)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
             server.login("ns9625856@gmail.com","mqujcgmpcqyjdhzh")
             server.send_message(msg)
        print("mail sent")

####################################################################################################################

       
        zip_object = zip((f"{ESP_NO}"),(f"{unique_id}"), (f"{POP}"),localtime,mod_combo.get())

        esp_count = 0
        with open ('C:\\esp\\esp-idf\\amol_codes\\excelbackup.csv','a')as csvfile:
          
             fieldnames = ['ESP_NO','unique_id','POP','ModelNo','TIME']
             thewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)

          
             d = {'ESP_NO':(f"{ESP_NO}"),'unique_id':(f"{unique_id}"),'POP':(f"{POP}"),'ModelNo':mod_combo.get(),'TIME':localtime}
             thewriter.writerow(d)

        csvfile.close()
      
        subprocess.call(['cmd','./burn_23000.sh'])


    except ValueError:
        messagebox.showerror("showerror","Enter the ESP NO  ")

###############################################333

def generate_Mood_Switch():
    try:
        int(name_entry1.get())
        ESP_NO = name_entry1.get()
        unique_id = name_entry2.get()
        POP = name_entry3.get()
        AWS = name_entry4.get()
        OTA = name_entry5.get()
        PRIVATE = name_entry6.get()

        file_name12=("ModelNo: " + mod_combo.get())
        file_name2=("ESP NO: "+ (f"{ESP_NO}"))
        file_name3=("unique_id: " +(f"{unique_id}") )
        file_name4=("POP: "+ (f"{POP}"))
        file_name66 = ("Device Type: "+ device_combo.get())
      
        filename1 = {"ModelNo":mod_combo.get(),
                      "ESP_NO":(f"{ESP_NO}"),
                     "unique_id":(f"{unique_id}"),
                     "POP":(f"{POP}"),
                     "DeviceType":device_combo.get()
                    }
        filename5 = json.dumps(filename1)
        my_list1.insert(END,file_name12)
        my_list1.insert(END,file_name2)
        my_list1.insert(END,file_name3)
        my_list1.insert(END,file_name4)
        my_list1.insert(END,file_name66)
        url = pyqrcode.create(filename5)

       
        file_name = (f"{unique_id}")+".png"
        url.png(file_name,scale=3)
      
        image = ImageTk.PhotoImage(Image.open(file_name))
        image_label = Label(image=image)
        image_label.image = image
        canvas.create_window(400,100,window=image_label)
       
        print(("SKSL_"+unique_id),"abcd1234",AWS,OTA,PRIVATE,mod_combo.get())

        GB = 100
        download = 0
        speed = 0.2
        while (download < GB):
            time.sleep(0.001)
            myprogress['value'] += (speed / GB) * 100
            download += speed
            percent.set(str(int((download / GB) * 100)) + "%")
            root.update_idletasks()

        localtime = time.asctime(time.localtime(time.time()))
        print(localtime)


####################################################################################################################
################################## Gmail code ######################################################
 
        msg = EmailMessage()
        msg['Subject'] =f"Skroman Device ({ESP_NO,unique_id,POP,mod_combo.get(),device_combo.get()})"
        msg['From'] = 'Skroman Production'
        msg['To'] =  'ns9625856@gmail.com'

        with open((f"{file_name}"),"rb") as f:
            file_data = f.read()
            print("file send",file_data)
            filetype = imghdr.what(f.name)
            file_name_img = f.name
            print("File name is",file_name_img)
            msg.add_attachment(file_data, maintype="image", subtype=filetype, filename=file_name_img)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
             server.login("ns9625856@gmail.com","mqujcgmpcqyjdhzh")
             server.send_message(msg)
        print("mail sent")

####################################################################################################################
        
        zip_object = zip((f"{ESP_NO}"),(f"{unique_id}"), (f"{POP}"),localtime,mod_combo.get())

        esp_count = 0
        with open ('C:\\esp\\esp-idf\\amol_codes\\excelbackup.csv','a')as csvfile:
           
             fieldnames = ['ESP_NO','unique_id','POP','ModelNo','TIME']
             thewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)

           
             d = {'ESP_NO':(f"{ESP_NO}"),'unique_id':(f"{unique_id}"),'POP':(f"{POP}"),'ModelNo':mod_combo.get(),'TIME':localtime}
             thewriter.writerow(d)

        csvfile.close()
       
        subprocess.call(['cmd','./burn_23000.sh'])

      

    except ValueError:
        messagebox.showerror("showerror","Enter the ESP NO  ")



        
######################################333

canvas = Canvas(root, width=400, height=600, bg = "#e3dac9")
canvas.pack()




my_list1 = Listbox(root, height=5, width=35)
canvas.create_window(360,280,window = my_list1)


name_label1 = Label(root, text="ESP NO:", bg ="#f4bbff")
name_label2 = Label(root, text="UNIQUE ID:",bg ="#f4bbff")
name_label3 = Label(root, text="POP:", bg ="#f4bbff")
name_label4 = Label(root, text="AMAZONROOTCA1:", bg ="#f4bbff")
name_label5 = Label(root, text="CERTIFICATION.PEM:", bg ="#f4bbff")
name_label6 = Label(root, text="PRIVATE.PEM", bg ="#f4bbff")

canvas.create_window(-2,40, window=name_label1)
canvas.create_window(-2,70, window=name_label2)
canvas.create_window(-2,100, window=name_label3)
canvas.create_window(-35,140, window=name_label4)
canvas.create_window(-35,180, window=name_label5)
canvas.create_window(-35,220, window=name_label6)


name_entry1 = Entry(root, text=ESP_NO)
name_entry2 = Entry(root, text= unique_id)
name_entry3 = Entry(root, text=POP)
name_entry4 = Entry(root)
name_entry5 = Entry(root)
name_entry6 = Entry(root)


canvas.create_window(90,40, window=name_entry1)
canvas.create_window(90,70, window=name_entry2)
canvas.create_window(90,100, window=name_entry3)

button = Button(text="Browse", bg="white",command = click_1, width=17)
canvas.create_window(90,140, window=button)


button = Button(text="Browse", bg="white", command = click_2, width=17)
canvas.create_window(90,180, window=button)


button = Button(text="Browse", bg="white",command=click_3, width=17)
canvas.create_window(90,220, window=button)


button = Button(text="GET DATA", bg="#e8f48c", command=parse )
canvas.create_window(-46, 270, window=button)


canvas.create_window(-30, 270, window=button)
button = Button(text="EEPROM", bg="#d14d4d", command=eeprom_func )
canvas.create_window(35, 270, window=button)

button = Button(text="BURN 4/6/8 MOD", bg="#f6eabe", command=generate)
canvas.create_window(143, 270, window=button)

button = Button(text="BURN 2 MOD", bg="#C0C0C0",command=generate_2mod)
canvas.create_window(60, 320, window=button)

button = Button(text="Mood Switch", bg="#00FFFF", command=generate_Mood_Switch)
canvas.create_window(-50, 320, window=button)

button = Button(text="EXIT", bg="#ff7070", command=root.destroy)
canvas.create_window(153, 320, window=button)

button = Button(text="DELETE", bg="#add8e6",command=delete_listbox)
canvas.create_window(355, 340, window=button)











root.mainloop()
