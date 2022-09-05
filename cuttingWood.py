from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

import resizeWood
import inputWood
import withdrawWood
import heatWood
import saleWood
import main

class  UI_Cutwood (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cutting")
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.display()
        self.displayTable()
        self.layouts()

# Tool Bar
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
        self.addInput.triggered.connect(self.funcInput)
        self.tb.addSeparator()
        # Cutting
        self.addCut=QAction(QIcon('icons/cutting.png'),"รายการตัด/ผ่า",self)
        self.tb.addAction(self.addCut)
         # self.addCut.triggered.connect(self.funcCut)
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

# Display
    def display(self):
        self.wg=QWidget()
        self.setCentralWidget((self.wg))
        self.cuttingText = QLabel("GUI CUTTING")

# Table
    def displayTable(self):
        self.cuttingTable = QTableWidget()
        self.cuttingTable.setRowCount(100)
        self.cuttingTable.setColumnCount(8)
        self.cuttingTable.setHorizontalHeaderItem(0, QTableWidgetItem("โค๊ดไม้"))
        self.cuttingTable.setHorizontalHeaderItem(1, QTableWidgetItem("หนา"))
        self.cuttingTable.setHorizontalHeaderItem(2, QTableWidgetItem("กว้าง"))
        self.cuttingTable.setHorizontalHeaderItem(3, QTableWidgetItem("ยาว"))
        self.cuttingTable.setHorizontalHeaderItem(4, QTableWidgetItem("จำนวน"))
        self.cuttingTable.setHorizontalHeaderItem(5, QTableWidgetItem("ปริมาตร(m^3)"))
        self.cuttingTable.setHorizontalHeaderItem(6, QTableWidgetItem("วันที่เบิก"))
        self.cuttingTable.setHorizontalHeaderItem(7, QTableWidgetItem("สถานะ"))

        self.cuttingTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

#Layouts
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainLeftLayout = QHBoxLayout()
        self.mainRightLayout = QHBoxLayout()
        self.leftTopLayout = QHBoxLayout()
        self.middleTopLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()
        self.sizeGropBox = QGroupBox("")

        # Left Top
        self.leftTopLayout.addWidget(self.cuttingText)
        self.sizeGropBox.setLayout(self.leftTopLayout)

        # Table
        self.mainLeftLayout.addWidget(self.cuttingTable)
        # All Layout
        self.mainRightLayout.addWidget(self.sizeGropBox)
        self.mainLayout.addLayout(self.mainRightLayout)
        self.mainLayout.addLayout(self.mainLeftLayout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

# Function Home
    def funcHome(self):
        self.newHome=main.Ui_MainWindow()
        self.close()

# Function Input
    def funcInput (self):
        self.newInput=inputWood.UI_Inputwood()
        self.close()

# Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw=withdrawWood.UI_Withdraw()
        self.close()

# Function Heat
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.close()

# Function Resize
    def funcResize(self):
        self.newResize=resizeWood.UI_Resizewood()
        self.close()

# Function  Sale
    def funcSale(self):
        self.newSale=saleWood.UI_Salewood()
        self.close()

# Main
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window=UI_Heatwood()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#    main()
