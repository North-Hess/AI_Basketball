# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface_designPfFABS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *



# import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
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
        self.centralwidget.setStyleSheet(u"background-color: transparent;\n"
        "color: black;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slideMenuContainer = QFrame(self.centralwidget)
        self.slideMenuContainer.setObjectName(u"slideMenuContainer")
        self.slideMenuContainer.setMaximumSize(QSize(200, 16777215))
        # background: linear-gradient(0deg, rgba(175,238,238,1) 0%, rgba(252,146,25,1) 100%);
        self.slideMenuContainer.setStyleSheet(u"""
            QFrame#slideMenuContainer {
                background: qlineargradient( x1:1 y1:0, x2:1 y2:1, stop:1 rgba(175,238,238,1), stop:0 rgba(252,146,25,1));
            }
        """)
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
        # Menu button stylesheet
        self.buttonContainer.setStyleSheet("""
            QPushButton {
                border-top: 0.5px solid rgb(0,0,0);
                border-bottom: 0.5px solid rgb(0,0,0);
            }
            QPushButton#uploadButton {
                border-top: none;
                border-bottom: none;
            }
            QPushButton:hover {
                background-color:rgb(218,126,22);
                border-left: 6px solid rgb(0,0,0);
            }
        """)
        self.verticalLayout_12 = QVBoxLayout(self.buttonContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.homeContainer = QFrame(self.buttonContainer)
        self.homeContainer.setObjectName(u"homeContainer")
        # self.homeContainer.setStyleSheet(u"border: 2px solid rgb(0,0,0);")
        self.homeContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.homeContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.homeContainer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.homeContainer)
        self.homeButton.setObjectName(u"homeButton")
        # self.homeButton.setStyleSheet(u"border: none;")
        self.homeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homeButton.setMinimumSize(QSize(0,40))

        self.verticalLayout_9.addWidget(self.homeButton)


        self.verticalLayout_12.addWidget(self.homeContainer)

        self.uploadContainer = QFrame(self.buttonContainer)
        self.uploadContainer.setObjectName(u"uploadContainer")
        # self.uploadContainer.setStyleSheet(u"border: 2px solid rgb(0,0,0);\n"
        # "border-bottom: none;\n"
        # "border-top: none;")
        self.uploadContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.uploadContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.uploadContainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.uploadButton = QPushButton(self.uploadContainer)
        self.uploadButton.setObjectName(u"uploadButton")
        # self.uploadButton.setStyleSheet(u"border: none;")
        self.uploadButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadButton.setMinimumSize(QSize(0,40))

        self.verticalLayout_10.addWidget(self.uploadButton)


        self.verticalLayout_12.addWidget(self.uploadContainer)

        self.gameContainer = QFrame(self.buttonContainer)
        self.gameContainer.setObjectName(u"gameContainer")
        # self.gameContainer.setStyleSheet(u"border: 2px solid rgb(0,0,0);")
        self.gameContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.gameContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.gameContainer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gamesButton = QPushButton(self.gameContainer)
        self.gamesButton.setObjectName(u"gamesButton")
        # self.gamesButton.setStyleSheet(u"border: none;")
        self.gamesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.gamesButton.setMinimumSize(QSize(0,40))

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
        # background-size: cover;
        self.mainBody.setStyleSheet("""
            QFrame#mainBody {
                background: url(%s);
                background-repeat: no-repeat;
                
            }

        """ % os.path.join('Assets', 'image.png'))
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
        self.slideMenuButton = QPushButton(self.slideMenuButtonFrame)
        self.slideMenuButton.setObjectName(u"slideMenuButton")
        self.slideMenuButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.slideMenuButton)


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

        # Create contents frame
        self.contentsFrame = QFrame(self.mainBody)
        self.contentsFrame.setObjectName(u"contentsFrame")
        # Crate border to help visualize space that frame takes up
        # self.contentsFrame.setStyleSheet("border:1px solid rgb(255,0,0);")
        # Create sizing policy to expand contents into space
        contentsSizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        contentsSizePolicy.setHorizontalStretch(0)
        contentsSizePolicy.setVerticalStretch(0)
        contentsSizePolicy.setHeightForWidth(self.contentsFrame.sizePolicy().hasHeightForWidth())
        self.contentsFrame.setSizePolicy(contentsSizePolicy)
        self.contentsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentsFrame.setFrameShadow(QFrame.Shadow.Raised)
        # Create layout for elements in contents frame
        self.contentsLayout = QVBoxLayout(self.contentsFrame)
        self.contentsLayout.setSpacing(0)
        self.contentsLayout.setObjectName("contentsLayout")
        self.contentsLayout.setContentsMargins(0, 0, 0, 0)

        # Create stacked widget for multiple pages
        self.contentsStackedWidget = QStackedWidget(self.contentsFrame)
        self.contentsStackedWidget.setObjectName("contentsStackedWidget")
        # Create identifying border to help visualize
        self.contentsStackedWidget.setStyleSheet("""QStackedWidget {
                                                    border:1px solid rgb(0,0,0);
                                                 }""")
        # Create sizing policy for inner elements
        # contentsStackedWidgetSizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.MinimumExpanding)
        # contentsStackedWidgetSizePolicy.setHorizontalStretch(0)
        # contentsStackedWidgetSizePolicy.setVerticalStretch(0)
        # contentsStackedWidgetSizePolicy.setHeightForWidth(self.contentsStackedWidget.sizePolicy().hasHeightForWidth())
        # self.contentsStackedWidget.setSizePolicy(contentsStackedWidgetSizePolicy)
        # Add stacked widget to contents layout
        self.contentsLayout.addWidget(self.contentsStackedWidget)

        # Create home page
        self.homePage = QWidget()
        self.homePage.setObjectName("homePage")
        # Create home page layout
        self.homePageVerticalLayout = QVBoxLayout(self.homePage)
        self.homePageVerticalLayout.setObjectName("homePageVerticalLayout")
        # Create placeholder home page label
        self.homeLabel = QLabel(self.homePage)
        self.homeLabel.setObjectName("homeLabel")
        self.homeLabel.setStyleSheet("""QLabel#homeLabel {
            background: rgb(175,238,238);
            font-size: 40px;
            padding: 5px;
        }
        """)
        # Add placeholder label to home page layout
        self.homePageVerticalLayout.addWidget(self.homeLabel, 0, Qt.AlignmentFlag.AlignCenter)
        # Add home page widget to stacked widget
        self.contentsStackedWidget.addWidget(self.homePage)


        # Create upload page
        self.uploadPage = QWidget()
        self.uploadPage.setObjectName("uploadPage")
        self.uploadPage.setStyleSheet("border:1px solid rgb(0,0,0);")
        # Create layout for upload page
        self.uploadPageVerticalLayout = QVBoxLayout(self.uploadPage)
        self.uploadPageVerticalLayout.setObjectName("uploadPageVerticalLayout")
        self.uploadPageVerticalLayout.setSpacing(0)
        self.uploadPageVerticalLayout.setContentsMargins(0, 0, 0, 0)
        # Create frame for upload file button
        self.uploadFileButtonFrame = QFrame(self.uploadPage)
        self.uploadFileButtonFrame.setObjectName("uploadFileButtonFrame")
        self.uploadFileButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.uploadFileButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        # Create layout for upload file button frame
        self.uploadFileButtonFrameVerticalLayout = QVBoxLayout(self.uploadFileButtonFrame)
        self.uploadFileButtonFrameVerticalLayout.setObjectName("uploadFileButtonFrameVerticalLayout")
        self.uploadFileButtonFrameVerticalLayout.setSpacing(0)
        self.uploadFileButtonFrameVerticalLayout.setContentsMargins(0,0,0,0)
        # Create upload file button
        self.uploadFileButton = QPushButton(self.uploadFileButtonFrame)
        self.uploadFileButton.setObjectName("uploadFileButton")
        self.uploadFileButton.setMinimumSize(250,75)
        self.uploadFileButton.setMaximumSize(300, 75)
        self.uploadFileButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadFileButton.setStyleSheet("""
            QPushButton#uploadFileButton {
                background: rgb(175,238,238)
            }
        """)
        # Add upload file button to upload file button frame layout
        self.uploadFileButtonFrameVerticalLayout.addWidget(self.uploadFileButton, 0, Qt.AlignmentFlag.AlignHCenter)
        # Add upload file button frame to upload page layout
        self.uploadPageVerticalLayout.addWidget(self.uploadFileButtonFrame)
        # Add upload page to stacked widget
        self.contentsStackedWidget.addWidget(self.uploadPage)

        
        # Create games analysis page
        self.gamesAnalysisPage = QWidget()
        self.gamesAnalysisPage.setObjectName("gamesAnalysisPage")
        # Create games page layout
        self.gamesAnalysisPageVerticalLayout = QVBoxLayout(self.gamesAnalysisPage)
        self.gamesAnalysisPageVerticalLayout.setObjectName("gamesAnalysisPageVerticalLayout")
        self.gamesAnalysisPageVerticalLayout.setContentsMargins(0, 0, 0, 0)
        # Create game action buttons frame
        self.gamesActionButtonsFrame = QFrame(self.gamesAnalysisPage)
        self.gamesActionButtonsFrame.setObjectName("gamesActionButtonsFrame")
        # self.gamesActionButtonsFrame.setMinimumHeight(20)
        # self.gamesActionButtonsFrame.setMinimumHeight(30)
        # self.gamesActionButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        # self.gamesActionButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gamesActionButtonsFrame.setStyleSheet("""
            QPushButton {
                padding: 5px 5px;
                font-size: 10px;
                text-align: center;
                color: rgb(0,0,0);
                background-color: rgb(252, 146, 25);
                border-left: 0.5px solid rgb(0, 0, 0);
            }

            QPushButton:hover {background-color: rgb(218,126,22)}
        """)
        # Create layout for action buttons frame
        # self.gamesActionButtonsFrameLayout = QHBoxLayout(self.gamesActionButtonsFrame)
        self.gamesActionButtonsFrameLayout = QGridLayout(self.gamesActionButtonsFrame)
        self.gamesActionButtonsFrameLayout.setObjectName("gamesActionButtonsFrameLayout")
        self.gamesActionButtonsFrameLayout.setSpacing(0)
        self.gamesActionButtonsFrameLayout.setContentsMargins(0,0,0,0)
        # Create run AI action button
        self.runAIButton = QPushButton(self.gamesActionButtonsFrame)
        self.runAIButton.setObjectName("runAIButton")
        self.runAIButton.setMinimumSize(50,30)
        self.runAIButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # Place run AI action button in frame
        # self.gamesActionButtonsFrameLayout.addWidget(self.runAIButton, alignment=Qt.AlignmentFlag.AlignLeft)
        self.gamesActionButtonsFrameLayout.addWidget(self.runAIButton, 0, 0)
        # Create past analyses action button
        self.pastAnalysesButton = QPushButton(self.gamesActionButtonsFrame)
        self.pastAnalysesButton.setObjectName("pastAnalysesButton")
        self.pastAnalysesButton.setMinimumSize(50,30)
        self.pastAnalysesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # Place past analyses action button in frame
        # self.gamesActionButtonsFrameLayout.addWidget(self.pastAnalysesButton, alignment=Qt.AlignmentFlag.AlignLeft)
        self.gamesActionButtonsFrameLayout.addWidget(self.pastAnalysesButton, 0, 1)
        # Create rename game button
        self.renameGameButton = QPushButton(self.gamesActionButtonsFrame)
        self.renameGameButton.setObjectName("renameGameButton")
        self.renameGameButton.setMinimumSize(50,30)
        self.renameGameButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # Place rename game button in frame
        # self.gamesActionButtonsFrameLayout.addWidget(self.renameGameButton, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.gamesActionButtonsFrameLayout.addWidget(self.renameGameButton, 0, 3)
        # Create create game button
        self.createGameButton = QPushButton(self.gamesActionButtonsFrame)
        self.createGameButton.setObjectName("createGameButton")
        self.createGameButton.setMinimumSize(50,30)
        self.createGameButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # Place create game button in frame
        # self.gamesActionButtonsFrameLayout.addWidget(self.createGameButton, alignment=Qt.AlignmentFlag.AlignRight)
        self.gamesActionButtonsFrameLayout.addWidget(self.createGameButton, 0, 2)
        self.removeGameButton = QPushButton(self.gamesActionButtonsFrame)
        self.removeGameButton.setObjectName("removeGameButton")
        self.removeGameButton.setMinimumSize(50,30)
        self.removeGameButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.gamesActionButtonsFrameLayout.addWidget(self.removeGameButton, 0, 4)
        # Create add footage button
        self.addFootageButton = QPushButton(self.gamesActionButtonsFrame)
        self.addFootageButton.setObjectName("addFootageButton")
        self.addFootageButton.setMinimumSize(50,30)
        self.addFootageButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # Place add footage button in frame
        # self.gamesActionButtonsFrameLayout.addWidget(self.addFootageButton, alignment=Qt.AlignmentFlag.AlignRight)
        self.gamesActionButtonsFrameLayout.addWidget(self.addFootageButton, 0, 5)
        # Create remove footage button
        self.removeFootageButton = QPushButton(self.gamesActionButtonsFrame)
        self.removeFootageButton.setObjectName("removeFootageButton")
        self.removeFootageButton.setMinimumSize(50,30)
        self.removeFootageButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # Place remove footage button in frame
        # self.gamesActionButtonsFrameLayout.addWidget(self.removeFootageButton, alignment=Qt.AlignmentFlag.AlignRight)
        self.gamesActionButtonsFrameLayout.addWidget(self.removeFootageButton, 0, 6)
        

        # Place game action buttons frame to page layout
        self.gamesAnalysisPageVerticalLayout.addWidget(self.gamesActionButtonsFrame, alignment=Qt.AlignmentFlag.AlignTop)

        # Add scroll area for moving through games
        self.gamesScrollArea = QScrollArea(self.gamesAnalysisPage)
        self.gamesScrollArea.setObjectName("gamesScrollArea")
        self.gamesScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.gamesScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.gamesScrollArea.setWidgetResizable(True)
        # Create scroll area layout
        # self.gamesScrollAreaLayout = QVBoxLayout(self.gamesScrollArea)
        # self.gamesScrollAreaLayout.setObjectName("gamesScrollAreaLayout")
        # self.gamesScrollAreaLayout.setContentsMargins(0,0,0,0)
        # Create sizing policy to expand contents into space
        gamesSizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        gamesSizePolicy.setHorizontalStretch(0)
        gamesSizePolicy.setVerticalStretch(0)
        self.gamesFrame = QFrame(self.gamesScrollArea)
        self.gamesFrame.setObjectName("gamesFrame")
        self.gamesFrame.setStyleSheet("""
            QFrame#gamesFrame {
                background: rgb(175,238,238);
            }
        """)
        gamesSizePolicy.setHeightForWidth(self.gamesFrame.sizePolicy().hasHeightForWidth())
        self.gamesFrame.setSizePolicy(gamesSizePolicy)
        # Add frame for radial buttons of game to have action performed on
        self.gamesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.gamesFrame.setFrameShadow(QFrame.Shadow.Raised)
        # Create layout for games frame
        self.gamesFrameLayout = QVBoxLayout(self.gamesFrame)
        self.gamesFrameLayout.setObjectName("gamesFrameLayout")
        # Add games frame to games scroll area layout
        self.gamesScrollArea.setWidget(self.gamesFrame)
        # self.gamesScrollAreaLayout.addWidget(self.gamesFrame)
        


        # Add scroll area to page layout
        self.gamesAnalysisPageVerticalLayout.addWidget(self.gamesScrollArea)

        # Add games page to stacked widget
        self.contentsStackedWidget.addWidget(self.gamesAnalysisPage)

        # Set default widget in contentsStackedWidget
        self.contentsStackedWidget.setCurrentIndex(0)

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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SABA", None))
        # Generate text for home related elements
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.homeLabel.setText(QCoreApplication.translate("MainWindow", "Welcome to the SlamAI: Basketball Analytics!", None))
        # Generate text for upload related elements
        self.uploadButton.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.uploadFileButton.setText(QCoreApplication.translate("MainWindow", "Select game footage", None))
        # Generate text for games related elements
        self.gamesButton.setText(QCoreApplication.translate("MainWindow", u"Games", None))
        self.runAIButton.setText(QCoreApplication.translate("MainWindow", "Run AI", None))
        self.pastAnalysesButton.setText(QCoreApplication.translate("MainWindow", "Past Analyses", None))
        self.createGameButton.setText(QCoreApplication.translate("MainWindow", "Create Game", None))
        self.renameGameButton.setText(QCoreApplication.translate("MainWindow", "Rename Game", None))
        self.removeGameButton.setText(QCoreApplication.translate("MainWindow", "Remove Game", None))
        self.addFootageButton.setText(QCoreApplication.translate("MainWindow", "Add Footage", None))
        self.removeFootageButton.setText(QCoreApplication.translate("MainWindow", "Remove Footage", None))
        # Generate text for slide menu related elements
        self.slideMenuButton.setIcon(QIcon(os.path.join("Assets", "icons8-basketball-96.png")))
        self.slideMenuButton.setIconSize(QSize(32, 32))
        # self.slideMenuButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SlamAI by North Hess v0.1", None))
    # retranslateUi

