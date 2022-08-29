from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import  sqlite3

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
        self.mainDesign()
        self.toolBar()
        self.tablewidgets()
        self.Widget()
        self.layouts()

    def mainDesign(self):
        pass
    ####################################### Tool Bar #################################################
    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ################################# หน้าหลัก ############################################
        self.addHome = QAction(QIcon('icons/warehouse01.png'), "หน้าหลัก", self)
        self.tb.addAction(self.addHome)
        self.addHome.triggered.connect(self.funcHome)
        self.tb.addSeparator()
        ################################## รับไม้เข้า ############################################
        self.addInput = QAction(QIcon('icons/forklift.png'), "รายการรับไม้เข้า", self)
        self.tb.addAction(self.addInput)
        self.addInput.triggered.connect(self.funcAddInput)
        self.tb.addSeparator()
        ################################## Cutting ###########################################
        self.addCut=QAction(QIcon('icons/cutting.png'),"รายการตัด/ผ่า",self)
        self.tb.addAction(self.addCut)
         # self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        ################################## Resize ###########################################
        self.addResize = QAction(QIcon('icons/cutting.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
        self.addResize.triggered.connect(self.funcResize)
        self.tb.addSeparator()
        ################################# Heat #############################################
        self.addHeat = QAction(QIcon('icons/heat01.png'), "รายการอบไม้", self)
        self.tb.addAction(self.addHeat)
        self.addHeat.triggered.connect(self.funcHeat)
        self.tb.addSeparator()
        ################################## เบิกไม้ #############################################
        self.addWithdraw = QAction(QIcon('icons/wood02.png'), "รายการเบิกไม้", self)
        self.tb.addAction(self.addWithdraw)
        self.addWithdraw.triggered.connect(self.funcWithdraw)
        self.tb.addSeparator()
        ################################## Sale ############################################
        self.addSale = QAction(QIcon('icons/sale01.png'), "รายการขาย", self)
        self.tb.addAction(self.addSale)
        self.addSale.triggered.connect(self.funcSale)
        self.tb.addSeparator()
###################################### Widget ####################################################
    def Widget(self):
        self.wg=QWidget()
        self.setCentralWidget((self.wg))

        self.heatText = QLabel("GUI CUTTING")



    ####################################### Table  #################################################
    def tablewidgets(self):
        self.heatTable = QTableWidget()
        self.heatTable.setRowCount(100)
        self.heatTable.setColumnCount(8)
        self.heatTable.setHorizontalHeaderItem(0, QTableWidgetItem("โค๊ดไม้"))
        self.heatTable.setHorizontalHeaderItem(1, QTableWidgetItem("หนา"))
        self.heatTable.setHorizontalHeaderItem(2, QTableWidgetItem("กว้าง"))
        self.heatTable.setHorizontalHeaderItem(3, QTableWidgetItem("ยาว"))
        self.heatTable.setHorizontalHeaderItem(4, QTableWidgetItem("จำนวน"))
        self.heatTable.setHorizontalHeaderItem(5, QTableWidgetItem("ปริมาตร(m^3)"))
        self.heatTable.setHorizontalHeaderItem(6, QTableWidgetItem("วันที่เบิก"))
        self.heatTable.setHorizontalHeaderItem(7, QTableWidgetItem("สถานะ"))

        self.heatTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

####################################### Layouts #################################################
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainLeftLayout = QHBoxLayout()
        self.mainRightLayout = QHBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightMiddleLayout = QVBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()

        self.sizeGropBox = QGroupBox("")


        ################### Right Middle Layouts ############################
        self.rightBottomLayout.addWidget(self.heatText)
        self.sizeGropBox.setLayout(self.rightBottomLayout)

        ######################  ##############################################
        self.mainLeftLayout.addWidget(self.heatTable)
        ###################### All Layout ####################################
        self.mainRightLayout.addWidget(self.sizeGropBox)
        self.mainLayout.addLayout(self.mainRightLayout)
        self.mainLayout.addLayout(self.mainLeftLayout)

        ######################  Main Layout ###################################
        self.wg.setLayout(self.mainLayout)

################################# Fucntion Home ####################################
    def funcHome(self):
        self.newHome=main.Ui_MainWindow()
        self.close()

################################# Fucntion AddProduct ####################################
    def funcAddInput (self):
        self.newInput=inputWood.UI_Inputwood()
        self.close()

################################# Fucntion Withdraw ######################################
    def funcWithdraw(self):
        self.newWithdraw=withdrawWood.UI_Withdraw()
        self.close()

################################# Fucntion Heat ######################################
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.close()

################################# Fucntion Resize ######################################
    def funcResize(self):
        self.newResize=resizeWood.UI_Resizewood()
        self.close()
################################# Fucntion Sale ######################################
    def funcSale(self):
        self.newSale=saleWood.UI_Salewood()
        self.close()
##################################### Main ###############################################
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window=UI_Heatwood()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#    main()
