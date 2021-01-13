import Tkinter as tk
from Tkinter import*
from PIL import ImageTk,Image
from drawnow import *
import serial
import datetime

root= tk.Tk()


serialArduino = serial.Serial('COM44', 9600)
canvas1 = tk.Canvas(root, width = 800, height = 270)
canvas1.pack()
image=ImageTk.PhotoImage(Image.open("D:\HP\file\\masfu.jpg"))#tempat file gambar di sesuaikan dengan direktori

def showImage():
    
    canvas1.create_image(20,45,anchor=NW,image=image)
    label1 = tk.Label(root, text='RFID INTERFACE')
    label1.config(font=('Arial', 20))
    canvas1.create_window(400, 20, window=label1)
    

    now = datetime.datetime.now()
    day = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")


    label1 = tk.Label(root, text='NAMA :')
    label1.config(font=('Arial', 12))
    canvas1.create_window(250, 70, window=label1)

    label1 = tk.Label(root, text='MUHAMMAD MASHFUKH')
    label1.config(font=('Arial', 12))
    canvas1.create_window(380, 70, window=label1)

    label1 = tk.Label(root, text='TTL :')
    label1.config(font=('Arial', 12))
    canvas1.create_window(240, 100, window=label1)

    label1 = tk.Label(root, text='22/01/1998')
    label1.config(font=('Arial', 12))
    canvas1.create_window(325, 100, window=label1)

    label1 = tk.Label(root, text='ID :')
    label1.config(font=('Arial', 12))
    canvas1.create_window(236, 130, window=label1)

    label1 = tk.Label(root, text=temp_c)
    label1.config(font=('Arial', 12))
    canvas1.create_window(325, 130, window=label1)

    label1 = tk.Label(root, text='TIME :')
    label1.config(font=('Arial', 12))
    canvas1.create_window(245, 160, window=label1)

    label1 = tk.Label(root, text=hour)
    label1.config(font=('Arial', 12))
    canvas1.create_window(316, 160, window=label1)

    label1 = tk.Label(root, text='ENTER',bg = "white")
    label1.config(font=('Arial', 25))
    canvas1.create_window(650, 120, window=label1)
while True:
    valueRead = serialArduino.readline()    
    string_n = valueRead.decode()# read a byte string  # decode byte string into Unicode  
    string = string_n.rstrip()
    temp_c = string
    print(valueRead)
    if temp_c == "67 6e 6a 63":
        drawnow(showImage)
        
    #######################################################
        
root.mainloop()
