# import dependencies
import sys
import os
from PyQt6 import *

# import ui file
from ui import *
from PyQt6 import QtCore

# Create MainWindow
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        # Window title and icon
        self.setWindowTitle("AI Tracker")
        # self.windowIcon("Filepath of icon")

        # Add size grip functionality to sizeGrip frame
        QSizeGrip(self.ui.sizeGrip)

        # Slide menu toggle button
        self.ui.slideMenuButton.clicked.connect(lambda: self.slideMenu())

        # Main content change
        self.ui.uploadButton.clicked.connect(lambda: self.uploadContent())
        self.ui.homeButton.clicked.connect(lambda: self.homeContent())
        self.ui.gamesButton.clicked.connect(lambda: self.gamesContent())

        self.show()

    # Function for slide menu to move in and out
    def slideMenu(self) -> None:
        # Get current slide menu width
        width = self.ui.slideMenuContainer.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            # self.ui.slideMenuButton.setIcon("") <- changes icon for menu button
        # If maximized
        else:
            # Restore menu
            newWidth = 0
        
        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slideMenuContainer, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    # TODO implement different menus: Home, Upload, Games
    # State machine? Stacked widgets?
    def homeContent(self) -> None:
        self.ui.contentsStackedWidget.setCurrentIndex(0)
        self.ui.label_2.setText(QCoreApplication.translate("MainWindow", "Welcome!", None))

    def uploadContent(self) -> None:
        self.ui.contentsStackedWidget.setCurrentIndex(1)
        self.ui.label_2.setText(QCoreApplication.translate("MainWindow", "Upload", None))

    def gamesContent(self) -> None:
        self.content = "Games"
        self.ui.label_2.setText(QCoreApplication.translate("MainWindow", "Games", None))


# Execute application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())