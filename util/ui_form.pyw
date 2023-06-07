# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 261)
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.export_path = QLineEdit(self.centralwidget)
        self.export_path.setObjectName(u"export_path")
        self.export_path.setGeometry(QRect(20, 70, 331, 21))
        self.master_path = QLineEdit(self.centralwidget)
        self.master_path.setObjectName(u"master_path")
        self.master_path.setGeometry(QRect(20, 120, 331, 21))
        self.browseButton_1 = QPushButton(self.centralwidget)
        self.browseButton_1.setObjectName(u"browseButton_1")
        self.browseButton_1.setGeometry(QRect(370, 70, 80, 21))
        self.browseButton_2 = QPushButton(self.centralwidget)
        self.browseButton_2.setObjectName(u"browseButton_2")
        self.browseButton_2.setGeometry(QRect(370, 120, 80, 21))
        self.runButton = QPushButton(self.centralwidget)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setGeometry(QRect(400, 190, 80, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 9, 501, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
        self.menuQR_Member_Detect = QMenu(self.menubar)
        self.menuQR_Member_Detect.setObjectName(u"menuQR_Member_Detect")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuQR_Member_Detect.menuAction())

        self.retranslateUi(MainWindow)
        self.browseButton_1.clicked.connect(self.export_path.clear)
        self.browseButton_2.clicked.connect(self.master_path.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.export_path.setText(QCoreApplication.translate("MainWindow", u"Insert Path To Future Trips Export File", None))
        self.master_path.setText(QCoreApplication.translate("MainWindow", u"Insert Path to Master Member List", None))
        self.browseButton_1.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.browseButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"QR Member Detector", None))
        self.menuQR_Member_Detect.setTitle(QCoreApplication.translate("MainWindow", u"QR Member Detect", None))
    # retranslateUi

