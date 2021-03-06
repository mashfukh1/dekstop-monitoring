import time, random
import math
from collections import deque
import socket
UDP_IP = "192.168.180.25"
UDP_PORT1 = 5013
UDP_PORT2 = 5012

sock1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock1.bind((UDP_IP, UDP_PORT1))

sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock2.bind((UDP_IP, UDP_PORT2))

start = time.time()


class RealtimePlot:
    def __init__(self, axes, max_entries=100):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)
        self.axes = axes
        self.max_entries = max_entries

        self.lineplot, = axes.plot([], [], "ro-")
        self.axes.set_autoscaley_on(True)

    def add(self, x, y):
        self.axis_x.append(x)
        self.axis_y.append(y)
        self.lineplot.set_data(self.axis_x, self.axis_y)
        self.axes.set_xlim(self.axis_x[0], self.axis_x[-1] + 1e-15)
        self.axes.relim();
        self.axes.autoscale_view()  # rescale the y-axis

    def animate(self, figure, callback, interval=50):
        import matplotlib.animation as animation
        def wrapper(frame_index):
            self.add(*callback(frame_index))
            self.axes.relim();
            self.axes.autoscale_view()  # rescale the y-axis
            return self.lineplot

        animation.FuncAnimation(figure, wrapper, interval=interval)


def main():
    from matplotlib import pyplot as plt

    fig, axes = plt.subplots(2)
    display1 = RealtimePlot(axes[0])
    display2 = RealtimePlot(axes[1])
    while True:
        data1, addr = sock1.recvfrom(32)
        display1.add(time.time() - start, data1)
        data2, addr = sock2.recvfrom(32)
        display2.add(time.time() - start, data2)
        plt.pause(0.0001)


if __name__ == "__main__": main()
