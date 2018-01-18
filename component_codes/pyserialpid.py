#!/usr/bin/env python
#sudocode

import serial.tools.list_ports
import time
controller = serial.Serial

targetsn = "9553034373435110E020"
#usb_port = ""

ports = serial.tools.list_ports.comports()

for p in ports:
	print (p.serial_number)
	if p.serial_number == 9553034373435110E020:
		p.device

ser = serial.Serial(p.device, 9600, timeout=1)

while True:
	arduinodata = ser.readline()
	csv=arduinodata.split(",")
	print (csv[0])

'''
	print p.vid
	print p.pid
	print p.device
'''
