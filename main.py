from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

import sqlite3

import heatWood
import inputWood
import resizeWood
import saleWood
import withdrawWood
import cuttingWood
from moduleDB import database

db = database()

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ระบบคลังไม้")
        self.setWindowIcon(QIcon('icons/wood.png'))
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.tablewidgets()
        self.Widget()
        self.layouts()
        self.funcDisplayMain()

    ####################################### Tool Bar #################################################
    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # หน้าหลัก
        self.addHome = QAction(QIcon('icons/warehouse01.png'), "หน้าหลัก", self)
        self.tb.addAction(self.addHome)
        self.tb.addSeparator()
        # รับไม้เข้า
        self.addInput = QAction(QIcon('icons/forklift.png'), "รายการรับไม้เข้า", self)
        self.tb.addAction(self.addInput)
        self.addInput.triggered.connect(self.funcAddInput)
        self.tb.addSeparator()
        # Cutting
        self.addCut = QAction(QIcon('icons/cutting.png'), "รายการตัด/ผ่า", self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # Resize
        self.addResize = QAction(QIcon('icons/sawmill.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
        self.addResize.triggered.connect(self.funcResize)
        self.tb.addSeparator()
        # Heat
        self.addHeat = QAction(QIcon('icons/heat01.png'), "รายการอบไม้", self)
        self.tb.addAction(self.addHeat)
        self.addHeat.triggered.connect(self.funcHeat)
        self.tb.addSeparator()
        # เบิกไม้
        self.addWithdraw = QAction(QIcon('icons/wood02.png'), "รายการเบิกไม้", self)
        self.tb.addAction(self.addWithdraw)
        self.addWithdraw.triggered.connect(self.funcWithdraw)
        self.tb.addSeparator()
        # Sale
        self.addSale = QAction(QIcon('icons/sale01.png'), "รายการขาย", self)
        self.tb.addAction(self.addSale)
        self.addSale.triggered.connect(self.funcSale)
        self.tb.addSeparator()

    ###################################### Widget ####################################################
    def Widget(self):
        self.wg = QWidget()
        self.setCentralWidget((self.wg))

        self.searchText = QLabel("Wood ID : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. 6328218")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearfch)

        self.allwoodmh = QRadioButton("All")
        self.mainWood = QRadioButton("Main")
        self.headWood = QRadioButton("Head")

        self.allwood = QRadioButton("All Wood")
        self.avaiableWood = QRadioButton("Avaiable")
        self.unavaiableWood = QRadioButton("Unavaiable")
        # self.listBtn = QPushButton("List")
        # self.listBtn.clicked.connect(self.fucnLis)

        # combobox
        self.sizeText = QLabel("| ขนาดไม้ : ")
        self.thickText = QLabel("หนา")
        self.wideText = QLabel("x กว้าง")
        self.longText = QLabel("x ยาว")

        # combobox thick
        self.comboThick = QComboBox()
        Thick = db.dataThick()

        for data_thick in Thick:
            self.comboThick.addItems([str(data_thick)])

        # combobox wide
        self.comboWide = QComboBox()
        Wide = db.dataWide()
        for data_wide in Wide:
            self.comboWide.addItems([str(data_wide)])

        # combobox long
        self.comboLong = QComboBox()
        Long = db.dataLong()
        for data_long in Long:
            self.comboLong.addItems([str(data_long)])

        # combobox woodtype
        self.typeText = QLabel("| ประเภทไม้ : ")
        self.comboType = QComboBox()
        Type = db.dataType()
        for data_type in Type:
            self.comboType.addItems([str(data_type)])

    ####################################### Table  #################################################
    def tablewidgets(self):
        self.homeTable = QTableWidget()

        self.homeTable.setColumnCount(9)
        self.homeTable.setHorizontalHeaderItem(0, QTableWidgetItem("Wood ID"))
        self.homeTable.setHorizontalHeaderItem(1, QTableWidgetItem("Code"))
        self.homeTable.setHorizontalHeaderItem(2, QTableWidgetItem("Type"))
        self.homeTable.setHorizontalHeaderItem(3, QTableWidgetItem("Thick"))
        self.homeTable.setHorizontalHeaderItem(4, QTableWidgetItem("Wide"))
        self.homeTable.setHorizontalHeaderItem(5, QTableWidgetItem("Long"))
        self.homeTable.setHorizontalHeaderItem(6, QTableWidgetItem("Quantity"))
        self.homeTable.setHorizontalHeaderItem(7, QTableWidgetItem("Volume"))
        self.homeTable.setHorizontalHeaderItem(8, QTableWidgetItem("Active"))

    ####################################### Layouts #################################################
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainLeftLayout = QHBoxLayout()
        self.mainRightLayout = QHBoxLayout()
        self.rightTopLayout = QVBoxLayout()
        self.rightMiddleLayout = QVBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()

        self.woodGroupBox = QGroupBox("Main/Head")
        self.middleGropBox = QGroupBox("Activity")
        self.searchGropBox = QGroupBox("Search")

        # Right Top Layouts
        # self.rightTopLayout.addWidget(self.searchText)
        # self.rightTopLayout.addWidget(self.searchEntry)
        # self.rightTopLayout.addWidget(self.searchButton)
        self.rightTopLayout.addWidget(self.allwoodmh)
        self.rightTopLayout.addWidget(self.mainWood)
        self.rightTopLayout.addWidget(self.headWood)
        self.woodGroupBox.setLayout(self.rightTopLayout)

        # Right Middle Layouts
        # self.rightBottomLayout.addWidget(self.searchText)
        # self.rightBottomLayout.addWidget(self.searchEntry)
        # self.rightBottomLayout.addWidget(self.searchButton)
        # self.rightBottomLayout.addWidget(self.sizeText)
        self.rightBottomLayout.addWidget(self.thickText)
        self.rightBottomLayout.addWidget(self.comboThick)
        self.rightBottomLayout.addWidget(self.wideText)
        self.rightBottomLayout.addWidget(self.comboWide)
        self.rightBottomLayout.addWidget(self.longText)
        self.rightBottomLayout.addWidget(self.comboLong)
        self.rightBottomLayout.addWidget(self.typeText)
        self.rightBottomLayout.addWidget(self.comboType)
        self.rightBottomLayout.addWidget(self.searchText)
        self.rightBottomLayout.addWidget(self.searchEntry)
        self.rightBottomLayout.addWidget(self.searchButton)
        self.searchGropBox.setLayout(self.rightBottomLayout)

        # Right Middle Layouts
        self.rightMiddleLayout.addWidget(self.allwood)
        self.rightMiddleLayout.addWidget(self.avaiableWood)
        self.rightMiddleLayout.addWidget(self.unavaiableWood)
        # self.rightMiddleLayout.addWidget(self.listBtn)
        self.middleGropBox.setLayout(self.rightMiddleLayout)

        #
        self.mainLeftLayout.addWidget(self.homeTable)

        # All Layout
        self.mainRightLayout.addWidget(self.searchGropBox)
        self.mainRightLayout.addWidget(self.woodGroupBox)
        self.mainRightLayout.addWidget(self.middleGropBox)

        self.mainLayout.addLayout(self.mainRightLayout)
        self.mainLayout.addLayout(self.mainLeftLayout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

    # Display
    def funcDisplayMain(self):
        for i in reversed(range(self.homeTable.rowCount())):
            self.homeTable.removeRow(i)
        query = db.dataTableHome()
        for row_data in query:
            row_number = self.homeTable.rowCount()
            self.homeTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.homeTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Search
    def funcSearfch(self):
        value= self.searchEntry.text()
        # print(value)
        if value == "":
            QMessageBox.information(self,"Warning","Search cant be empty!!")
        else:
            self.searchEntry.setText("")
            results = db.search(value)
            print(results)
        return
    # List
    def fucnLis(self):
        if self.allwood.isChecked() == True:
            self.funcDisplayMain()
            print("Sss")
    ################################# Fucntion AddProduct ####################################
    def funcAddInput(self):
        self.newInput = inputWood.UI_Inputwood()
        self.hide()

    ################################# Fucntion Cut  ##########################################
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.hide()

    ################################# Fucntion Resize #########################################
    def funcResize(self):
        self.newResize = resizeWood.UI_Resizewood()
        self.hide()

    ################################# Fucntion Heat ###########################################
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.hide()

    ################################# Fucntion Withdraw ######################################
    def funcWithdraw(self):
        self.newWithdraw = withdrawWood.UI_Withdraw()
        self.hide()

    ################################# Fucntion Sale ######################################
    def funcSale(self):
        self.newSale = saleWood.UI_Salewood()
        self.hide()

##################################### Main ###############################################
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()