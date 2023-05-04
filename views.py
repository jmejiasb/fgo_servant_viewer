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
        self.test_servant = self.model.fgo.get_servant("JP",504600)
        self.__setupUI()
        

    def __setupUI(self):
        
        main_container = QVBoxLayout()

        self.filter_container = self.__setupFilterContainer()
        #self.banner_container = self.__setupBannerContainer()
        self.servant_container = self.__setupServantContainer()

        self.name_chooser = QComboBox()
        self.name_chooser.currentTextChanged.connect(self.showServantInfo)
        
        main_container.addLayout(self.filter_container)
        main_container.addWidget(self.name_chooser)
        #main_container.addLayout(self.banner_container)
        main_container.addLayout(self.servant_container)

        self.layout.addLayout(main_container)

    def __setupFilterContainer(self):
        # Setup filter container
        filter = QHBoxLayout()
        self.region_filter = QComboBox()
        self.region_filter.addItems(self.model.list_regions)
        self.class_filter = QComboBox()
        self.class_filter.addItems(self.model.list_classes)
        self.rarity_filter = QComboBox()
        self.rarity_filter.addItems(self.model.list_rarities)
        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.filterConnection)
        
        filter.addWidget(self.region_filter)
        filter.addWidget(self.class_filter)
        filter.addWidget(self.rarity_filter)
        filter.addWidget(self.filter_button)

        return filter
    
    """def __setupBannerContainer(self):
        # Setup banner container, probably gonna erase this

        banner = QHBoxLayout()
        self.class_name = QLabel("Class:")
        self.stars = QLabel()

        banner.addWidget(self.class_name)
        banner.addWidget(self.stars)

        return banner
    """

    def __setupServantContainer(self):
        servant_container = QVBoxLayout()

        servant_info = QGridLayout() 

        self.graph_pixmap = QPixmap()
        self.servant_graph = QLabel("test")

        name_label = QLabel("Name :")
        self.servant_name = QLabel(self.test_servant["name"])

        attribute = QLabel("Attribute :")
        self.servant_attribute = QLabel(self.test_servant["attribute"].capitalize())

        alignment = QLabel("Alignment :")
        self.servant_alignment = QLabel("test2")

        self.stage_1 = QPushButton("Stage 1")
        self.stage_2 = QPushButton("Stage 2")
        self.stage_3 = QPushButton("Stage 3")
        self.stage_4 = QPushButton("Stage 4")

        servant_info.addWidget(self.servant_graph,0,0,5,2)
        servant_info.addWidget(name_label,0,2)
        servant_info.addWidget(self.servant_name,0,3)
        servant_info.addWidget(attribute,1,2)
        servant_info.addWidget(self.servant_attribute,1,3)
        servant_info.addWidget(alignment,2,2)
        servant_info.addWidget(self.servant_alignment,2,3)
        servant_info.addWidget(self.stage_1,3,2)
        servant_info.addWidget(self.stage_2,3,3)
        servant_info.addWidget(self.stage_3,4,2)
        servant_info.addWidget(self.stage_4,4,3)

        servant_container.addLayout(servant_info)

        return servant_container

    def filterConnection(self):

        self.name_chooser.clear()

        region = self.region_filter.currentText()
        class_ = self.class_filter.currentText()
        rarity = int(self.rarity_filter.currentText())

        

        self.model.filterServant(region, class_, rarity)

        self.name_chooser.addItems(self.model.filtered_servants)


    def showServantInfo(self):

        region = self.region_filter.currentText()
        current_name = self.name_chooser.currentText()
        id = self.model.fgo.get_id_by_name(region, current_name)
        
        self.servant = self.model.fgo.get_servant(region, id)

        stage = 1
        self.setServantImage(stage)

        self.servant_name.setText(self.servant["name"])
        self.servant_attribute.setText(self.servant["attribute"].capitalize())

        #Do the split and merge of the alignments

        #Do the buttons with servant["extraAssets"]["charaGraph"]["ascension"]["1"]...

    def setServantImage(self,stage):

        image = self.model.fgo.get_image(self.servant["extraAssets"]["charaGraph"]["ascension"][str(stage)]).content
        self.graph_pixmap.loadFromData(image)
        scaled_graph = self.graph_pixmap.scaled(240, 360, Qt.AspectRatioMode.KeepAspectRatio)

        self.servant_graph.setPixmap(scaled_graph)
        self.servant_graph.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
