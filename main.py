from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class webBrowser(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(webBrowser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("ABM Internet Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.urlBar = QTextEdit()
        self.urlBar.setMaximumHeight(30)

        self.exeBtn = QPushButton("Execute")
        self.exeBtn.setMaximumHeight(30)

        self.backBtn = QPushButton("<")
        self.backBtn.setMaximumHeight(30)

        self.forBtn = QPushButton(">")
        self.forBtn.setMaximumHeight(30)

        self.horizontal.addWidget(self.urlBar)
        self.horizontal.addWidget(self.exeBtn)
        self.horizontal.addWidget(self.backBtn)
        self.horizontal.addWidget(self.forBtn)

        self.browser = QWebEngineView()
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://github.com/AlecBlyth"))

        self.window.setLayout(self.layout)
        self.window.show()

app = QApplication([])
window = webBrowser()
app.exec_()



