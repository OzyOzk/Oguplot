from PlotWindow import PlotWindow
from SerialDevice import SerialDevice
from PyQt5.QtWidgets import QApplication
from math import ceil
from numpy import zeros
import sys
from PyQt5.QtCore import QTimer

class Main:

    dt = 2
    elementCount = 0
    view = 500
    bufferSize = 2*500
    maxPlotCount = 3
    sampleSize = 3

    plotColours = ['r', 'g', 'b']
    LegendFields = ['Data 1', 'Data 2', 'Data 3']
    curveContainer = list()

    readyToPlot = False
    XaxisValue = 0
    buffers = zeros((maxPlotCount, bufferSize+1), float)

    def __init__(self):
        self.window = PlotWindow()
        self.device = SerialDevice()
        # When Poll is clicked, call find_device from SerialDevice object and pass to it
        # the text from the line edit widget in PlotWidget object
        self.window.b1.clicked.connect(self.pollButtonMethod)

    def closePort(self):
        self.device.close()

    def closeApp(self):
        self.device.close()
        sys.exit()

    def pollButtonMethod(self):
        if self.device.find_device(self.window.t1.text(), self.window.t1.text()):
            self.device.open()
            self.findElementCount()
            print("element count: ", self.elementCount)
            for x in range(self.elementCount):
                self.curveContainer.append(self.window.p1.plot(pen=self.plotColours[x], name=self.LegendFields[x], width=0.01))
            self.readyToPlot = True

    def findElementCount(self):
        total = 0
        for x in range(self.sampleSize):
            csv = self.device.readline().decode().split(',')
            total += len(csv)
        self.elementCount = int(ceil(total/self.sampleSize))

    def shiftPlot(self, buffer, csv):
        i = buffer[self.bufferSize]
        buffer[i] = buffer[i+self.view] = csv
        buffer[self.bufferSize] = i = (i+1) % self.view
        return i

    def setData(self, curve_container, buffer, element):
        curve_container.setData(buffer[element:element+self.view])
        curve_container.setPos(self.XaxisValue, 0)

    def updatePlot(self):
        if self.readyToPlot:
            print("Ready to plot")
            csv = self.device.readline().decode().split(',')
            self.XaxisValue += 1
            if len(csv) == self.elementCount:
                print("up1 ", len(csv))
                for el in range(self.elementCount):
                    print("el is ", el,"csv0 is ", csv[0])
                    self.setData(self.curveContainer[el], self.buffers[el], self.shiftPlot(self.buffers[el], csv[el]))
                    print("set Data Success")
            app.processEvents()


if not QApplication.instance():
    app = QApplication([])
else:
    app = QApplication.instance()

program = Main()

timer = QTimer()
timer.timeout.connect(program.updatePlot)
timer.start(2)
timer.setInterval(2)
program.window.show()
app.exec_()
