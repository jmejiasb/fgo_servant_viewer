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


from model import ServantModel

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("FGO Servant Viewer")
        self.resize(480, 720)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.model = ServantModel()
        self.setupUI()

    def setupUI(self):
        
        main_container = QVBoxLayout()

        # Setup filter container
        filter_container = QHBoxLayout()
        self.region_filter = QComboBox()
        self.region_filter.addItems(self.model.list_regions)
        self.class_filter = QComboBox()
        self.class_filter.addItems(self.model.list_classes)
        self.rarity_filter = QComboBox()
        self.rarity_filter.addItems(self.model.list_rarities)
        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.filterConnection)

        filter_container.addWidget(self.region_filter)
        filter_container.addWidget(self.class_filter)
        filter_container.addWidget(self.rarity_filter)
        filter_container.addWidget(self.filter_button)
        
        self.name_chooser = QComboBox()
        self.name_chooser.currentTextChanged.connect(self.showServantInfo)
        #filter_container.addWidget(self.name_chooser)
        
        # Setup banner container

        banner_container = QHBoxLayout()
        self.class_name = QLabel("Class:")
        self.stars = QLabel()

        banner_container.addWidget(self.class_name)
        banner_container.addWidget(self.stars)

        # Setup servant container
        servant_container = QVBoxLayout()

        servant_info = QVBoxLayout() #Future Jose Change this to a Grid
        self.name_of_servant = QLabel()

        servant_info.addWidget(self.name_of_servant)

        servant_container.addLayout(servant_info)

        main_container.addLayout(filter_container)
        main_container.addWidget(self.name_chooser)
        main_container.addLayout(banner_container)
        main_container.addLayout(servant_container)


        self.layout.addLayout(main_container)

    def filterConnection(self):

        region = self.region_filter.currentText()
        class_ = self.class_filter.currentText().lower()
        rarity = int(self.rarity_filter.currentText())

        
        self.model.filterServant(region, class_, rarity)
        
        self.name_chooser.addItems([])
        self.name_chooser.addItems(self.model.filtered_servants)


    def showServantInfo(self):
        #Change this to reflect all the info, for now just the name
        #Should call get_servant witht the id of the servant selected
        current_name = self.name_chooser.currentText()
        self.name_of_servant.setText(current_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
