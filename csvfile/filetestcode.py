import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports 
from tkinter import scrolledtext
from time import sleep
import csv
from tabulate import tabulate
import requests
import json
import pandas as pd
import re
import re
import os
import time
from tkinter import *
from tkinter import ttk
import json
import time
import threading
import numpy as np
import matplotlib.pyplot as plt 
import tkinter as tk
from tkinter import ttk
import pandas as pd                     
import json
from io import StringIO
#from tabulate import tabulate


HEIGHT = 800
WIDTH = 800
baudRate = 115200
ser = None 
after_id = None
 
t1 = None
t2 = None
dropdown_value = None
 

listobj = []



def serial_ports():
    return serial.tools.list_ports.comports()


def on_select(event=None):
    global ser
    global mytext
    #global index = 1
    COMPort = cb.get()
    string_separator = "="

    COMPort = COMPort.split(string_separator,1)[0] 
    COMPort = COMPort[:-1] 
    ser = serial.Serial(port = 'COM5', baudrate='115200', timeout=0)
    ser.flush();

    print(ser.readline().decode().rstrip('\r\n').split(","))



def readSerial():

    if  reading_serial:

        while (ser_bytes := ser.readline()):
        

            try:
                
                text.insert("end", ser_bytes.decode('utf-8'))
               # text.insert("end", "nikhil")
                mytext = text.get('1.0', 'end')
               # print(mytext)
                if vsb.get()[1]==1.0: 
                    text.see("end") 
                        
                data =  ser_bytes.decode('utf-8')
                #json_all = json.loads(data)
                #print("load data is here..", json_all)
                # print("data us ", data)
                #df = pd.DataFrame(data)
                #df.to_excel('a.xlsx')
                with open('myfile.json', 'a') as f:
                    f.write(data)
                    f.close()
                #with open('shinde1234.json', 'a') as f:
                   # listobj = json.load(f)
                #print("list object is here.", listobj)
                #print(type(listobj))

                #listobj.append(data)
                #print("list append data object .", listobj)

                #with open('Shinde1234.json', 'a')as json_file:
                #    json.dump(listobj, json_file)
                #print("data append sucessfully in list")

                #with open('aa11234.json','a') as f:
                 #       f.write(data)
                  #      f.close()

                #with open('Shinde.json', 'w')as json_file:
                 #   json.dumpjson_file)
                #print("data append sucessfully in list")


                #with open("test_data.csv","a") as f:
                 #   writer = csv.writer(f,delimiter=",")
                  #  writer.writerow(data)

                
            except UnicodeExceptionError:
                print("check code")
    root.after(50,readSerial)

def csv_file():

    f = open('myfile.json')
    data = json.load(f)

    column = list(map(lambda i: i, data[0]))
    row = list(map(lambda i: i , data))

    f.close()

    with open("NikhilShinde12345.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=column)
        writer.writeheader()
        writer.writerows(row) 
        f.close()


    





def dropdown_selection(*args):
   global dropdown_value
   dropdown_value = clicked.get()
   button_single['state'] = 'normal' 



def rawdata(): 

    global reading_serial    
    reading_serial = True
    button_stop['state']='normal' 
    ser.write("rf".encode())  
#    csv_file()

    readSerial()

def stopdata():       
    
    global reading_serial
    reading_serial=False
    button_stop['state']='disabled'
    ser.write("c".encode())
    root.after_cancel(after_id) 



def show():

    f = open('one.json')
    
    data = json.load(f)
    courses = list(data.keys())
    print("here is course..", courses)

    values = list(data.values())
    print("vlaues here....", values)

    fig = plt.figure(figsize = (90, 10))    
    plt.bar(courses, values, color ='maroon', 

            width = 0.4)
    

    plt.xlabel(" BATTERY PARAMNETERS")

    plt.ylabel("BATTERY VALUES")

    plt.title("BATTERY MONITOR SYSTEM")
    plt.show()



def table():

    root = tk.Tk()
    root.geometry("1400x700")
    root.title("TABLE FORMAT ")
    s = ttk.Style()
    
    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings', height=50)
    
    tree.column("# 1", anchor=CENTER, width=250)
    tree.heading("# 1", text="Sr.No.")
    tree.column("# 2", anchor=CENTER, width=250)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER, width=600)
    tree.heading("# 3", text="Value")
    tree.column("# 4", anchor=CENTER, width=200)
    tree.heading("# 4", text="Unit")

    f = open('one.json')
    data = json.load(f)
    print(data)
    datas = json.dumps(data)
    print("dump data is here ...", datas)
    print("Done reading json file")

    i = 0
    for keys, values in data.items():

        tree.insert("", "end", values=())

        i =  i+1
        if keys == 'bms_temperature_max':
            tree.insert("", "end", values=(i, keys, values, '°C'))
        elif keys == 'bms_deviceid':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'bms_temperature_min':
            tree.insert("", "end", values=(i, keys, values, '°C'))
        elif keys == 'bms_pack_capacity':
            tree.insert("", "end", values=(i, keys, values, 'AH'))
        elif keys == 'battery_voltage':
            tree.insert("", "end", values=(i, keys, values, 'V'))
        elif keys == 'battery_current':
            tree.insert("", "end", values=(i, keys, values, 'A'))
        elif keys == 'battery_soc':
            tree.insert("", "end", values=(i, keys, values, '%'))
        elif keys == 'battery_soh':
            tree.insert("", "end", values=(i, keys, values, '%'))
        elif keys == 'no_of_cells':
            tree.insert("", "end", values=(i, keys, values, 'NO'))
        elif keys == 'pack_total_capacity':
            tree.insert("", "end", values=(i, keys, values, 'V'))
        elif keys == 'cell_voltage_difference':
            tree.insert("", "end", values=(i, keys, values, 'V'))
        elif keys == 'charge_discharge_cycles':
            tree.insert("", "end", values=(i, keys, values, 'NO'))
        elif keys == 'charge_discharge_status':
            tree.insert("", "end", values=(i, keys, values, 'STATE'))
        elif keys == 'fet_charge_state':
            tree.insert("", "end", values=(i, keys, values, 'STATE'))
        elif keys == 'fet_discharge_state':
            tree.insert("", "end", values=(i, keys, values, 'STATE'))
        elif keys == 'high_voltage_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'low_voltage_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'charge_over_current_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'discharge_over_current_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'charge_high_temperature_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'charge_low_temperature_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'discharge_high_temperature_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'discharge_low_temperature_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'total_high_pressure_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'total_low_pressure_alarm':
            tree.insert("", "end", values=(i, keys, values, '-'))
        elif keys == 'cell_voltages':
            tree.insert("", "end", values=(i, keys, values, 'V'))
        elif keys == 'cell_temp':
            tree.insert("", "end", values=(i, keys, values, '°C'))
    tree.pack()


root = tk.Tk() 
root.title("VAROS BATTERY HEALTH ANALYZER")

 
canvas = tk.Canvas(root, height=1000, width=800)
canvas.pack()
 
frame1 = tk.Frame(root)
frame1.place(relx=0, rely=0.05, relheight=0.03, relwidth=1, anchor='nw') 
 
label0 = tk.Label(frame1, text="SELECT THE COM PORT ")
label0.configure(fg= 'black', font=("Comic Sans MS", 13, "bold" ))
#label0.config(font=("TkDefaultFont", 8))
label0.place(relx = 0.1, rely=0.3, relwidth=0.3, relheight=0.5)
 
 
cb = ttk.Combobox(frame1, values=serial_ports())
cb.place(relx=0.5, rely=0.5,anchor='center')
cb.bind('<<ComboboxSelected>>', on_select)

frame2 = tk.Frame(root, bd=5) 
frame2.place(relx=0, rely=0.1, relheight=0.07, relwidth=1, anchor='nw')
 
button_all = tk.Button(frame2, text="MEASURE_RAW_DATA", bg='#80c1ff', fg='red', state='normal', command=threading.Thread(target=rawdata).start)  
button_all.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ))
button_all.place(relx=0.2, rely=0.5, anchor='center')
 

button1 = tk.Button(frame2, text="TABULAR_FORMAT", bg='#80c1ff', fg='red', state='normal', command=table)
button1.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ))
button1.place(relx=0.70, rely=0.50, anchor='w')


button2 = tk.Button(frame2, text="GRAHICAL_FORMAT", bg='#80c1ff', fg='red', state='normal', command=show)
button2.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ))
button2.place(relx=0.40, rely=0.50, anchor='w')


frame3 = tk.Frame(root, bd=5) 
frame3.place(relx=0, rely=0.2, relheight=0.07, relwidth=1, anchor='nw')
 
button_stop = tk.Button(frame3, text="STOP_RAW_DATA", bg='#80c1ff', fg='red', state='disabled', command=threading.Thread(target=stopdata).start)
button_stop.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ))
button_stop.place(relx=0.2, rely=0.5, anchor='center')

button1 = tk.Button(frame3, text="CSV_FILE", bg='#80c1ff', fg='red', state='normal', command=csv_file)
button1.configure(background="#5D6D7E", fg= 'black', font=("Comic Sans MS", 13, "bold" ))
button1.place(relx=0.70, rely=0.50, anchor='w')

#button_stop.grid(padx=30,pady= 10,row=1, column=2)
frame4 = tk.Frame(root, bd=5)
frame4.place(relx=0, rely=0.3, relheight=0.09, relwidth=1, anchor='nw')
 
frame6 = tk.Frame(root, bg='#5D6D7E') 
frame6.place(relx=0.0, rely=0.4, relheight=1, relwidth=1, anchor='nw')
 
text_frame=tk.Frame(frame6)
text_frame.place(relx=0, rely=0, relheight=0.6, relwidth=1, anchor='nw')
text=tk.Text(text_frame)

text.place(relx=0, rely=0, relheight=1, relwidth=1, anchor='nw')
vsb=tk.Scrollbar(text_frame)
vsb.pack(side='right',fill='y')
text.config(yscrollcommand=vsb.set)
vsb.config(command=text.yview)
 
reading_serial=False 
 
root.mainloop() 
 


#ser.close()
