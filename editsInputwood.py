from PyQt5 import QtWidgets , QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from moduleDB import database
db = database()

class UI_editsInputwood(QWidget):
    def __init__(self, inputdata , input_id):
        super().__init__()
        self.setWindowTitle("แก้ไขข้อมูล")
        self.setWindowIcon(QIcon('icons/edit.png'))
        self.setGeometry(909, 250, 650, 550)
        strdate = inputdata[0]
        self.dt = tuple([int(x) for x in strdate[:10].split('-')])
        self.inputWooddate = self.dt
        self.inputWoodid = inputdata[1]
        self.inputWoodtype = inputdata[2]
        self.inputWoodthick = inputdata[3]
        self.inputWoodtwide = inputdata[4]
        self.inputWoodtlong = inputdata[5]
        self.inputWoodvolume = inputdata[6]
        self.inputWoodsupplier = inputdata[7]
        self.check = input_id

        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.display()
        self.layout()

    # Display
    def display(self):
        # TOP
        self.imgEditInputWood = QLabel()
        self.img = QPixmap('icons/forklift02.png')
        self.imgEditInputWood.setPixmap(self.img)
        self.imgEditInputWood.setAlignment(Qt.AlignCenter)
        self.title_txt = QLabel("แก้ไขข้อมูลรับไม้เข้า")
        self.title_txt.setFont(QFont('Arial', 12))
        self.title_txt.setAlignment(Qt.AlignCenter)

        # Info
        self.dateEditInputWood_txt = QLabel("วันที่รับไม้เข้า: ")
        self.dateEditInputWood = QDateEdit(self)
        self.dateEditInputWood.setDateTime(QtCore.QDateTime(QtCore.QDate(self.inputWooddate[0], self.inputWooddate[1], self.inputWooddate[2])))
        # self.dateEditInputWood.setAcceptDrops(False)
        self.dateEditInputWood.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.dateEditInputWood.setDisplayFormat('yyyy-MM-dd')
        self.dateEditInputWood.setMinimumDate(QtCore.QDate(2019, 1, 1))
        # self.dateEditInputWood.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEditInputWood.setCalendarPopup(True)

        self.woodidEntry = QLineEdit(self)
        self.woodidEntry.setText(self.inputWoodid)
        self.woodtypeCombobox = QComboBox()

        self.woodtypeCombobox.addItems([str(self.inputWoodtype),"Green", "GKD", "KD", "G"])
        self.woodtypeCombobox.setEditable(True)

        self.thickCombobox = QComboBox()
        self.thickCombobox.addItems([str(self.inputWoodthick)])
        self.thickCombobox.setEditable(True)
        self.wideCombobox = QComboBox()
        self.wideCombobox.addItem(self.inputWoodtwide)
        self.wideCombobox.setEditable(True)
        self.longCombobox = QComboBox()
        self.longCombobox.addItem(self.inputWoodtlong)
        self.longCombobox.setEditable(True)

        self.volomeEntry = QLineEdit()
        self.volomeEntry.setText(self.inputWoodvolume)
        self.supplierEntry = QLineEdit()
        self.supplierEntry.setText(self.inputWoodsupplier)
        self.updateBtn = QPushButton("แก้ไขข้อมูล")
        self.updateBtn.setStyleSheet("""
              QPushButton {
                  background-color: #008CBA;
                  color: white;
                  font-size: 14px;
                  text-align: center;
                  padding: 10px 24px;
                  border-radius: 4px
               }
              QPushButton:hover {
                  background-color: white; 
                  border: 0.5px solid #008CBA;
                  color: black;
              }
          """)
        self.updateBtn.clicked.connect(self.funcQmessbox)
        # self.updateBtn.clicked.connect(self.funcUpdateInfo)

        self.cancelBtn = QPushButton("ยกเลิก")
        self.cancelBtn.setStyleSheet("""
              QPushButton {
                  background-color: red;
                  color: white;
                  font-size: 14px;
                  text-align: center;
                  padding: 10px 24px;
                  border-radius: 4px
               }
              QPushButton:hover {
                  background-color: white; 
                  border: 0.5px solid red;
                  color: black;
              }
          """)

        self.cancelBtn.clicked.connect(self.funcClosedbox)

    # Layout
    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.midLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.text = QWidget()
        self.topFrame = QGroupBox()
        self.bottomFrame = QFrame()

        self.midLayout.addWidget(self.title_txt)
        self.text.setLayout(self.midLayout)

        self.topLayout.addWidget(self.imgEditInputWood)
        self.topFrame.setLayout(self.topLayout)
        self.btnbox = QHBoxLayout()
        self.btnbox.addStretch()
        self.btnbox.addWidget(self.updateBtn)
        self.btnbox.addWidget(self.cancelBtn)

        self.bottomLayout.addRow(QLabel("วันที่รับไม้เข้า: "), self.dateEditInputWood)
        self.bottomLayout.addRow(QLabel("รหัสไม้: "), self.woodidEntry)
        self.bottomLayout.addRow(QLabel("ประเภทไม้: "), self.woodtypeCombobox)
        self.bottomLayout.addRow(QLabel("หนา: "), self.thickCombobox)
        self.bottomLayout.addRow(QLabel("กว้าง: "), self.wideCombobox)
        self.bottomLayout.addRow(QLabel("ยาว: "), self.longCombobox)
        self.bottomLayout.addRow(QLabel("ปริมาตร: "), self.volomeEntry)
        self.bottomLayout.addRow(QLabel("Supplier: "), self.supplierEntry)
        self.bottomFrame.setLayout(self.bottomLayout)
        # self.bottomFrame.setLayout(self.btnbox)

        self.mainLayout.addWidget(self.text)
        # self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.mainLayout.addLayout(self.btnbox)
        # self.mainLayout.addLayout(self.btnbox)
        self.setLayout(self.mainLayout)

    # Update
    def funcUpdateInfo(self):
        date = self.dateEditInputWood.text()
        id = self.woodidEntry.text()
        type = self.woodtypeCombobox.currentText()
        thick = int(self.thickCombobox.currentText())
        wide = int(self.wideCombobox.currentText())
        long = int(self.longCombobox.currentText())
        volume = int(self.volomeEntry.text())
        supplier = self.supplierEntry.text()

    #
    def funcQmessbox(self):
        global gid
        date = self.dateEditInputWood.text()
        id = self.woodidEntry.text()
        type = self.woodtypeCombobox.currentText()
        thick = int(self.thickCombobox.currentText())
        wide = int(self.wideCombobox.currentText())
        long = int(self.longCombobox.currentText())
        volume = float(self.volomeEntry.text())
        supplier = self.supplierEntry.text()
        check = self.check


        if (date !=  ""):
            try:
                print(">>",date)
                sql = db.updateInputTable(date)

            except:
                pass

        msg = QMessageBox()
        msg.setWindowTitle("info")
        msg.setText("Please check the accuracy of the information.")
        msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msg.exec_()
        self.close()

    # Cancel
    def funcClosedbox(self):
        self.close()