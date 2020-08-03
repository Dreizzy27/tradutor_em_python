import tradutorpython
import sys
import googletrans
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Main(QtWidgets.QMainWindow, tradutorpython.Ui_Dialog):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.setupUi(self)
        self.linguas()
        self.pushButton.clicked.connect(self.trad)

    def linguas(self):
        for x in googletrans.LANGUAGES.values():
            self.comboBox.addItem(x.capitalize())
            self.comboBox_2.addItem(x.capitalize())

    def trad(self):
        try:
            t1 = self.textEdit.toPlainText()
            l1 = self.comboBox.currentText()
            l2 = self.comboBox_2.currentText()

            trad2 = googletrans.Translator()
            trad3 = trad2.translate(t1, scr=l1, dest=l2)
            self.textEdit_2.setText(trad3.text)
        except Exception as h:
            self.msg_erro(h)

    def msg_erro(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("ERRO")
        msg.setIcon(QMessageBox.Critical)
        msg.setText(str(text))
        msg.exec_()


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = Main()
    app.show()
    a.exec()
