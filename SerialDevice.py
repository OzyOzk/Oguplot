import serial
import serial.tools.list_ports as lp


class SerialDevice(serial.Serial):

    def __init__(self):
        super().__init__()
        self.baudrate = 9600
        self.timeout = 1

    def find_device(self, target_serial, target_pid):
        ports = lp.comports()
        for p in ports:
            if str(p.pid) == target_pid or p.serial_number == target_serial:
                self.port = p.device
                print("device found")
                return True
        return False

    @staticmethod
    def list_connected_devices():
        ports = lp.comports()
        for p in ports:
            print(p.name, " ", p.serial_number, " ", p.pid, " ", p.name)


'''
print("device found")
print("find device called. values are ", target_serial, " ", target_serial)

test = SerialDevice()
test.find_device("24577", "24577")

while True:
    
    test.open()
    line = test.readline().decode()
    print(line)
    '''