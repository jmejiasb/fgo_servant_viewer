from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QHBoxLayout, QPushButton, QGridLayout, QLabel, QButtonGroup, \
                            QFrame, QMessageBox, QMainWindow, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from .model import ServantModel

class MainWindow(QMainWindow):

    app_style = """
    QWidget 
    {
        background-color: #f5fcff;
        font: sans-serif;
        font-size: 13px
    }

    QPushButton
    {
        outline: 0;
        border: 1px solid #005781;
        font-weight: 600;
        font-size: 13px;
        height: 30px;
        background-color: #ffffff;
        color: #005781;
        padding: 0 20px;
    }
    
    QPushButton:hover 
    {
        background: #005781;
        color: #fff;  
    }

    QLabel
    {
        font-size: 13px;
        padding: 10px;
    }

    QGridLayout
    {
        border: 1px solid #005781;
        font-size: 13px;
    }

    QComboBox {
        border: 1px solid #005781;
        background: #ffffff;
        min-width: 6em;
        padding: 0 10px;
    }

    QComboBox:editable {
        background: white;
    }

    QComboBox:on { /* shift the text when the popup opens */
        padding-top: 3px;
        padding-left: 4px;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;

        border-left-width: 1px;
        border-left-color: darkgray;
        border-left-style: solid; /* just a single line */
        border-top-right-radius: 3px; /* same radius as the QComboBox */
        border-bottom-right-radius: 3px;
    }

    QScrollBar
    {
        background : #f5fcff;
    }

    QScrollBar::handle
    {
        background : #005781;
    }
    
    QScrollBar::handle::pressed
    {
        background : #004F75;
    }



"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("FGO Servant Viewer")
        self.resize(600, 300)
        self.setStyleSheet(MainWindow.app_style)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.model = ServantModel()
        self.name_chooser = QComboBox()
        self.__setupUI()
        

    def __setupUI(self):
        
        main_container = QVBoxLayout()
        

        self.filter_container = self.__setupFilterContainer()
        self.servant_container = self.__setupServantContainer()

        self.name_chooser.currentTextChanged.connect(self.__showServantInfo)
        
        main_container.addWidget(QLabel("Choose the Server Region, Class and Rarity and click 'Filter' to look for servants!"))
        main_container.addLayout(self.filter_container)
        main_container.addWidget(self.name_chooser)
        main_container.addWidget(self.servant_container)
        main_container.addStretch()

        self.layout.addLayout(main_container)

    def __setupFilterContainer(self):
        # Setup filter container
        filter = QHBoxLayout()

        region = QLabel("Region:")
        self.region_filter = QComboBox()
        self.region_filter.addItems(self.model.list_regions)
        self.region_filter.currentTextChanged.connect(self.__clearServantList)
        _class = QLabel("Class:")
        self.class_filter = QComboBox()
        self.class_filter.currentTextChanged.connect(self.__clearServantList)
        self.class_filter.addItems(self.model.list_classes)
        rarity = QLabel("Rarity:")
        self.rarity_filter = QComboBox()
        self.rarity_filter.addItems(self.model.list_rarities)
        self.rarity_filter.currentTextChanged.connect(self.__clearServantList)
        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.__filterServant)
        
        filter.addWidget(region)
        filter.addWidget(self.region_filter)
        filter.addWidget(_class)
        filter.addWidget(self.class_filter)
        filter.addWidget(rarity)
        filter.addWidget(self.rarity_filter)
        filter.addWidget(self.filter_button)

        return filter

    def __setupServantContainer(self):
        servant_container = QHBoxLayout()

        servant_info = QGridLayout() 
        servant_info.setVerticalSpacing(10)

        self.graph_pixmap = QPixmap()
        self.servant_graph = QLabel()
        self.servant_graph.setFixedSize(384,543)

        name_label = QLabel("Name :")
        self.servant_name = QLabel()

        attribute = QLabel("Attribute :")
        self.servant_attribute = QLabel()

        alignment = QLabel("Alignment :")
        self.servant_alignment = QLabel()

        self.stage_1 = QPushButton("Stage 1")
        self.stage_2 = QPushButton("Stage 2")
        self.stage_3 = QPushButton("Stage 3")
        self.stage_4 = QPushButton("Stage 4")

        base_atk = QLabel("Base ATK:")
        self.servant_base_atk = QLabel()

        max_atk = QLabel("Max ATK:")
        self.servant_max_atk = QLabel()

        base_hp = QLabel("Base HP:")
        self.servant_base_hp = QLabel()

        max_hp = QLabel("Max HP:")
        self.servant_max_hp = QLabel()
        
        servant_info.addWidget(name_label,0,0)
        servant_info.addWidget(self.servant_name,0,1)
        servant_info.addWidget(attribute,1,0)
        servant_info.addWidget(self.servant_attribute,1,1)
        servant_info.addWidget(alignment,2,0)
        servant_info.addWidget(self.servant_alignment,2,1)
        servant_info.addWidget(self.stage_1,3,0)
        servant_info.addWidget(self.stage_2,3,1)
        servant_info.addWidget(self.stage_3,4,0)
        servant_info.addWidget(self.stage_4,4,1)
        servant_info.addWidget(base_atk,5,0)
        servant_info.addWidget(self.servant_base_atk,5,1)
        servant_info.addWidget(max_atk,6,0)
        servant_info.addWidget(self.servant_max_atk,6,1)
        servant_info.addWidget(base_hp,7,0)
        servant_info.addWidget(self.servant_base_hp,7,1)
        servant_info.addWidget(max_hp,8,0)
        servant_info.addWidget(self.servant_max_hp,8,1)
        
        self.stage_group = QButtonGroup()
        self.stage_group.setExclusive(True)
        self.stage_group.addButton(self.stage_1)
        self.stage_group.addButton(self.stage_2)
        self.stage_group.addButton(self.stage_3)
        self.stage_group.addButton(self.stage_4)

        self.stage_group.buttonClicked.connect(self.__changeServantImage)

        servant_container.addWidget(self.servant_graph)
        servant_container.addLayout(servant_info)

        frame = QFrame()
        frame.setLayout(servant_container)
        frame.hide()

        return frame

    def __filterServant(self):

        region = self.region_filter.currentText()
        class_ = self.class_filter.currentText()
        rarity = int(self.rarity_filter.currentText())
        name_chooser_names = [self.name_chooser.itemText(i) for i in range(self.name_chooser.count())]

        filtered_servants = self.model.filterServant(region, class_, rarity)

        if set(name_chooser_names) != set(filtered_servants):

            self.name_chooser.addItems(filtered_servants)

        self.is_filtered = True

        self.__showServantInfo()

    def __clearServantList(self):

        self.is_filtered = False

        if self.name_chooser.currentText() != "":
            
            self.name_chooser.clear()

    def __showServantInfo(self):
        
        if self.is_filtered == True:
            region = self.region_filter.currentText()
            current_name = self.name_chooser.currentText()

            id = self.model.fgo.get_id_by_name(region, current_name)

            self.servant = self.model.fgo.get_servant(region, id)
            
            if "detail" in self.servant.keys():
                QMessageBox.critical(
                        self,
                        "Error",
                        f"No servant found! Please try again",
                    )
                self.is_filtered == False
                return
            else:
                stage = 1
                self.__setServantImage(stage)

                self.servant_name.setText(self.servant["name"])
                self.servant_attribute.setText(self.servant["attribute"].capitalize())
                self.servant_alignment.setText(self.model.getServantAlignment(self.servant))
                self.servant_base_atk.setText(str(self.servant["atkBase"]))
                self.servant_max_atk.setText(str(self.servant["atkMax"]))
                self.servant_base_hp.setText(str(self.servant["hpBase"]))
                self.servant_max_hp.setText(str(self.servant["hpMax"]))

                self.servant_container.show()

    def __setServantImage(self,stage):
        
        image = self.model.getServantImage(stage, self.servant)
        
        self.graph_pixmap.loadFromData(image)
        #scaled_graph = self.graph_pixmap.scaled(360, 540, Qt.AspectRatioMode.KeepAspectRatio)

        self.servant_graph.setPixmap(self.graph_pixmap)
        self.servant_graph.setScaledContents(True)

    def __changeServantImage(self,button):

        stage = button.text()[-1]

        if self.is_filtered == True:
            

            self.__setServantImage(stage)

    
class App(QApplication):

    def __init__(self):
        super().__init__()
