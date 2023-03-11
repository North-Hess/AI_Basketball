# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface_designPfFABS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.actionGames = QAction(MainWindow)
        self.actionGames.setObjectName(u"actionGames")
        self.actionAnalyze = QAction(MainWindow)
        self.actionAnalyze.setObjectName(u"actionAnalyze")
        self.actionUngrouped_Footage = QAction(MainWindow)
        self.actionUngrouped_Footage.setObjectName(u"actionUngrouped_Footage")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: black;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slideMenuContainer = QFrame(self.centralwidget)
        self.slideMenuContainer.setObjectName(u"slideMenuContainer")
        self.slideMenuContainer.setMaximumSize(QSize(200, 16777215))
        self.slideMenuContainer.setStyleSheet(u"background-color: rgb(252, 146, 25);")
        self.slideMenuContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.slideMenuContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slideMenuContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slideMenu = QFrame(self.slideMenuContainer)
        self.slideMenu.setObjectName(u"slideMenu")
        self.slideMenu.setMinimumSize(QSize(198, 0))
        self.slideMenu.setStyleSheet(u"")
        self.slideMenu.setFrameShape(QFrame.Shape.StyledPanel)
        self.slideMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.slideMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.topContainer = QFrame(self.slideMenu)
        self.topContainer.setObjectName(u"topContainer")
        self.topContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.topContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.topContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.appNameFrame = QFrame(self.topContainer)
        self.appNameFrame.setObjectName(u"appNameFrame")
        self.appNameFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.appNameFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.appNameFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.appNameFrame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_4.addWidget(self.appNameFrame)

        self.logoFrame = QFrame(self.topContainer)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.logoFrame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_6.addWidget(self.topContainer, 0, Qt.AlignmentFlag.AlignTop)
        
        self.menuContainer = QFrame(self.slideMenu)
        self.menuContainer.setObjectName(u"menuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuContainer.sizePolicy().hasHeightForWidth())
        self.menuContainer.setSizePolicy(sizePolicy)
        self.menuContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.menuContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.buttonContainer = QFrame(self.menuContainer)
        self.buttonContainer.setObjectName(u"buttonContainer")
        self.buttonContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttonContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.buttonContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.homeContainer = QFrame(self.buttonContainer)
        self.homeContainer.setObjectName(u"homeContainer")
        self.homeContainer.setStyleSheet(u"border: 2px solid rgb(0,0,0);")
        self.homeContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.homeContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.homeContainer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.homeButton = QPushButton(self.homeContainer)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setStyleSheet(u"border: none;")

        self.verticalLayout_9.addWidget(self.homeButton)


        self.verticalLayout_12.addWidget(self.homeContainer)

        self.uploadContainer = QFrame(self.buttonContainer)
        self.uploadContainer.setObjectName(u"uploadContainer")
        self.uploadContainer.setStyleSheet(u"border: 2px solid rgb(0,0,0);\n"
"border-bottom: none;\n"
"border-top: none;")
        self.uploadContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.uploadContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.uploadContainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.uploadButton = QPushButton(self.uploadContainer)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setStyleSheet(u"border: none;")

        self.verticalLayout_10.addWidget(self.uploadButton)


        self.verticalLayout_12.addWidget(self.uploadContainer)

        self.gameContainer = QFrame(self.buttonContainer)
        self.gameContainer.setObjectName(u"gameContainer")
        self.gameContainer.setStyleSheet(u"border: 2px solid rgb(0,0,0);")
        self.gameContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.gameContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.gameContainer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gamesButton = QPushButton(self.gameContainer)
        self.gamesButton.setObjectName(u"gamesButton")
        self.gamesButton.setStyleSheet(u"border: none;")

        self.verticalLayout_11.addWidget(self.gamesButton)


        self.verticalLayout_12.addWidget(self.gameContainer)


        self.verticalLayout_8.addWidget(self.buttonContainer, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_6.addWidget(self.menuContainer)

        self.frame_3 = QFrame(self.slideMenu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.slideMenu)


        self.horizontalLayout.addWidget(self.slideMenuContainer)

        self.mainBody = QFrame(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainBody.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QFrame(self.mainBody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slideMenuButtonFrame = QFrame(self.headerFrame)
        self.slideMenuButtonFrame.setObjectName(u"slideMenuButtonFrame")
        self.slideMenuButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.slideMenuButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slideMenuButtonFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton = QPushButton(self.slideMenuButtonFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.slideMenuButtonFrame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.titleFrame = QFrame(self.headerFrame)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.titleFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.titleFrame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.titleFrame, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.contentsFrame = QFrame(self.mainBody)
        self.contentsFrame.setObjectName(u"contentsFrame")
        self.contentsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentsFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.contentsFrame)

        self.footerFrame = QFrame(self.mainBody)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.credit = QFrame(self.footerFrame)
        self.credit.setObjectName(u"credit")
        self.credit.setFrameShape(QFrame.Shape.StyledPanel)
        self.credit.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.credit)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.credit)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.credit)

        self.sizeGrip = QFrame(self.footerFrame)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.sizeGrip, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.footerFrame, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGames.setText(QCoreApplication.translate("MainWindow", u"Games", None))
        self.actionAnalyze.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.actionUngrouped_Footage.setText(QCoreApplication.translate("MainWindow", u"Ungrouped Footage", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"AI TRACKER", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.uploadButton.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.gamesButton.setText(QCoreApplication.translate("MainWindow", u"Games", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AI Tracker by North Hess v0.1", None))
    # retranslateUi

