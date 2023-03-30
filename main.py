# import dependencies
import sys
import os
from PyQt6 import *

# import ui file
from ui import *
from PyQt6 import QtCore

# import class for ai analysis
from ai import AIDetection

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

        # Games page buttons
        self.ui.runAIButton.clicked.connect(lambda: self.runAI())
        self.ui.renameGameButton.clicked.connect(lambda: self.renameGame())

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

    
    # Runs files from selected game against ai
    def runAI(self) -> None:
        modelClass = AIDetection()
        for child in self.ui.gamesFrame.children():
            if isinstance(child, QRadioButton().__class__) and child.isChecked():
                modelClass.setGameDirectory(os.path.join(self.gamesDirectory, child.objectName()))
                consumable = modelClass.detectLabels()
                self.analyze(consumable)


    # TODO Implement logic for analyzing model results
    def analyze(self, consumable: dict) -> None:
        print(consumable)

    
    # Renames a game
    def renameGame(self) -> None:
        for child in self.ui.gamesFrame.children():
            if isinstance(child, QRadioButton().__class__) and child.isChecked():
                oldName = os.path.join(self.gamesDirectory, child.objectName())
        newName, status = QInputDialog.getText(None, "Rename Game", "Enter new name for game:")
        newName = os.path.join(self.gamesDirectory, newName)
        if status:
            os.rename(oldName, newName)
        self.populateGames()
        self.populateGamesButtons()


    # Function for populating games from Games folder
    def populateGames(self) -> None:
        self.games = []
        for directory in os.scandir(self.gamesDirectory):
            if directory.is_dir():
                self.games.append(directory.name)


    # Function for populating radio buttons for each game folder
    def populateGamesButtons(self) -> None:
        for child in self.ui.gamesFrame.children():
            if child.objectName() != "gamesFrameLayout":
                child.deleteLater()
        for game in self.games:
            newGame = QRadioButton(self.ui.gamesFrame)
            newGame.setObjectName(f"{game}")
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
        self.populateGamesButtons()


# Execute application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())