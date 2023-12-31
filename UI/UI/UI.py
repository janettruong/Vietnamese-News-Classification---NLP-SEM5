# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V:\NLP\Project\UI\NLP.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LabelPrediction(object):
    def setupUi(self, LabelPrediction):
        LabelPrediction.setObjectName("LabelPrediction")
        LabelPrediction.resize(1159, 659)
        self.centralwidget = QtWidgets.QWidget(LabelPrediction)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_7 = QtWidgets.QLabel(self.centralwidget)
        self.bg_7.setGeometry(QtCore.QRect(0, 0, 1161, 131))
        self.bg_7.setStyleSheet("background-image: url(uehlogo.png);")
        self.bg_7.setText("")
        self.bg_7.setPixmap(QtGui.QPixmap("uehlogo.png"))
        self.bg_7.setScaledContents(True)
        self.bg_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.bg_7.setObjectName("bg_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 130, 1311, 691))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setStyleSheet("font: 87 12pt \"Segoe UI Black\";")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.INTRODUCTION = QtWidgets.QWidget()
        self.INTRODUCTION.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.INTRODUCTION.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.INTRODUCTION.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.INTRODUCTION.setObjectName("INTRODUCTION")
        self.intro = QtWidgets.QLabel(self.INTRODUCTION)
        self.intro.setGeometry(QtCore.QRect(0, 0, 1161, 471))
        self.intro.setStyleSheet("background-image: url(intro.png);")
        self.intro.setText("")
        self.intro.setPixmap(QtGui.QPixmap("intro.png"))
        self.intro.setScaledContents(True)
        self.intro.setObjectName("intro")
        self.tabWidget.addTab(self.INTRODUCTION, "")
        self.PREVIEW = QtWidgets.QWidget()
        self.PREVIEW.setObjectName("PREVIEW")
        self.preview = QtWidgets.QLabel(self.PREVIEW)
        self.preview.setGeometry(QtCore.QRect(0, 0, 1161, 471))
        self.preview.setStyleSheet("background-image: url(previewfn.png);")
        self.preview.setText("")
        self.preview.setPixmap(QtGui.QPixmap("previewfn.png"))
        self.preview.setScaledContents(True)
        self.preview.setObjectName("preview")
        self.fileinputButton = QtWidgets.QPushButton(self.PREVIEW)
        self.fileinputButton.setGeometry(QtCore.QRect(560, 90, 71, 81))
        self.fileinputButton.setAutoFillBackground(False)
        self.fileinputButton.setStyleSheet("background-image: url(inputfile.png);")
        self.fileinputButton.setText("")
        self.fileinputButton.setIconSize(QtCore.QSize(20, 20))
        self.fileinputButton.setCheckable(False)
        self.fileinputButton.setAutoExclusive(True)
        self.fileinputButton.setAutoRepeatDelay(300)
        self.fileinputButton.setAutoDefault(False)
        self.fileinputButton.setObjectName("fileinputButton")
        self.label = QtWidgets.QLabel(self.PREVIEW)
        self.label.setGeometry(QtCore.QRect(70, 90, 461, 361))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setLineWidth(2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-image: url(timetrain.png);")
        self.label.setPixmap(QtGui.QPixmap("timetrain.png"))
        self.label.setScaledContents(True)
        self.tabWidget.addTab(self.PREVIEW, "")
        self.PREDICT = QtWidgets.QWidget()
        self.PREDICT.setObjectName("PREDICT")
        self.bgpredict = QtWidgets.QLabel(self.PREDICT)
        self.bgpredict.setGeometry(QtCore.QRect(0, 0, 1161, 471))
        self.bgpredict.setStyleSheet("background-image: url(PREDICT.png);")
        self.bgpredict.setText("")
        self.bgpredict.setPixmap(QtGui.QPixmap("PREDICT.png"))
        self.bgpredict.setScaledContents(True)
        self.bgpredict.setObjectName("bgpredict")
        self.inputText = QtWidgets.QLineEdit(self.PREDICT)
        self.inputText.setGeometry(QtCore.QRect(300, 90, 721, 61))
        self.inputText.setStyleSheet("font: 12pt \"Segoe UI Light\";")
        self.inputText.setObjectName("inputText")
        self.timesvmOuput = QtWidgets.QTableWidget(self.PREDICT)
        self.timesvmOuput.setGeometry(QtCore.QRect(160, 400, 231, 51))
        self.timesvmOuput.setMouseTracking(False)
        self.timesvmOuput.setTabletTracking(False)
        self.timesvmOuput.setAcceptDrops(False)
        self.timesvmOuput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timesvmOuput.setAutoFillBackground(False)
        self.timesvmOuput.setStyleSheet("font: 12pt \"Segoe UI Black\";")
        self.timesvmOuput.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.timesvmOuput.setShowGrid(False)
        self.timesvmOuput.setWordWrap(True)
        self.timesvmOuput.setRowCount(0)
        self.timesvmOuput.setColumnCount(0)
        self.timesvmOuput.setObjectName("timesvmOuput")
        self.timebag = QtWidgets.QLabel(self.PREDICT)
        self.timebag.setGeometry(QtCore.QRect(60, 400, 101, 51))
        self.timebag.setStyleSheet("background-image: url(Time.png);")
        self.timebag.setText("")
        self.timebag.setPixmap(QtGui.QPixmap("Time.png"))
        self.timebag.setScaledContents(True)
        self.timebag.setObjectName("timebag")
        self.bg = QtWidgets.QLabel(self.PREDICT)
        self.bg.setGeometry(QtCore.QRect(60, 240, 331, 161))
        self.bg.setStyleSheet("background-image: url(background.png);")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.bg_2 = QtWidgets.QLabel(self.PREDICT)
        self.bg_2.setGeometry(QtCore.QRect(410, 240, 331, 161))
        self.bg_2.setStyleSheet("background-image: url(background.png);")
        self.bg_2.setText("")
        self.bg_2.setObjectName("bg_2")
        self.bg_3 = QtWidgets.QLabel(self.PREDICT)
        self.bg_3.setGeometry(QtCore.QRect(760, 240, 331, 161))
        self.bg_3.setStyleSheet("background-image: url(background.png);")
        self.bg_3.setText("")
        self.bg_3.setObjectName("bg_3")
        self.accbg = QtWidgets.QLabel(self.PREDICT)
        self.accbg.setGeometry(QtCore.QRect(410, 400, 101, 51))
        self.accbg.setStyleSheet("background-image: url(Time.png);")
        self.accbg.setText("")
        self.accbg.setPixmap(QtGui.QPixmap("Time.png"))
        self.accbg.setScaledContents(True)
        self.accbg.setObjectName("accbg")
        self.timemaxentOuput = QtWidgets.QTableWidget(self.PREDICT)
        self.timemaxentOuput.setGeometry(QtCore.QRect(510, 400, 231, 51))
        self.timemaxentOuput.setMouseTracking(False)
        self.timemaxentOuput.setTabletTracking(False)
        self.timemaxentOuput.setAcceptDrops(False)
        self.timemaxentOuput.setAutoFillBackground(False)
        self.timemaxentOuput.setStyleSheet("font: 12pt \"Segoe UI Black\";")
        self.timemaxentOuput.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.timemaxentOuput.setObjectName("timemaxentOuput")
        self.timemaxentOuput.setColumnCount(0)
        self.timemaxentOuput.setRowCount(0)
        self.accbg_2 = QtWidgets.QLabel(self.PREDICT)
        self.accbg_2.setGeometry(QtCore.QRect(760, 400, 101, 51))
        self.accbg_2.setStyleSheet("background-image: url(Time.png);")
        self.accbg_2.setText("")
        self.accbg_2.setPixmap(QtGui.QPixmap("Time.png"))
        self.accbg_2.setScaledContents(True)
        self.accbg_2.setObjectName("accbg_2")
        self.timelstmOutput = QtWidgets.QTableWidget(self.PREDICT)
        self.timelstmOutput.setGeometry(QtCore.QRect(860, 400, 231, 51))
        self.timelstmOutput.setMouseTracking(False)
        self.timelstmOutput.setTabletTracking(False)
        self.timelstmOutput.setAcceptDrops(False)
        self.timelstmOutput.setAutoFillBackground(False)
        self.timelstmOutput.setStyleSheet("font: 12pt \"Segoe UI Black\";")
        self.timelstmOutput.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.timelstmOutput.setObjectName("timelstmOutput")
        self.timelstmOutput.setColumnCount(0)
        self.timelstmOutput.setRowCount(0)
        self.bg_4 = QtWidgets.QLabel(self.PREDICT)
        self.bg_4.setGeometry(QtCore.QRect(110, 250, 241, 31))
        self.bg_4.setStyleSheet("font: 25 14pt \"Segoe UI Light\";\n"
"")
        self.bg_4.setObjectName("bg_4")
        self.bg_5 = QtWidgets.QLabel(self.PREDICT)
        self.bg_5.setGeometry(QtCore.QRect(540, 250, 71, 31))
        self.bg_5.setStyleSheet("font: 25 14pt \"Segoe UI Light\";\n"
"")
        self.bg_5.setScaledContents(False)
        self.bg_5.setObjectName("bg_5")
        self.bg_6 = QtWidgets.QLabel(self.PREDICT)
        self.bg_6.setGeometry(QtCore.QRect(800, 250, 251, 31))
        self.bg_6.setStyleSheet("font: 25 14pt \"Segoe UI Light\";\n"
"")
        self.bg_6.setObjectName("bg_6")
        self.findButton = QtWidgets.QPushButton(self.PREDICT)
        self.findButton.setGeometry(QtCore.QRect(1030, 90, 61, 61))
        self.findButton.setStyleSheet("background-image: url(search.png);")
        self.findButton.setText("")
        self.findButton.setAutoDefault(False)
        self.findButton.setObjectName("findButton")
        self.timebag_2 = QtWidgets.QLabel(self.PREDICT)
        self.timebag_2.setGeometry(QtCore.QRect(410, 400, 101, 51))
        self.timebag_2.setStyleSheet("background-image: url(Time.png);")
        self.timebag_2.setText("")
        self.timebag_2.setPixmap(QtGui.QPixmap("Time.png"))
        self.timebag_2.setScaledContents(True)
        self.timebag_2.setObjectName("timebag_2")
        self.timebag_3 = QtWidgets.QLabel(self.PREDICT)
        self.timebag_3.setGeometry(QtCore.QRect(760, 400, 101, 51))
        self.timebag_3.setStyleSheet("background-image: url(Time.png);")
        self.timebag_3.setText("")
        self.timebag_3.setPixmap(QtGui.QPixmap("Time.png"))
        self.timebag_3.setScaledContents(True)
        self.timebag_3.setObjectName("timebag_3")
        self.svm = QtWidgets.QLabel(self.PREDICT)
        self.svm.setGeometry(QtCore.QRect(56, 280, 341, 121))
        self.svm.setFrameShape(QtWidgets.QFrame.Box)
        self.svm.setFrameShadow(QtWidgets.QFrame.Plain)
        self.svm.setLineWidth(3)
        self.svm.setText("")
        self.svm.setObjectName("svm")
        self.maxent = QtWidgets.QLabel(self.PREDICT)
        self.maxent.setGeometry(QtCore.QRect(410, 280, 331, 121))
        self.maxent.setFrameShape(QtWidgets.QFrame.Box)
        self.maxent.setLineWidth(3)
        self.maxent.setText("")
        self.maxent.setObjectName("maxent")
        self.label_2 = QtWidgets.QLabel(self.PREDICT)
        self.label_2.setGeometry(QtCore.QRect(760, 280, 331, 121))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(3)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.outsvm = QtWidgets.QLabel(self.PREDICT)
        self.outsvm.setGeometry(QtCore.QRect(180, 400, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.outsvm.setFont(font)
        self.outsvm.setText("")
        self.outsvm.setObjectName("outsvm")
        self.outmaxent = QtWidgets.QLabel(self.PREDICT)
        self.outmaxent.setGeometry(QtCore.QRect(530, 400, 201, 51))
        self.outmaxent.setText("")
        self.outmaxent.setObjectName("outmaxent")
        self.outlstm = QtWidgets.QLabel(self.PREDICT)
        self.outlstm.setGeometry(QtCore.QRect(880, 400, 211, 51))
        self.outlstm.setText("")
        self.outlstm.setObjectName("outlstm")
        self.bgpredict.raise_()
        self.bg.raise_()
        self.inputText.raise_()
        self.timesvmOuput.raise_()
        self.timebag.raise_()
        self.bg_2.raise_()
        self.bg_3.raise_()
        self.accbg.raise_()
        self.timemaxentOuput.raise_()
        self.accbg_2.raise_()
        self.timelstmOutput.raise_()
        self.bg_4.raise_()
        self.bg_5.raise_()
        self.bg_6.raise_()
        self.findButton.raise_()
        self.timebag_2.raise_()
        self.timebag_3.raise_()
        self.svm.raise_()
        self.maxent.raise_()
        self.label_2.raise_()
        self.outsvm.raise_()
        self.outmaxent.raise_()
        self.outlstm.raise_()
        self.tabWidget.addTab(self.PREDICT, "")
        self.bg_8 = QtWidgets.QLabel(self.centralwidget)
        self.bg_8.setGeometry(QtCore.QRect(0, 130, 1161, 41))
        self.bg_8.setStyleSheet("background-image: url(background.png);")
        self.bg_8.setText("")
        self.bg_8.setObjectName("bg_8")
        self.bg_8.raise_()
        self.bg_7.raise_()
        self.tabWidget.raise_()
        LabelPrediction.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LabelPrediction)
        self.statusbar.setObjectName("statusbar")
        LabelPrediction.setStatusBar(self.statusbar)

        self.retranslateUi(LabelPrediction)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(LabelPrediction)

    def retranslateUi(self, LabelPrediction):
        _translate = QtCore.QCoreApplication.translate
        LabelPrediction.setWindowTitle(_translate("LabelPrediction", "Label Prediction"))
        self.INTRODUCTION.setAccessibleName(_translate("LabelPrediction", "INTRDUCTION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.INTRODUCTION), _translate("LabelPrediction", "INTRODUCTION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PREVIEW), _translate("LabelPrediction", "PREVIEW"))
        self.inputText.setWhatsThis(_translate("LabelPrediction", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.timesvmOuput.setWhatsThis(_translate("LabelPrediction", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.timemaxentOuput.setWhatsThis(_translate("LabelPrediction", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.timelstmOutput.setWhatsThis(_translate("LabelPrediction", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.bg_4.setText(_translate("LabelPrediction", "Support Vector Machine"))
        self.bg_5.setToolTip(_translate("LabelPrediction", "<html><head/><body><p align=\"center\">Maxent</p></body></html>"))
        self.bg_5.setWhatsThis(_translate("LabelPrediction", "<html><head/><body><p align=\"center\">Maxent</p></body></html>"))
        self.bg_5.setText(_translate("LabelPrediction", "Maxent"))
        self.bg_6.setText(_translate("LabelPrediction", "Long-Short Term Memory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PREDICT), _translate("LabelPrediction", "PREDICT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelPrediction = QtWidgets.QMainWindow()
    ui = Ui_LabelPrediction()
    ui.setupUi(LabelPrediction)
    LabelPrediction.show()
    sys.exit(app.exec_())
