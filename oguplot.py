#!/usr/bin/env python
#sudocode

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

p6 = win.addPlot(title="Updating plot")
p6.setRange(yRange=[-18000,18000])
curve = p6.plot(pen='b')
data = [0]

def update():
    global curve, data
    line = ser.readline()
    data.append(float(line))
    xdata = np.array(data[-500:], dtype='float32')
    curve.setData(xdata)
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
