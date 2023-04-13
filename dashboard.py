from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class Dashboard(QDialog):
    from main import MainWindow
    def __init__(self, main: MainWindow, makes: int, total: int):
        QDialog.__init__(self)
        self.ui = main.ui
        self.game = main.activeGame
        self.gamesDirectory = main.gamesDirectory
        self.ungroupedFootageDirectory = main.ungroupedFootageDirectory

        self.analysisWindow = QDialog(self)
        self.analysisWindow.setMaximumSize(500, 500)
        self.analysisWindow.setMinimumSize(500, 500)
        self.analysisFrame = QFrame(self.analysisWindow)
        
        self.analysisFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.analysisFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.analysisFrameLayout = QVBoxLayout(self.analysisFrame)

        self.titleFrame = QFrame(self.analysisFrame)
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.titleFrameLayout = QHBoxLayout(self.titleFrame)

        self.title = QLabel(self.titleFrame)
        self.title.setObjectName("title")
        self.title.setText(QCoreApplication.translate("MainWindow", self.game, None))

        self.titleFrameLayout.addWidget(self.title)

        self.analysisFrameLayout.addWidget(self.titleFrame, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.bodyFrame = QFrame(self.analysisFrame)
        self.bodyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bodyFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.bodyFrameLayout = QHBoxLayout(self.bodyFrame)
        
        self.makeFrame = QFrame(self.bodyFrame)
        self.makeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.makeFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.makeFrameLayout = QVBoxLayout(self.makeFrame)

        self.makeTitleFrame = QFrame(self.makeFrame)
        self.makeTitleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.makeTitleFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.makeTitleFrameLayout = QVBoxLayout(self.makeTitleFrame)

        self.makeTitle = QLabel(self.makeTitleFrame)
        self.makeTitle.setText(QCoreApplication.translate("MainWindow", "Makes:", None))

        self.makeTitleFrameLayout.addWidget(self.makeTitle)

        self.makeFrameLayout.addWidget(self.makeTitleFrame)

        self.makesFrame = QFrame(self.makeFrame)
        self.makesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.makesFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.makesFrameLayout = QVBoxLayout(self.makesFrame)

        self.makes = QLabel(self.makesFrame)
        self.makes.setText(QCoreApplication.translate("MainWindow", "N/A", None))

        self.makesFrameLayout.addWidget(self.makes)

        self.makeFrameLayout.addWidget(self.makesFrame)

        self.bodyFrameLayout.addWidget(self.makeFrame)

        self.missFrame = QFrame(self.bodyFrame)
        self.missFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.missFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.missFrameLayout = QVBoxLayout(self.missFrame)

        self.missTitleFrame = QFrame(self.missFrame)
        self.missTitleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.missTitleFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.missTitleFrameLayout = QVBoxLayout(self.missTitleFrame)

        self.missTitle = QLabel(self.missTitleFrame)
        self.missTitle.setText(QCoreApplication.translate("MainWindow", "Total Shots:", None))

        self.missTitleFrameLayout.addWidget(self.missTitle)

        self.missFrameLayout.addWidget(self.missTitleFrame)

        self.missesFrame = QFrame(self.missFrame)
        self.missesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.missesFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.missesFrameLayout = QVBoxLayout(self.missesFrame)

        self.misses = QLabel(self.missesFrame)
        self.misses.setText(QCoreApplication.translate("MainWindow", "N/A", None))

        self.missesFrameLayout.addWidget(self.misses)

        self.missFrameLayout.addWidget(self.missesFrame)

        self.bodyFrameLayout.addWidget(self.missFrame)

        self.analysisFrameLayout.addWidget(self.bodyFrame)

        self.makes.setText(str(makes))
        self.misses.setText(str(total))

        self.analysisWindow.exec()

    def setMakes(self, makes: int):
        self.makes.setText(int(makes))

    def setMisses(self, misses: int):
        self.misses.setText(int(misses))