# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore
import serial.tools.list_ports
import pyqtgraph as pg
import numpy as np
from numpy import zeros
import sys
import math
"""
Created on Thu Jan 18 14:38:46 2018

@author: OzyOzk
"""

ser = None
dt = 2  # Time delta in milliseconds
element_count = 0

view = 500
buffersize = 2*view  # it's a double buffer
max_plot_count = 3

sample_size = 3

colours = ['r', 'g', 'b']
plot_names = ['Data 1', 'Data 2', 'Data 3']

#serial_number = "9553034373435110E020"


# to contain the information for the plots
buffers = zeros((max_plot_count, buffersize+1), int)
curve_container = list()


def find_device(sn):
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if p.serial_number == sn:
            comport = p.device
            print("Found device on", p.device)
            return comport
    return '!'


def connect_to_device(comport):
    return serial.Serial(comport, 9600, timeout=1)


def poll_button(lineedit):
    return(lineedit.text())


def find_length(ser):
    global sample_size
    elements = 0
    for x in range(sample_size):
        line = ser.readline()
        csv = line.decode().split(',')
        elements += len(csv)
    return elements/sample_size


def make_curves(elements):
    global curve_container, colours, plot_names
    for x in range(elements):
        curve_container.append(
            p1.plot(pen=colours[x], name=plot_names[x], width=0.01))


def qlewrapper():
    global element_count, ser
    serial_number = poll_button(t1)
    comport = find_device(serial_number)
    if comport == '!':
        return
    ser = connect_to_device(comport)
    element_count = int(math.ceil(find_length(ser)))
    print(element_count)
    make_curves(element_count)


def shift_plot(buffer, csv):
    global view, buffersize, element_count
    i = buffer[buffersize]
    buffer[i] = buffer[i+view] = csv
    buffer[buffersize] = i = (i+1) % view
    return i


def set_data(curve_container, buffer, element):
    global view, x
    curve_container.setData(buffer[element:element+view])
    curve_container.setPos(x, 0)


def close_port():
    global ser
    if (ser != None):
        ser.close()


def close_app():
    close_port()
    sys.exit()


def update():
    global x, view, element_count, curve_container, buffers, buffersize
    if(ser != None):
        line = ser.readline()
        csv = line.decode().split(',')
        x += 1
        if len(csv) == element_count:
            for el in range(element_count):
                set_data(curve_container[el], buffers[el],
                         shift_plot(buffers[el], csv[el]))
        app.processEvents()

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

t1 = QtGui.QLineEdit("9553034373435110E020")

p1 = pg.PlotWidget()
p1.setRange(yRange=[-18000, 18000])
p1.showGrid(x=True, y=True, alpha=0.5)
p1.setLabel('left', 'Amplitude')
p1.setLabel('bottom', 'Sample')
p1.addLegend()

layout.addWidget(p1, 0, 0, 1, 3)
layout.addWidget(b1, 1, 0)
layout.addWidget(t1, 1, 1)
layout.addWidget(b2, 1, 2)

x = 0


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(dt)
timer.setInterval(dt)
win.show()
app.exec_()
