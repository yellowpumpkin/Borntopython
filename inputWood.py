from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import sqlite3

import heatWood
import main
import resizeWood
import saleWood
import withdrawWood
import cuttingWood
import editsInputwood

from moduleDB import database

con = sqlite3.connect('dbDEMO.db')
cur = con.cursor()

db = database()


class UI_Inputwood(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ข้อมูลไม้เข้า")
        self.setWindowIcon(QIcon('icons/wood01.png'))
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):

        self.toolBar()
        self.tablewidgets()
        self.Widget()
        self.layouts()
        self.funcDisplayInputWood()

    ####################################### Tool Bar #################################################
    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # หน้าหลัก
        self.addHome = QAction(QIcon('icons/warehouse01.png'), "หน้าหลัก", self)
        self.tb.addAction(self.addHome)
        self.addHome.triggered.connect(self.funcHome)
        self.tb.addSeparator()
        # รับไม้เข้า
        self.addInput = QAction(QIcon('icons/forklift.png'), "รายการรับไม้เข้า", self)
        self.tb.addAction(self.addInput)
        self.tb.addSeparator()
        # Cutting
        self.addCut = QAction(QIcon('icons/cutting.png'), "รายการตัด/ผ่า", self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # Resize
        self.addResize = QAction(QIcon('icons/cutting.png'), "รายการแปลงไม้", self)
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

        # self.allwood=QRadioButton("AllWood")
        # self.avaiableWood=QRadioButton("Avaiable")
        # self.unavaiableWood=QRadioButton("Unavaiable")
        self.searchText = QLabel("Wood ID : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. 6328218")
        self.searchButton = QPushButton("Search")

        # combobox
        self.sizeText = QLabel("ขนาดไม้")
        self.thickText = QLabel("หนา")
        self.wideText = QLabel("x กว้าง")
        self.longText = QLabel("x ยาว")

        # combobox thick
        self.combboxThick = QComboBox()
        Thick = db.dataThick()
        for data_thick in Thick:
            self.combboxThick.addItems([str(data_thick)])

        # combobox wide
        self.comboboxWide = QComboBox()
        Wide = db.dataWide()
        for data_wide in Wide:
            self.comboboxWide.addItems([str(data_wide)])

        # combobox long
        self.comboboxLong = QComboBox()
        Long = db.dataLong()
        for data_long in Long:
            self.comboboxLong.addItems([str(data_long)])

        # combobox woodtype
        self.typeText = QLabel("ประเภทไม้ : ")
        self.comboboxType = QComboBox()
        Type = db.dataType()
        for data_type in Type:
            self.comboboxType.addItems([str(data_type)])

        self.dateText = QLabel("วันที่รับไม้เข้า : ")
        self.date = QDateEdit(self)
        self.date.setDate(QDate.currentDate())
        self.date.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))

        # self.date.setGeometry(300,300,350,200)
        self.date.setAcceptDrops(False)
        self.date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setDisplayFormat('yyyy-MM-dd')
        self.date.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(True)

        self.btn_insert_input = QPushButton("insert")
        self.btn_save_input = QPushButton()
        self.btn_save_input.setIcon(QIcon('icons/excel (2).png'))

    ####################################### Table  #################################################
    def tablewidgets(self):
        self.inputTable = QTableWidget()
        self.inputTable.setColumnCount(9)
        self.inputTable.setHorizontalHeaderItem(0, QTableWidgetItem("วันที่รับไม้เข้า"))
        self.inputTable.setHorizontalHeaderItem(1, QTableWidgetItem("รหัสไม้"))
        self.inputTable.setHorizontalHeaderItem(2, QTableWidgetItem("ประเภทไม้"))
        self.inputTable.setHorizontalHeaderItem(3, QTableWidgetItem("หนา"))
        self.inputTable.setHorizontalHeaderItem(4, QTableWidgetItem("กว้าง"))
        self.inputTable.setHorizontalHeaderItem(5, QTableWidgetItem("ยาว"))
        self.inputTable.setHorizontalHeaderItem(6, QTableWidgetItem("ปริมาตร (m^3)"))
        self.inputTable.setHorizontalHeaderItem(7, QTableWidgetItem("Supplier"))
        self.inputTable.setHorizontalHeaderItem(8, QTableWidgetItem("Manage"))
        self.inputTable.doubleClicked.connect(self.funchandleButtonClicked)
        self.inputTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        #

    ####################################### Layouts #################################################
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainLeftLayout = QHBoxLayout()
        self.mainRightLayout = QHBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightMiddleLayout = QVBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()

        self.searchGropBox = QGroupBox()
        self.sizeGrop = QGroupBox()
        self.btnGrop = QWidget()

        # Right Middle Layouts
        self.rightBottomLayout.addWidget(self.searchText)
        self.rightBottomLayout.addWidget(self.searchEntry)
        self.rightBottomLayout.addWidget(self.searchButton)
        self.rightBottomLayout.addWidget(self.dateText)
        self.rightBottomLayout.addWidget(self.date)
        self.searchGropBox.setLayout(self.rightBottomLayout)

        self.rightTopLayout.addWidget(self.sizeText)
        self.rightTopLayout.addWidget(self.thickText)
        self.rightTopLayout.addWidget(self.combboxThick)
        self.rightTopLayout.addWidget(self.wideText)
        self.rightTopLayout.addWidget(self.comboboxWide)
        self.rightTopLayout.addWidget(self.longText)
        self.rightTopLayout.addWidget(self.comboboxLong)
        self.rightTopLayout.addWidget(self.typeText)
        self.rightTopLayout.addWidget(self.comboboxType)
        self.sizeGrop.setLayout(self.rightTopLayout)

        self.rightMiddleLayout.addWidget(self.btn_insert_input)
        self.rightMiddleLayout.addWidget(self.btn_save_input)
        self.btnGrop.setLayout(self.rightMiddleLayout)

        # Layout Table
        self.mainLeftLayout.addWidget(self.inputTable)

        # All Layout
        self.mainRightLayout.addWidget(self.searchGropBox)
        self.mainRightLayout.addWidget(self.sizeGrop)
        self.mainRightLayout.addWidget(self.btnGrop)
        self.mainLayout.addLayout(self.mainRightLayout)
        self.mainLayout.addLayout(self.mainLeftLayout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

    ################################# Fucntion Home ####################################
    def funcHome(self):
        self.newHome = main.Ui_MainWindow()
        self.hide()

    ################################# Fucntion Cut  ##########################################
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.hide()

    ################################# Fucntion Withdraw ######################################
    def funcWithdraw(self):
        self.newWithdraw = withdrawWood.UI_Withdraw()
        self.hide()

    ################################# Fucntion Resize ######################################
    def funcResize(self):
        self.newResize = resizeWood.UI_Resizewood()
        self.hide()

    ################################# Fucntion Heat ######################################
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.hide()

    ################################# Fucntion Sale ######################################
    def funcSale(self):
        self.newHeat = saleWood.UI_Salewood()
        self.hide()

    ###############################3# Display ###########################################
    def funcDisplayInputWood(self):
        for i in reversed(range(self.inputTable.rowCount())):
            self.inputTable.removeRow(i)
        query = db.dataTableInput()
        for row_data in query:
            row_number = self.inputTable.rowCount()
            self.inputTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.inputTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.btn_edit = QPushButton('Edit')
            self.btn_edit.setStyleSheet("""
                        QPushButton {
                            color:  black;
                            border-style: solid;
                            border-width: 3px;
                            border-color:  #008CBA;
                            border-radius: 12px
                        }
                        QPushButton:hover{
                            background-color: #008CBA;
                            color: white;
                        }
                    """)
            self.btn_edit.clicked.connect(self.funchandleButtonClicked)
            self.inputTable.setCellWidget(row_number, 8, self.btn_edit)
        self.inputTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    ################################# Edit ####################################
    def funchandleButtonClicked(self):
        global Input_id
        listInput = []
        for i in range(0, 8):
            listInput.append(self.inputTable.item(self.inputTable.currentRow(), i).text())
        # print("Listinput = ",listInput)
        Input_id = listInput[1]
        # return Input_id

        self.neweditInput = editsInputwood.UI_editsInputwood(listInput,Input_id)

#################################### Main ###############################################
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window = UI_Inputwood()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()
