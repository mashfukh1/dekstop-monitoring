import Tkinter as tk
from Tkinter import*
from PIL import ImageTk,Image
from drawnow import*
import serial
from itertools import count
import matplotlib.pyplot as plt
import datetime

root= tk.Tk()
index = count()
canvas1 = tk.Canvas(root, width = 800, height = 270)

image=ImageTk.PhotoImage(Image.open("D:\HP\pakbeni\TKK_POLIJE\PYTHON PROGRAM\\LOGO.png"))#tempat file gambar di sesuaikan dengan direktori
canvas1.create_image(700,10,anchor=NW,image=image)

values = []
valuesA = []

plt.ion()
cnt=0

serialArduino = serial.Serial('COM52', 9600)
canvas1.pack()

  
def plotValues():
    plt.style.use('fivethirtyeight')
    plt.title('DHT SENSOR')
    plt.grid(True)
    plt.tight_layout()
    plt.plot(values, "b-",label='kelembaban')
    plt.legend()
    plt.twinx()
    plt.plot(valuesA, 'r-',label='suhu')
    plt.legend()
    now = datetime.datetime.now()
    day = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")
    
    label1 = tk.Label(root, text='GRAPHICAL USER INTERFACE')
    label1.config(font=('Arial', 25))
    canvas1.create_window(400, 50, window=label1)

    label1 = tk.Label(root, text=hour)
    
    label1.config(font=('Arial', 35))
    canvas1.create_window(400, 150, window=label1)

    label1 = tk.Label(root, text=day)
    label1.config(font=('Arial', 12))
    canvas1.create_window(400, 190, window=label1)

    label1 = tk.Label(root, text='TIME')
    label1.config(font=('Arial', 10))
    canvas1.create_window(400, 112, window=label1)

    #######################################################
    label1 = tk.Label(root, text=temp_c, bg = "white")
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 100, window=label1)
       

    label1 = tk.Label(root, text='KEEMBABAN:')
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 130, window=label1)
    label1.place(x=0, y=87)

    label1 = tk.Label(root, text=temp_d, bg = "white")
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 130, window=label1)

    label1 = tk.Label(root, text='SUHU :')
    label1.config(font=('Arial', 10))
    canvas1.create_window(140, 120, window=label1)
    label1.place(x=0, y=117)

def clear_charts():
    bar1.get_tk_widget().pack_forget()
    bar2.get_tk_widget().pack_forget()
    
for i in range(0,26):
    values.append(0)

    
while True:
    while (serialArduino.inWaiting()==0):
        pass
    valueRead = serialArduino.readline()    
    string_n = valueRead.decode()# read a byte string  # decode byte string into Unicode  
    string = string_n.rstrip()
    parsing = string.split(',',2)
    temp_c = parsing[0] #SUHU
    temp_d = parsing[1] #KELEMBABAN
    print(valueRead)
    #check if valid value can be casted
    try:
        valueInInt = temp_c
        valueInIntA = temp_d
        values.append(valueInInt)
        valuesA.append(valueInIntA)
        drawnow(plotValues)
    except ValueError:
        print "Invalid! cannot cast"
            
 
root.mainloop()
