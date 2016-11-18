from PyQt4.QtGui import *
import sys

class main(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.resize(500, 600)

        self.bg = QLabel(self)
        self.bg.resize(self.size())

        self.slider = QSlider(self)
        self.slider.sliderMoved.connect(self.printer)
        self.slider.move(20, 20)
        self.slider.setFixedSize(400, 100)
        self.slider.setOrientation(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)

    def printer(self):
        print self.slider.value()

app = QApplication(sys.argv)
window = main()
window.show()
sys.exit(app.exec_())