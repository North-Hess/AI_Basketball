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
        self.programDirectory = os.getcwd()
        self.ungroupedFootageDirectory = os.path.join(self.programDirectory, "UngroupedFootage")
        self.gamesDirectory = os.path.join(self.programDirectory, "Games")
        # Ungrouped footage directory
        if not os.path.exists(self.ungroupedFootageDirectory):
            os.mkdir(self.ungroupedFootageDirectory)
        # Directory of game directories
        if not os.path.exists(self.gamesDirectory):
            os.mkdir(self.gamesDirectory)

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
        fileFilter = "JPEG (*.jpeg *.jpg);; PNG (*.png);; MP4 (*.mp4);; MOV (*.mov)"
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption="Select file(s) to upload",
            directory=defaultDirectory,
            filter=fileFilter,
            initialFilter="JPEG (*.jpeg *.jpg)"
        )
        filesToCopy = response[0]
        if filesToCopy:
            for file in filesToCopy:
                fileName = os.path.split(file)[1]
                os.rename(file, os.path.join(self.ungroupedFootageDirectory, fileName))

    # TODO Function for running games against AI
    # Radial button for each game displayed in games page?
    # Select radial button, press run AI button at top of page and run AI against all files in game directory


    # Function for populating games from Games folder
    def populateGames(self) -> None:
        self.games = []
        for directory in os.listdir(self.gamesDirectory):
            fullPath = os.path.join(self.gamesDirectory, directory)
            if os.path.isdir(fullPath):
                self.games.append(directory)

    def populateGamesButtons(self) -> None:
        for child in self.ui.gamesFrame.children():
            if child.objectName() != "gamesFrameLayout":
                child.deleteLater()
        for game in self.games:
            newGame = QRadioButton(self.ui.gamesFrame)
            newGame.setObjectName(f"{game}RadioButton")
            newGame.setText(QCoreApplication.translate("MainWindow", f"{game}", None))
            self.ui.gamesFrameLayout.addWidget(newGame)
            


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
        self.populateGames()
        print(self.games)
        self.populateGamesButtons()


# Execute application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())