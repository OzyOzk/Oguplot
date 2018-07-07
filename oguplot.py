# -*- coding: utf-8 -*-
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

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import serial.tools.list_ports

controller = serial.Serial

#All ports
ports = serial.tools.list_ports.comports()

serial_number = "9553034373435110E020"

#Scan all devices and queery for Serial number. 
#Attach to device if found
for p in ports:
  if p.serial_number == serial_number:
    comport = p.device
    print("Found device on", p.device)

ser = serial.Serial(comport, 9600, timeout=1)

#Serial object. Check if open. If not then open.
if not ser.isOpen():
  ser.open()
print("Port", comport, ser.isOpen())

app = QtGui.QApplication([])

pg.setConfigOptions(antialias=True)

win = pg.GraphicsWindow(title="Ogu-plotter")
win.resize(1000,600)
win.useOpenGL

p6 = win.addPlot(title="Raw accellerometer data")
p6.setRange(yRange=[-18000,18000])
p6.addLegend()
p6.showGrid(x = True, y = True, alpha = 0.8) 
p6.setLabel('left', 'Amplitude (16bit Signed)')

curve1 = p6.plot(pen='y', name = "Accelerometer Y")
curve2 = p6.plot(pen='g', name = "Accelerometer X")

data1 = [0] * 500
data2 = [0] * 500
x=0

def update():
  global curve1, curve2, data1, data2, x
  line = ser.readline()
  csv = line.decode().split(',')
  if len(csv) == 2:	    
    data1.append(int(csv[1]))
    data2.append(int(csv[0]))
    data1.pop(0)
    data2.pop(0)
    xdata1 = np.array(data1[-500:], dtype='int')
    xdata2 = np.array(data2[-500:], dtype='int')
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
