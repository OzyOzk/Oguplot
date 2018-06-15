#!/usr/bin/env python
#sudocode
'''
Need to add feature to split line into three components
and display on same graph
'''

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
##======================================================

import serial.tools.list_ports
import time
controller = serial.Serial

targetsn = "9553034373435110E020"



ports = serial.tools.list_ports.comports()

for p in ports:
	print (p.serial_number)
	if p.serial_number == 9553034373435110E020:
		p.device

ser = serial.Serial(p.device, 9600, timeout=1)

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Ogu-plotter")
win.resize(1000,600)

pg.setConfigOptions(antialias=True)

p6 = win.addPlot(title="Raw accellerometer data")
p6.setRange(yRange=[-18000,18000])
curve1 = p6.plot(pen='y')

curve2 = p6.plot(pen='g')

data1 = [0]
data2 = [0]
x=0
def update():
    global curve1, curve2, data1, data2, x
    line = ser.readline()
    csv = line.decode().split(',')
    if len(csv) == 2:	    
	    set1 = csv[0]
	    set2 = csv[1]
	    data1.append(float(set1))
	    data2.append(float(set2))
	    print (len(data1), len(data2))
	    xdata1 = np.array(data1[-500:], dtype='float32')
	    xdata2 = np.array(data2[-500:], dtype='float32')
	    curve1.setData(xdata1)
	    x += 1
	    curve1.setPos(x, 0)
	    curve2.setData(xdata2)
	    curve2.setPos(x, 0)
	    app.processEvents()


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

'''
	print p.vid
	print p.pid
	print p.device
'''
