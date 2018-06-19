import serial.tools.list_ports
controller = serial.Serial

ports = serial.tools.list_ports.comports()

for p in ports:
  print(p.serial_number)
  if p.serial_number == 9553034373435110E020:
    p.device

ser = serial.Serial(p.device, 9600)

while(True):
  line = ser.readline()
  #print(line)
  first = line.decode().split(",")[0]
  secon = line.decode().split(",")[1]
  print(first, secon)