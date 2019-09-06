from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QPushButton, QLineEdit
import pyqtgraph as pg


class PlotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeWindow()

    def initializeWindow(self):
        # Window settings
        self.setWindowTitle("OguPlot")
        self.resize(1000, 600)
        self.gridlayout = QGridLayout()
        self.setLayout(self.gridlayout)

        # Window elements

        self.b1 = QPushButton("Poll")

        self.b2 = QPushButton("Close Port")

        self.t1 = QLineEdit("")

        self.p1 = pg.PlotWidget()
        self.p1.setRange(yRange=[-18000, 18000])
        self.p1.showGrid(x=True, y=True, alpha=0.5)
        self.p1.setLabel('left', 'Amplitude')
        self.p1.setLabel('bottom', 'Sample')
        self.p1.addLegend()

        self.gridlayout.addWidget(self.p1, 0, 0, 1, 3)
        self.gridlayout.addWidget(self.b1, 1, 0)
        self.gridlayout.addWidget(self.t1, 1, 1)
        self.gridlayout.addWidget(self.b2, 1, 2)


'''
if not QApplication.instance():
    app = QApplication([])
else:
    app = QApplication.instance()

test = PlotWindow()
app.exec_()
'''