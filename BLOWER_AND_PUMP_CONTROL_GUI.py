import Tkinter
import time
import serial

ser = serial.Serial ('COM44',9600) #Used for Pro Mini

class gui(Tkinter.Tk):
        def __init__(self,parent):
                Tkinter.Tk.__init__(self,parent)
                self.parent = parent
                #ser = serial.Serial ('/dev/ttyACM0',9600)
                self.initialize()
                
        def initialize(self):
                self.grid()

                #self.entry = Tkinter.Entry(self)
                #self.entry.grid(column=0, row=0, sticky='EW')
                
                Label = Tkinter.Label(self, text='.          .')
                Label.grid(column=1, row=0)

                Label = Tkinter.Label(self, text='.          .')
                Label.grid(column=1, row=14)

                button = Tkinter.Button(self, text="Turn BLOWER off!",
                                        command=self.OnButtonClick)
                button.grid(column=0, row=1)
                
                button = Tkinter.Button(self, text="Turn BLOWER on!",
                                        command=self.OffButtonClick)
                button.grid(column=2, row=1)

                button = Tkinter.Button(self, text="Turn PUMP off!",
                                        command=self.OnButtonClickA)
                button.grid(column=0, row=18)
                
                button = Tkinter.Button(self, text="Turn PUMP on!",
                                        command=self.OffButtonClickA)
                button.grid(column=2, row=18)


        def OnButtonClick(self):
                print("BLOWER OFF")
                ser.write("Y")
                Label = Tkinter.Label(self, text='BLOWER OFF')
                Label.grid(column=1, row=0)
        def OffButtonClick(self):
                print("BLOWER ON")
                ser.write("N")
                Label = Tkinter.Label(self, text='BLOWER ON')
                Label.grid(column=1, row=0)
        def OnButtonClickA(self):
                print("PUMP OFF")
                ser.write("O")
                Label = Tkinter.Label(self, text='PUMP OFF')
                Label.grid(column=1, row=14)
        def OffButtonClickA(self):
                print("PUMP ON")
                ser.write("P")
                Label = Tkinter.Label(self, text='PUMP ON')
                Label.grid(column=1, row=14)
                
if __name__ == "__main__":
        app = gui(None)
        app.title('CONTROL BLOWER AND PUMP')
        app.mainloop()
