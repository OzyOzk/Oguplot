# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore
import serial.tools.list_ports
import pyqtgraph as pg
import numpy as np
import sys
"""
Created on Thu Jan 18 14:38:46 2018

@author: OzyOzk
"""

"""
If you are on a windows machine, after succesfully running the code once, if you
terminated and run again, you will get the following error

SerialException: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)

You need to either reset your Kernel or delete all environment variables. On Spyder,
this can be done in the Ipython console. Reset is inside the options menu on the top 
right of the console (Cog symbol). Remove all variables is to the left of the Cog by
the stop button.

Once I find a proper solution I will update the code. 
"""


ser = None
dt = 5  # Time delta in milliseconds

#serial_number = "9553034373435110E020"


def find_device(sn):
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if p.serial_number == sn:
            comport = p.device
            print("Found device on", p.device)
            return comport
    return "Not found"


def connect_to_device(comport):
    return serial.Serial(comport, 9600, timeout=1)


def poll_button(lineedit):
    return(lineedit.text())


def qlewrapper():
    serial_number = poll_button(t1)
    comport = find_device(serial_number)
    if(comport == "Not found"):
        return
    global ser
    ser = connect_to_device(comport)
    print(comport)


def close_port():
    global ser
    if (ser != None):
        ser.close()


def close_app():
    close_port()
    sys.exit()

# for Spyder. When you close your window, the QtApplicaiton instance is
# still there after being created once. Therefore check if a Qt instance
# already exists, if it does, then use it, otherwise, create new instance


if not QtGui.QApplication.instance():
    app = QtGui.QApplication([])
else:
    app = QtGui.QApplication.instance()

win = QtGui.QWidget()
win.setWindowTitle("OguPlot")
win.resize(1000, 600)
layout = QtGui.QGridLayout()
win.setLayout(layout)

b1 = QtGui.QPushButton("Poll")
b1.clicked.connect(qlewrapper)

b2 = QtGui.QPushButton("Close port")
b2.clicked.connect(close_port)

t1 = QtGui.QLineEdit("Enter Device Serial")

p1 = pg.PlotWidget()
p1.setRange(yRange=[-18000, 18000])
p1.addLegend()
p1.showGrid(x=True, y=True, alpha=0.8)
p1.setLabel('left', 'Amplitude (16bit Signed)')

curve1 = p1.plot(pen='y', name="Data 1")
curve2 = p1.plot(pen='g', name="Data 2")

layout.addWidget(p1, 0, 0, 1, 3)
layout.addWidget(b1, 1, 0)
layout.addWidget(t1, 1, 1)
layout.addWidget(b2, 1, 2)

size = 500
buffersize = 2*500
buffer1 = np.zeros(buffersize+1, int)
buffer2 = np.zeros(buffersize+1, int)

x = 0


def update():
    global curve1, curve2, data1, data2, x, ser, size, buffersize
    if(ser != None and ser.is_open):
        line = ser.readline()
        csv = line.decode().split(',')
        x += 1
        if len(csv) == 2:

            i = buffer1[buffersize]
            buffer1[i] = buffer1[i+size] = csv[0]
            buffer1[buffersize] = i = (i+1) % size

            j = buffer2[buffersize]
            buffer2[j] = buffer2[j+size] = csv[1]
            buffer2[buffersize] = j = (j+1) % size

            curve1.setData(buffer1[i:i+size])
            curve1.setPos(x, 0)
            curve2.setData(buffer2[j:j+size])
            curve2.setPos(x, 0)
            app.processEvents()


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(dt)
timer.setInterval(dt)
# if(ser != None):
#  timer.stop()
win.show()
app.exec_()
