import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # creating tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tap_open_on_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_change)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.setCentralWidget(self.tabs)

        # creating navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        bck_btn = QAction('Back', self)
        bck_btn.triggered.connect(self.tabs.back)
        navbar.addAction(bck_btn)

        fwd_btn = QAction('Forward', self)
        fwd_btn.triggered.connect(self.tabs.forward)
        navbar.addAction(fwd_btn)

        rld_btn = QAction('Reload', self)
        rld_btn.triggered.connect(self.tabs.reload)
        navbar.addAction(rld_btn)

        hm_btn = QAction('Home', self)
        hm_btn.triggered.connect(self.navigate_home)
        navbar.addAction(hm_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.tabs.urlchanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.tabs.ser