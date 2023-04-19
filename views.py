import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


from fgo_api import Fgo_Api

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("FGO Servant Viewer")
        self.resize(480, 720)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
        #self.solicitationModel = SolicitationModel()
        self.setupUI()

    def setupUI(self):
        
        """self.table = QTableView()
        self.table.setModel(self.solicitationModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.horizontalHeader().stretchLastSection()

        self.addButton = QPushButton("Add Solicitation")
        self.addButton.clicked.connect(self.openAddDialog)

        self.deleteButton = QPushButton("Delete Solicitation")
        self.deleteButton.clicked.connect(self.deleteSolicitation)"""

        main_container = QVBoxLayout()

        # Setup filter container
        filter_container = QHBoxLayout()
        self.region_filter = QComboBox()
        self.region_filter.addItems(["Test"])
        self.class_filter = QComboBox()
        self.class_filter.addItems(["Test"])
        self.rarity_filter = QComboBox()
        self.rarity_filter.addItems(["Test"])
        self.name_chooser = QComboBox()
        self.name_chooser.addItems(["Test"])

        filter_container.addWidget(self.region_filter)
        filter_container.addWidget(self.class_filter)
        filter_container.addWidget(self.rarity_filter)
        filter_container.addWidget(self.name_chooser)
        
        # Setup servant container
        servant_container = QVBoxLayout()

        banner_container = QHBoxLayout()
        self.class_name = QLabel("Class")
        self.stars = QLabel("5 Stars")

        banner_container.addWidget(self.class_name)
        banner_container.addWidget(self.stars)

        servant_info = QVBoxLayout() #Future Jose Change this to a Grid
        self.name_of_servant = QLabel("It works!")

        servant_info.addWidget(self.name_of_servant)

        servant_container.addLayout(banner_container)
        servant_container.addLayout(servant_info)

        main_container.addLayout(filter_container)
        main_container.addLayout(servant_container)


        self.layout.addLayout(main_container)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
