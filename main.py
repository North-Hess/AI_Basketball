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

        # Upload files to system button
        self.ui.uploadFileButton.clicked.connect(lambda: self.uploadFiles())

        # Main content change
        self.ui.uploadButton.clicked.connect(lambda: self.uploadContent())
        self.ui.homeButton.clicked.connect(lambda: self.homeContent())
        self.ui.gamesButton.clicked.connect(lambda: self.gamesContent())

        # Ensure default directories exist
        self.ungroupedFootageDirectory = os.path.join(os.getcwd(), "UngroupedFootage")
        if not os.path.exists(self.ungroupedFootageDirectory):
            os.mkdir(self.ungroupedFootageDirectory)

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

    # Function for button in upload page to upload files to system for analysis
    def uploadFiles(self) -> None:
        defaultDirectory = os.path.join(os.path.expanduser('~'), "Documents", "")
        fileFilter = "Images (*.jpeg, *.jpg, *.png);; Videos(*.mp4, *.mov);;"
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption="Select file(s) to upload",
            directory=defaultDirectory,
            filter=fileFilter,
            initialFilter="Images (*.jpeg, *.jpg, *.png)"
        )
        filesToCopy = response[0]
        for file in filesToCopy:
            fileName = os.path.split(file)[1]
            os.rename(file, os.path.join(self.ungroupedFootageDirectory, fileName))


    # Functions for buttons in slide menu to update page
    def homeContent(self) -> None:
        self.ui.contentsStackedWidget.setCurrentIndex(0)
        self.ui.label_2.setText(QCoreApplication.translate("MainWindow", "Welcome!", None))

    def uploadContent(self) -> None:
        self.ui.contentsStackedWidget.setCurrentIndex(1)
        self.ui.label_2.setText(QCoreApplication.translate("MainWindow", "Upload", None))

    def gamesContent(self) -> None:
        self.ui.contentsStackedWidget.setCurrentIndex(2)
        self.ui.label_2.setText(QCoreApplication.translate("MainWindow", "Games", None))


# Execute application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())