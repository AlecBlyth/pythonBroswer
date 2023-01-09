from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class webBrowser():

    def __init__(self):

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

        self.exeBtn.clicked.connect(lambda: self.navigate(self.urlBar.toPlainText()))
        self.backBtn.clicked.connect(self.browser.back)
        self.forBtn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://github.com/AlecBlyth"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.urlBar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = webBrowser()
app.exec_()



