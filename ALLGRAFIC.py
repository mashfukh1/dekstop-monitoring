import Tkinter as tk
from Tkinter import*
import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
import random
import datetime
from PIL import ImageTk,Image
import paho.mqtt.client as mqtt #import the client1

broker_address="127.0.0.1" 
client = mqtt.Client("P1")
client.connect(broker_address)

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 200, height = 810)
image=ImageTk.PhotoImage(Image.open("D:\HP\pakbeni\TKK_POLIJE\\PYTHON PROGRAM\LOGO.png"))#tempat file gambar di sesuaikan dengan direktori
canvas1.create_image(57,25,anchor=NW,image=image)
canvas1.pack()
serialArduino = serial.Serial('COM44', 9600)

suhu = []
kelembapan = []
gas = []
uv = []
soil = []
plt.ion()
cnt = 0

def makeFig():
    
    ####################   PLOTING BLOK   ####################
    plt.subplot(5,1,1)
    plt.ylim(0,400)
    plt.title('bismillah plot A')
    plt.grid(True)
    plt.ylabel('temp F')
    plt.plot(suhu, 'g-', label = 'suhu')
    plt.legend(loc='upper right')

    plt.subplot(5,1,2)
    plt.ylim(0,400)
    plt.title('bismillah plot B')
    plt.grid(True)
    plt.ylabel('pressure')
    plt.plot(kelembapan, 'r-', label = 'kelembapan')
    plt.legend(loc='upper right')
    plt.ticklabel_format(useOffset=False)
    plt.tight_layout()

    plt.subplot(5,1,3)
    plt.ylim(0,400)
    plt.title('bismillah plot C')
    plt.grid(True)
    plt.ylabel('gas')
    plt.plot(gas, 'b-', label = 'gas')
    plt.legend(loc='upper right')
    plt.ticklabel_format(useOffset=False)
    plt.tight_layout()
    
    plt.subplot(5,1,4)
    plt.ylim(0,400)
    plt.title('bismillah plot D')
    plt.grid(True)
    plt.ylabel('soil')
    plt.plot(soil, 'y-', label = 'soil')
    plt.legend(loc='upper right')
    plt.ticklabel_format(useOffset=False)
    plt.tight_layout()

    plt.subplot(5,1,5)
    plt.ylim(0,400)
    plt.title('bismillah plot E')
    plt.grid(True)
    plt.ylabel('uv')
    plt.plot(uv,'m-', label = 'uv')
    plt.legend(loc='upper right')
    plt.ticklabel_format(useOffset=False)
    plt.tight_layout()

    now = datetime.datetime.now()
    day = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")

    ##########################################################

    

    ####################   TKINTER BLOK   ####################
    
    label1 = tk.Label(root, text='SPD GUI')
    label1.config(font=('Arial', 25))
    canvas1.create_window(100, 150, window=label1)

    label1 = tk.Label(root, text=hour)
    
    label1.config(font=('Arial', 35))
    canvas1.create_window(100, 250, window=label1)

    label1 = tk.Label(root, text=day)
    label1.config(font=('Arial', 12))
    canvas1.create_window(100, 290, window=label1)

    label1 = tk.Label(root, text='TIME')
    label1.config(font=('Arial', 10))
    canvas1.create_window(100, 212, window=label1)

    label1 = tk.Label(root, text=random.randrange(0,400), bg = "white")
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 430, window=label1)
       

    label1 = tk.Label(root, text='>GAS :')
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 330, window=label1)
    label1.place(x=0, y=540)


    label1 = tk.Label(root, text=random.randrange(0,400), bg = "white")
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 460, window=label1)

    label1 = tk.Label(root, text='>SOIL MOISTURE :')
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 320, window=label1)
    label1.place(x=0, y=417)
    

    label1 = tk.Label(root, text=random.randrange(0,400), bg = "white")
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 490, window=label1)

    label1 = tk.Label(root, text='>ULTRAVIOLET :')
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 350, window=label1)
    label1.place(x=0, y=448)

    label1 = tk.Label(root, text=random.randrange(0,400), bg = "white")
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 520, window=label1)

    label1 = tk.Label(root, text='>SUHU :')
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 380, window=label1)
    label1.place(x=0, y=478)

    label1 = tk.Label(root, text=random.randrange(0,40), bg = "white")
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 550, window=label1)

    label1 = tk.Label(root, text='>KELEMBABAN :')
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 410, window=label1)
    label1.place(x=0, y=510)

    label1 = tk.Label(root, text='Connected', bg = "white")
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 650, window=label1)

    label1 = tk.Label(root, text='MQTT :')
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 610, window=label1)
    label1.place(x=0, y=640)

    ##########################################################
    
for i in range(0,26):
    suhu.append(0)
    gas.append(0)
    kelembapan.append(0)
    uv.append(0)
    soil.append(0)
    
while True:
    valueRead = serialArduino.readline()    
    string_n = valueRead.decode()# read a byte string  # decode byte string into Unicode  
    string = string_n.rstrip()
    parsing = string.split(',',5)
        
    temp_c = parsing[0] #GAS
    temp_d = parsing[1] #soil
    temp_e = parsing[2] #UV
    temp_f = parsing[3] #suhu
    temp_g = parsing[4] #kelembaban

    
    #suhu.append(str(temp_c))
    kelembapan.append(str(temp_c))
    #gas.append(str(temp_c))
    #uv.append(str(temp_c))
    #soil.append(str(temp_c))
    drawnow(makeFig)

    #client.publish("SPD/SUHU",random.randrange(0,400))#publish
    #client.publish("SPD/UV",random.randrange(0,400))#publish
    #client.publish("SPD/SOIL",random.randrange(0,400))#publish
    #client.publish("SPD/GAS",random.randrange(0,400))#publish
    #client.publish("SPD/KELEMBABAN",random.randrange(0,400))#publish
