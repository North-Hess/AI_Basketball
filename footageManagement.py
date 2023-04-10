from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import os



class FootageManagement(QDialog):
    from main import MainWindow
    def __init__(self, main: MainWindow):
        QDialog.__init__(self)
        self.ui = main.ui
        self.gamesDirectory = main.gamesDirectory
        self.ungroupedFootageDirectory = main.ungroupedFootageDirectory

        self.footageWindow = QDialog(self)
        self.footageWindow.setMaximumSize(500, 500)
        self.footageWindow.setMinimumSize(500, 500)
        self.footageFrame = QFrame(self.footageWindow)
        
        self.footageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footageFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.footageFrameLayout = QVBoxLayout(self.footageFrame)

        self.footageCheckboxFrame = QFrame(self.footageFrame)
        
        self.footageCheckboxFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footageCheckboxFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.footageFrameLayout.addWidget(self.footageCheckboxFrame)

        self.footageCheckboxFrameLayout = QVBoxLayout(self.footageCheckboxFrame)

        self.footageActionFrame = QFrame(self.footageFrame)
                
        self.footageActionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footageActionFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.footageFrameLayout.addWidget(self.footageActionFrame)

        self.footageActionFrameLayout = QHBoxLayout(self.footageActionFrame)

        self.submitButton = QPushButton(self.footageActionFrame)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setText(QCoreApplication.translate("MainWindow", "Submit", None))

        self.cancelButton = QPushButton(self.footageActionFrame)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", "Cancel", None))
        self.cancelButton.clicked.connect(lambda: self.__cancel())
        self.footageActionFrameLayout.addWidget(self.cancelButton)


    def __addFootageWindow(self) -> None:
            game = ""
            for child in self.ui.gamesFrame.children():
                if isinstance(child, QRadioButton().__class__) and child.isChecked():
                    game = os.path.join(self.gamesDirectory, child.objectName())
                    # Add pop up window if no game is selected
            if game:
                # Add pop up window instead if there is not footage
                for footage in os.scandir(self.ungroupedFootageDirectory):
                    addFootageBox = QCheckBox(self.footageCheckboxFrame)
                    addFootageBox.setObjectName(f"{footage.name}")
                    addFootageBox.setText(QCoreApplication.translate("MainWindow", f"{footage.name}", None))
                    self.footageCheckboxFrameLayout.addWidget(addFootageBox)
                
                self.submitButton.clicked.connect(lambda: self.__addFootageSubmit(self.footageCheckboxFrame, self.footageWindow, game))
                self.footageActionFrameLayout.addWidget(self.submitButton)

                self.footageWindow.exec()
            
    # Adds selected footage to selected game from ungrouped footage
    def __addFootageSubmit(self, checkedButtons: QFrame, window: QDialog, game: str) -> None:
        check = True
        for child in checkedButtons.children():
            if isinstance(child, QCheckBox().__class__) and child.isChecked():
                check = False
                os.rename(os.path.join(self.ungroupedFootageDirectory, child.objectName()), os.path.join(game, child.objectName()))
        if check:
            print(1)
            # Add pop up window saying something must be clicked to submit
        else:
            window.close()


    def __removeFootageWindow(self) -> None:
        game = ""
        for child in self.ui.gamesFrame.children():
            if isinstance(child, QRadioButton().__class__) and child.isChecked():
                game = os.path.join(self.gamesDirectory, child.objectName())
                # Add pop up window if no game is selected
        if game:
            # Add pop up window instead if there is not footage
            for footage in os.scandir(game):
                addFootageBox = QCheckBox(self.footageCheckboxFrame)
                addFootageBox.setObjectName(f"{footage.name}")
                addFootageBox.setText(QCoreApplication.translate("MainWindow", f"{footage.name}", None))
                self.footageCheckboxFrameLayout.addWidget(addFootageBox)
            
            self.submitButton.clicked.connect(lambda: self.__removeFootageSubmit(self.footageCheckboxFrame, self.footageWindow, game))
            self.footageActionFrameLayout.addWidget(self.submitButton)

            self.footageWindow.exec()


    def __removeFootageSubmit(self, checkedButtons: QFrame, window: QDialog, game: str) -> None:
        check = True
        for child in checkedButtons.children():
            if isinstance(child, QCheckBox().__class__) and child.isChecked():
                check = False
                os.rename(os.path.join(game, child.objectName()), os.path.join(self.ungroupedFootageDirectory, child.objectName()))
        if check:
            print(1)
            # Add pop up window saying something must be clicked to submit
        else:
            window.close()


    def __cancel(self):
        self.footageWindow.close()
    
    
    def addFootage(self):
        self.__addFootageWindow()

    def removeFootage(self):
        self.__removeFootageWindow()