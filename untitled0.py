from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import serial.tools.list_ports
import timeit

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

data1 = [0] * 500
data2 = [0] * 500
x=0

mysetup = "from math import sqrt"

def testshift():
  line = ser.readline()
  csv = line.decode().split(',')
  if len(csv) == 2:	    
    data1.append(int(csv[1]))
    data2.append(int(csv[0]))
    data1.pop(0)
    data2.pop(0)
      
print (timeit.timeit(setup = mysetup,
                    stmt = testshift,
                    number = 60)/60)