# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(891, 600)
        Client.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Client.setWhatsThis("")
        self.gridLayout = QtWidgets.QGridLayout(Client)
        self.gridLayout.setObjectName("gridLayout")
        self.yearQuarterLabel = QtWidgets.QLabel(Client)
        self.yearQuarterLabel.setObjectName("yearQuarterLabel")
        self.gridLayout.addWidget(self.yearQuarterLabel, 0, 9, 1, 1)
        self.yearQuarterField = QtWidgets.QSpinBox(Client)
        self.yearQuarterField.setMinimumSize(QtCore.QSize(100, 20))
        self.yearQuarterField.setMaximumSize(QtCore.QSize(100, 20))
        self.yearQuarterField.setAlignment(QtCore.Qt.AlignCenter)
        self.yearQuarterField.setMinimum(1)
        self.yearQuarterField.setMaximum(15)
        self.yearQuarterField.setProperty("value", 4)
        self.yearQuarterField.setObjectName("yearQuarterField")
        self.gridLayout.addWidget(self.yearQuarterField, 1, 9, 1, 1)
        self.searchLabel = QtWidgets.QLabel(Client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLabel.sizePolicy().hasHeightForWidth())
        self.searchLabel.setSizePolicy(sizePolicy)
        self.searchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchLabel.setObjectName("searchLabel")
        self.gridLayout.addWidget(self.searchLabel, 0, 4, 1, 1)
        self.searchButton = QtWidgets.QPushButton(Client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QtCore.QSize(100, 25))
        self.searchButton.setMaximumSize(QtCore.QSize(100, 25))
        self.searchButton.setMouseTracking(False)
        self.searchButton.setTabletTracking(False)
        self.searchButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.searchButton.setCheckable(False)
        self.searchButton.setAutoDefault(False)
        self.searchButton.setDefault(True)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 1, 10, 1, 1)
        self.getTimeLabel = QtWidgets.QLabel(Client)
        self.getTimeLabel.setObjectName("getTimeLabel")
        self.gridLayout.addWidget(self.getTimeLabel, 0, 7, 1, 1)
        self.typeFinanceLabel = QtWidgets.QLabel(Client)
        self.typeFinanceLabel.setObjectName("typeFinanceLabel")
        self.gridLayout.addWidget(self.typeFinanceLabel, 0, 6, 1, 1)
        self.typeFinanceField = QtWidgets.QComboBox(Client)
        self.typeFinanceField.setMinimumSize(QtCore.QSize(175, 20))
        self.typeFinanceField.setMaximumSize(QtCore.QSize(175, 20))
        self.typeFinanceField.setObjectName("typeFinanceField")
        self.typeFinanceField.addItem("")
        self.typeFinanceField.addItem("")
        self.typeFinanceField.addItem("")
        self.typeFinanceField.addItem("")
        self.gridLayout.addWidget(self.typeFinanceField, 1, 6, 1, 1)
        self.searchField = QtWidgets.QLineEdit(Client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchField.sizePolicy().hasHeightForWidth())
        self.searchField.setSizePolicy(sizePolicy)
        self.searchField.setMinimumSize(QtCore.QSize(225, 20))
        self.searchField.setMaximumSize(QtCore.QSize(16777215, 20))
        self.searchField.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.searchField.setInputMethodHints(QtCore.Qt.ImhNone)
        self.searchField.setText("")
        self.searchField.setMaxLength(15)
        self.searchField.setObjectName("searchField")
        self.gridLayout.addWidget(self.searchField, 1, 4, 1, 2)
        self.getDateButton = QtWidgets.QDateEdit(Client)
        self.getDateButton.setMinimumSize(QtCore.QSize(100, 20))
        self.getDateButton.setMaximumSize(QtCore.QSize(100, 20))
        self.getDateButton.setAlignment(QtCore.Qt.AlignCenter)
        self.getDateButton.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.getDateButton.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 12, 31), QtCore.QTime(23, 59, 59)))
        self.getDateButton.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2005, 1, 1), QtCore.QTime(0, 0, 0)))
        self.getDateButton.setMaximumDate(QtCore.QDate(2022, 12, 31))
        self.getDateButton.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.getDateButton.setCalendarPopup(False)
        self.getDateButton.setTimeSpec(QtCore.Qt.LocalTime)
        self.getDateButton.setDate(QtCore.QDate(2022, 1, 1))
        self.getDateButton.setObjectName("getDateButton")
        self.gridLayout.addWidget(self.getDateButton, 1, 7, 1, 1)
        self.financeLabel = QtWidgets.QLabel(Client)
        self.financeLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.financeLabel.sizePolicy().hasHeightForWidth())
        self.financeLabel.setSizePolicy(sizePolicy)
        self.financeLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.financeLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.financeLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.financeLabel.setAcceptDrops(False)
        self.financeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.financeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.financeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.financeLabel.setWordWrap(False)
        self.financeLabel.setObjectName("financeLabel")
        self.gridLayout.addWidget(self.financeLabel, 3, 4, 1, 1)
        self.yearCheckBox = QtWidgets.QCheckBox(Client)
        self.yearCheckBox.setMinimumSize(QtCore.QSize(100, 20))
        self.yearCheckBox.setMaximumSize(QtCore.QSize(100, 20))
        self.yearCheckBox.setObjectName("yearCheckBox")
        self.gridLayout.addWidget(self.yearCheckBox, 1, 8, 1, 1)
        self.dataTable = QtWidgets.QTableView(Client)
        self.dataTable.setObjectName("dataTable")
        self.gridLayout.addWidget(self.dataTable, 4, 4, 1, 7)

        self.retranslateUi(Client)
        self.searchField.textChanged['QString'].connect(self.searchButton.click)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", "Báo cáo tài chính"))
        self.yearQuarterLabel.setText(_translate("Client", "Số quý / năm cần lấy"))
        self.searchLabel.setText(_translate("Client", "Tìm kiếm"))
        self.searchButton.setText(_translate("Client", "Tìm kiếm"))
        self.getTimeLabel.setText(_translate("Client", "Thời gian"))
        self.typeFinanceLabel.setText(_translate("Client", "Loại BCTC"))
        self.typeFinanceField.setItemText(0, _translate("Client", "Cân đối kế toán"))
        self.typeFinanceField.setItemText(1, _translate("Client", "Kết quả kinh doanh"))
        self.typeFinanceField.setItemText(2, _translate("Client", "Lưu chuyển tiền tệ (trực tiếp)"))
        self.typeFinanceField.setItemText(3, _translate("Client", "Lưu chuyển tiền tệ (gián tiếp)"))
        self.searchField.setPlaceholderText(_translate("Client", "Nhập mã chứng khoán cần tìm BCTC"))
        self.getDateButton.setDisplayFormat(_translate("Client", "MM/yyyy"))
        self.financeLabel.setText(_translate("Client", "Thông tin báo cáo tài chính"))
        self.yearCheckBox.setText(_translate("Client", "Lấy theo năm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Client = QtWidgets.QDialog()
    ui = Ui_Client()
    ui.setupUi(Client)
    Client.show()
    sys.exit(app.exec_())