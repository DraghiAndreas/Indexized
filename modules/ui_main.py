# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKFuNUd.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 691)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setAutoFillBackground(False)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(36,36,36,255);\n"
"	border: 2px solid rgb(10, 10, 10);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgba(0,170,118,255);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"#bgApp {\n"
"	background-color: #14181c;\n"
"	border: 1px rgb(36,36,36)\n"
"}\n"
"/* /////////////////////////////////////////////////////////////"
                        "////////////////////////////////////\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgba(16,16,16,255);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgba(16,16,16,255);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgba(0,170,118,255); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgba(35,35,35,255);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgba(0,170,118,255);\n"
""
                        "	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgba(36,36,36,255);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgba(0,170,118,255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgba(0,170,118,255);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgba(35,35,35,255);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgba(36,36,36,255);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgba(0,1"
                        "70,118,255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgba(16,16,16,255);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgba(0,170,118,255)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgba(0,170,118,255); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	bord"
                        "er-top: 3px solid rgba(0,170,118,255);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgba(36,36,36,255);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgba(0,170,118,255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgba(16,16,16,255);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgba(0,170,118,255);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgba(36,36"
                        ",36,255); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgba(16,16,16,255); }\n"
"#themeSettingsTopDetail { background-color: rgba(0,170,118,255); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgba(16,16,16,255); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgba(36,36,36,255);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgba("
                        "0,170,118,255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	padding: 10px;\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgba(0,170,118,255);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb"
                        "(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);"
                        "\n"
"	selection-background-color: rgba(0,170,118,255);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(16,16,16,255);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(0,170,118,255);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(16,16,16,255);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"   "
                        " subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(16,16,16,255);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgba(16,16,16,255);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgba(0,170,118,255);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgba(16,14,16,255);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
""
                        "     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgba(16,16,16,255);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
""
                        "	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgba(25,25,25,255);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgba(42,42,42,255);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgba(0,170,118,255);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::d"
                        "rop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgba(0,170,118,255);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgba(16,16,16,255);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgba(16,16,16,255)\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    backgroun"
                        "d-color: rgba(0,170,118,255);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgba(0,170,118,255);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color:rgba(16,16,16,255);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgba(0,170,118,255);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgba(0,170,118,255);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////"
                        "//////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgba(0,170,118,255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgba(36,36,36,255);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgba(0,170,118,255);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(252,259, 172);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")
        self.btn_home.setAutoDefault(False)

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, 1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setStyleSheet(u"QPushButton:pressed {\n"
"        background-color: #2ecc71;  /* Pressed state (green) */\n"
"    }")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.extraContent)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: transparent; border:none;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_10.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)

        self.username_input = QTextEdit(self.frame_13)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setStyleSheet(u"background-color:#14181c;\n"
"")

        self.verticalLayout_10.addWidget(self.username_input)

        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_10.addWidget(self.frame_12)

        self.save_username_btn = QPushButton(self.frame_13)
        self.save_username_btn.setObjectName(u"save_username_btn")
        self.save_username_btn.setMinimumSize(QSize(150, 30))
        self.save_username_btn.setFont(font)
        self.save_username_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_username_btn.setStyleSheet(u"background-color: #1c2228;\n"
"border-radius:5px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_username_btn.setIcon(icon1)

        self.verticalLayout_10.addWidget(self.save_username_btn)

        self.verticalLayout_10.setStretch(0, 4)
        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_10.setStretch(2, 1)
        self.verticalLayout_10.setStretch(3, 2)
        self.verticalLayout_10.setStretch(4, 2)

        self.verticalLayout_12.addWidget(self.frame_13)

        self.frame_11 = QFrame(self.extraContent)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: transparent; border:none;")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.frame_11)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 5)

        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setStyleSheet(u"QPushButton:pressed {\n"
"        background-color: #2ecc71;  /* Pressed state (green) */\n"
"    }")
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsTopBtn.setStyleSheet(u"QPushButton:pressed {\n"
"        background-color: #2ecc71;  /* Pressed state (green) */\n"
"    }")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_20 = QVBoxLayout(self.home)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.home_upper = QFrame(self.home)
        self.home_upper.setObjectName(u"home_upper")
        self.home_upper.setFrameShape(QFrame.Shape.StyledPanel)
        self.home_upper.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.home_upper)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.welcome_label = QLabel(self.home_upper)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 50px;")
        self.welcome_label.setTextFormat(Qt.TextFormat.PlainText)
        self.welcome_label.setScaledContents(False)

        self.verticalLayout_21.addWidget(self.welcome_label)

        self.quote_label = QLabel(self.home_upper)
        self.quote_label.setObjectName(u"quote_label")
        self.quote_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_21.addWidget(self.quote_label)

        self.label_8 = QLabel(self.home_upper)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 15px;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_21.addWidget(self.label_8)

        self.date_label = QLabel(self.home_upper)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 15px;")

        self.verticalLayout_21.addWidget(self.date_label)

        self.separator_3 = QFrame(self.home_upper)
        self.separator_3.setObjectName(u"separator_3")
        self.separator_3.setStyleSheet(u"QFrame {\n"
"    border:11px solid;\n"
"	border-color: #363f44;\n"
"}")
        self.separator_3.setFrameShape(QFrame.Shape.HLine)
        self.separator_3.setFrameShadow(QFrame.Shadow.Plain)
        self.separator_3.setLineWidth(1)

        self.verticalLayout_21.addWidget(self.separator_3)


        self.verticalLayout_20.addWidget(self.home_upper)

        self.home_lower = QFrame(self.home)
        self.home_lower.setObjectName(u"home_lower")
        self.home_lower.setStyleSheet(u"")
        self.home_lower.setFrameShape(QFrame.Shape.StyledPanel)
        self.home_lower.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.home_lower)
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gainers_frame = QFrame(self.home_lower)
        self.gainers_frame.setObjectName(u"gainers_frame")
        self.gainers_frame.setStyleSheet(u"QFrame#gainers_frame QFrame {\n"
"    background-color: rgb(16,16,16);\n"
"	border-radius :7px;\n"
"}\n"
"")
        self.gainers_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.gainers_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.gainers_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.top_gainers_frame = QFrame(self.gainers_frame)
        self.top_gainers_frame.setObjectName(u"top_gainers_frame")
        self.top_gainers_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.top_gainers_frame.setStyleSheet(u"background-color:transparent;")
        self.top_gainers_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_gainers_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.top_gainers_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.top_gainers_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTabletTracking(False)
        self.label_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")
        self.label_3.setLineWidth(1)
        self.label_3.setMargin(0)
        self.label_3.setIndent(0)

        self.horizontalLayout_7.addWidget(self.label_3)


        self.verticalLayout_23.addWidget(self.top_gainers_frame)

        self.gainer1 = QFrame(self.gainers_frame)
        self.gainer1.setObjectName(u"gainer1")
        self.gainer1.setStyleSheet(u"QFrame#gainer1{\n"
"border: 1px solid #2ecc71;\n"
"}")
        self.gainer1.setFrameShape(QFrame.Shape.StyledPanel)
        self.gainer1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.gainer1)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(9, 0, -1, 0)
        self.g1_tick_label = QLabel(self.gainer1)
        self.g1_tick_label.setObjectName(u"g1_tick_label")
        self.g1_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.g1_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.g1_tick_label)

        self.g1_change_label = QLabel(self.gainer1)
        self.g1_change_label.setObjectName(u"g1_change_label")
        self.g1_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#2ecc71")
        self.g1_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.g1_change_label)


        self.verticalLayout_23.addWidget(self.gainer1)

        self.gainer2 = QFrame(self.gainers_frame)
        self.gainer2.setObjectName(u"gainer2")
        self.gainer2.setStyleSheet(u"QFrame#gainer2{\n"
"border: 1px solid #2ecc71;\n"
"}")
        self.gainer2.setFrameShape(QFrame.Shape.StyledPanel)
        self.gainer2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.gainer2)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 0, -1, 0)
        self.g2_tick_label = QLabel(self.gainer2)
        self.g2_tick_label.setObjectName(u"g2_tick_label")
        self.g2_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.g2_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.g2_tick_label)

        self.g2_change_label = QLabel(self.gainer2)
        self.g2_change_label.setObjectName(u"g2_change_label")
        self.g2_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#2ecc71")
        self.g2_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.g2_change_label)


        self.verticalLayout_23.addWidget(self.gainer2)

        self.gainer3 = QFrame(self.gainers_frame)
        self.gainer3.setObjectName(u"gainer3")
        self.gainer3.setStyleSheet(u"QFrame#gainer3{\n"
"border: 1px solid #2ecc71;\n"
"}")
        self.gainer3.setFrameShape(QFrame.Shape.StyledPanel)
        self.gainer3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.gainer3)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(9, 0, -1, 0)
        self.g3_tick_label = QLabel(self.gainer3)
        self.g3_tick_label.setObjectName(u"g3_tick_label")
        self.g3_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.g3_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.g3_tick_label)

        self.g3_change_label = QLabel(self.gainer3)
        self.g3_change_label.setObjectName(u"g3_change_label")
        self.g3_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#2ecc71")
        self.g3_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.g3_change_label)


        self.verticalLayout_23.addWidget(self.gainer3)

        self.gainer4 = QFrame(self.gainers_frame)
        self.gainer4.setObjectName(u"gainer4")
        self.gainer4.setStyleSheet(u"QFrame#gainer4{\n"
"border: 1px solid #2ecc71;\n"
"}")
        self.gainer4.setFrameShape(QFrame.Shape.StyledPanel)
        self.gainer4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.gainer4)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(9, 0, -1, 0)
        self.g4_tick_label = QLabel(self.gainer4)
        self.g4_tick_label.setObjectName(u"g4_tick_label")
        self.g4_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.g4_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.g4_tick_label)

        self.g4_change_label = QLabel(self.gainer4)
        self.g4_change_label.setObjectName(u"g4_change_label")
        self.g4_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#2ecc71")
        self.g4_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.g4_change_label)


        self.verticalLayout_23.addWidget(self.gainer4)

        self.gainer5 = QFrame(self.gainers_frame)
        self.gainer5.setObjectName(u"gainer5")
        self.gainer5.setStyleSheet(u"QFrame#gainer5{\n"
"border: 1px solid #2ecc71;\n"
"}")
        self.gainer5.setFrameShape(QFrame.Shape.StyledPanel)
        self.gainer5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.gainer5)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(9, 0, -1, 0)
        self.g5_tick_label = QLabel(self.gainer5)
        self.g5_tick_label.setObjectName(u"g5_tick_label")
        self.g5_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.g5_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.g5_tick_label)

        self.g5_change_label = QLabel(self.gainer5)
        self.g5_change_label.setObjectName(u"g5_change_label")
        self.g5_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#2ecc71")
        self.g5_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.g5_change_label)


        self.verticalLayout_23.addWidget(self.gainer5)


        self.horizontalLayout_6.addWidget(self.gainers_frame)

        self.losers_frame = QFrame(self.home_lower)
        self.losers_frame.setObjectName(u"losers_frame")
        self.losers_frame.setStyleSheet(u"QFrame#losers_frame QFrame {\n"
"    background-color: rgb(16,16,16);\n"
"	border-radius :7px;\n"
"}")
        self.losers_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.losers_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.losers_frame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.top_losers_frame = QFrame(self.losers_frame)
        self.top_losers_frame.setObjectName(u"top_losers_frame")
        self.top_losers_frame.setStyleSheet(u"background-color:transparent;")
        self.top_losers_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_losers_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.top_losers_frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_4 = QLabel(self.top_losers_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_27.addWidget(self.label_4)


        self.verticalLayout_24.addWidget(self.top_losers_frame)

        self.loser1 = QFrame(self.losers_frame)
        self.loser1.setObjectName(u"loser1")
        self.loser1.setStyleSheet(u"QFrame#loser1{\n"
"border: 1px solid #ff4143;\n"
"}")
        self.loser1.setFrameShape(QFrame.Shape.StyledPanel)
        self.loser1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.loser1)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(9, 0, -1, 0)
        self.l1_tick_label = QLabel(self.loser1)
        self.l1_tick_label.setObjectName(u"l1_tick_label")
        self.l1_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.l1_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.l1_tick_label)

        self.l1_change_label = QLabel(self.loser1)
        self.l1_change_label.setObjectName(u"l1_change_label")
        self.l1_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.l1_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.l1_change_label)


        self.verticalLayout_24.addWidget(self.loser1)

        self.loser2 = QFrame(self.losers_frame)
        self.loser2.setObjectName(u"loser2")
        self.loser2.setStyleSheet(u"QFrame#loser2{\n"
"border: 1px solid #ff4143;\n"
"}")
        self.loser2.setFrameShape(QFrame.Shape.StyledPanel)
        self.loser2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.loser2)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(9, 0, -1, 0)
        self.l2_tick_label = QLabel(self.loser2)
        self.l2_tick_label.setObjectName(u"l2_tick_label")
        self.l2_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.l2_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.l2_tick_label)

        self.l2_change_label = QLabel(self.loser2)
        self.l2_change_label.setObjectName(u"l2_change_label")
        self.l2_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.l2_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.l2_change_label)


        self.verticalLayout_24.addWidget(self.loser2)

        self.loser3 = QFrame(self.losers_frame)
        self.loser3.setObjectName(u"loser3")
        self.loser3.setStyleSheet(u"QFrame#loser3{\n"
"border: 1px solid #ff4143;\n"
"}")
        self.loser3.setFrameShape(QFrame.Shape.StyledPanel)
        self.loser3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.loser3)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(9, 0, -1, 0)
        self.l3_tick_label = QLabel(self.loser3)
        self.l3_tick_label.setObjectName(u"l3_tick_label")
        self.l3_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.l3_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.l3_tick_label)

        self.l3_change_label = QLabel(self.loser3)
        self.l3_change_label.setObjectName(u"l3_change_label")
        self.l3_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.l3_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.l3_change_label)


        self.verticalLayout_24.addWidget(self.loser3)

        self.loser4 = QFrame(self.losers_frame)
        self.loser4.setObjectName(u"loser4")
        self.loser4.setStyleSheet(u"QFrame#loser4{\n"
"border: 1px solid #ff4143;\n"
"}")
        self.loser4.setFrameShape(QFrame.Shape.StyledPanel)
        self.loser4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.loser4)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(9, 0, -1, 0)
        self.l4_tick_label = QLabel(self.loser4)
        self.l4_tick_label.setObjectName(u"l4_tick_label")
        self.l4_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.l4_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.l4_tick_label)

        self.l4_change_label = QLabel(self.loser4)
        self.l4_change_label.setObjectName(u"l4_change_label")
        self.l4_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.l4_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.l4_change_label)


        self.verticalLayout_24.addWidget(self.loser4)

        self.loser5 = QFrame(self.losers_frame)
        self.loser5.setObjectName(u"loser5")
        self.loser5.setStyleSheet(u"QFrame#loser5{\n"
"border: 1px solid #ff4143;\n"
"}")
        self.loser5.setFrameShape(QFrame.Shape.StyledPanel)
        self.loser5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.loser5)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 0, -1, 0)
        self.l5_tick_label = QLabel(self.loser5)
        self.l5_tick_label.setObjectName(u"l5_tick_label")
        self.l5_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.l5_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.l5_tick_label)

        self.l5_change_label = QLabel(self.loser5)
        self.l5_change_label.setObjectName(u"l5_change_label")
        self.l5_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.l5_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.l5_change_label)


        self.verticalLayout_24.addWidget(self.loser5)


        self.horizontalLayout_6.addWidget(self.losers_frame)

        self.currencies_frame = QFrame(self.home_lower)
        self.currencies_frame.setObjectName(u"currencies_frame")
        self.currencies_frame.setStyleSheet(u"QFrame#currencies_frame QFrame {\n"
"    background-color: rgb(16,16,16);\n"
"	border-radius :7px;\n"
"}\n"
"")
        self.currencies_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.currencies_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.currencies_frame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.test_frame = QFrame(self.currencies_frame)
        self.test_frame.setObjectName(u"test_frame")
        self.test_frame.setStyleSheet(u"background-color:transparent;")
        self.test_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.test_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.test_frame)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_5 = QLabel(self.test_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_28.addWidget(self.label_5)


        self.verticalLayout_25.addWidget(self.test_frame)

        self.currency1 = QFrame(self.currencies_frame)
        self.currency1.setObjectName(u"currency1")
        self.currency1.setFrameShape(QFrame.Shape.StyledPanel)
        self.currency1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.currency1)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.c1_tick_label = QLabel(self.currency1)
        self.c1_tick_label.setObjectName(u"c1_tick_label")
        self.c1_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.c1_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.c1_tick_label)

        self.c1_change_label = QLabel(self.currency1)
        self.c1_change_label.setObjectName(u"c1_change_label")
        self.c1_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.c1_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.c1_change_label)


        self.verticalLayout_25.addWidget(self.currency1)

        self.currency2 = QFrame(self.currencies_frame)
        self.currency2.setObjectName(u"currency2")
        self.currency2.setFrameShape(QFrame.Shape.StyledPanel)
        self.currency2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.currency2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.c2_tick_label = QLabel(self.currency2)
        self.c2_tick_label.setObjectName(u"c2_tick_label")
        self.c2_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.c2_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_30.addWidget(self.c2_tick_label)

        self.c2_change_label = QLabel(self.currency2)
        self.c2_change_label.setObjectName(u"c2_change_label")
        self.c2_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.c2_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_30.addWidget(self.c2_change_label)


        self.verticalLayout_25.addWidget(self.currency2)

        self.currency3 = QFrame(self.currencies_frame)
        self.currency3.setObjectName(u"currency3")
        self.currency3.setFrameShape(QFrame.Shape.StyledPanel)
        self.currency3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.currency3)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.c3_tick_label = QLabel(self.currency3)
        self.c3_tick_label.setObjectName(u"c3_tick_label")
        self.c3_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.c3_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.c3_tick_label)

        self.c3_change_label = QLabel(self.currency3)
        self.c3_change_label.setObjectName(u"c3_change_label")
        self.c3_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.c3_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.c3_change_label)


        self.verticalLayout_25.addWidget(self.currency3)

        self.currency4 = QFrame(self.currencies_frame)
        self.currency4.setObjectName(u"currency4")
        self.currency4.setFrameShape(QFrame.Shape.StyledPanel)
        self.currency4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.currency4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.c4_tick_label = QLabel(self.currency4)
        self.c4_tick_label.setObjectName(u"c4_tick_label")
        self.c4_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.c4_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_32.addWidget(self.c4_tick_label)

        self.c4_change_label = QLabel(self.currency4)
        self.c4_change_label.setObjectName(u"c4_change_label")
        self.c4_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.c4_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_32.addWidget(self.c4_change_label)


        self.verticalLayout_25.addWidget(self.currency4)

        self.currency5 = QFrame(self.currencies_frame)
        self.currency5.setObjectName(u"currency5")
        self.currency5.setFrameShape(QFrame.Shape.StyledPanel)
        self.currency5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.currency5)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.c5_tick_label = QLabel(self.currency5)
        self.c5_tick_label.setObjectName(u"c5_tick_label")
        self.c5_tick_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;")
        self.c5_tick_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_33.addWidget(self.c5_tick_label)

        self.c5_change_label = QLabel(self.currency5)
        self.c5_change_label.setObjectName(u"c5_change_label")
        self.c5_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 19px;color:#ff4143")
        self.c5_change_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_33.addWidget(self.c5_change_label)


        self.verticalLayout_25.addWidget(self.currency5)


        self.horizontalLayout_6.addWidget(self.currencies_frame)


        self.verticalLayout_20.addWidget(self.home_lower)

        self.verticalLayout_20.setStretch(0, 3)
        self.verticalLayout_20.setStretch(1, 6)
        self.stackedWidget.addWidget(self.home)
        self.portfolio = QWidget()
        self.portfolio.setObjectName(u"portfolio")
        self.verticalLayout_33 = QVBoxLayout(self.portfolio)
        self.verticalLayout_33.setSpacing(3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.all_holdings = QFrame(self.portfolio)
        self.all_holdings.setObjectName(u"all_holdings")
        self.all_holdings.setFrameShape(QFrame.Shape.StyledPanel)
        self.all_holdings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.all_holdings)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.text_label_1 = QLabel(self.all_holdings)
        self.text_label_1.setObjectName(u"text_label_1")
        self.text_label_1.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 13px;")

        self.verticalLayout_34.addWidget(self.text_label_1)

        self.all_holdings_label = QLabel(self.all_holdings)
        self.all_holdings_label.setObjectName(u"all_holdings_label")
        self.all_holdings_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 30px;")

        self.verticalLayout_34.addWidget(self.all_holdings_label)

        self.separator_4 = QFrame(self.all_holdings)
        self.separator_4.setObjectName(u"separator_4")
        self.separator_4.setStyleSheet(u"QFrame {\n"
"    border:11px solid;\n"
"	border-color: #363f44;\n"
"}")
        self.separator_4.setFrameShape(QFrame.Shape.HLine)
        self.separator_4.setFrameShadow(QFrame.Shadow.Plain)
        self.separator_4.setLineWidth(2)

        self.verticalLayout_34.addWidget(self.separator_4)


        self.verticalLayout_33.addWidget(self.all_holdings)

        self.holdings_data = QFrame(self.portfolio)
        self.holdings_data.setObjectName(u"holdings_data")
        self.holdings_data.setFrameShape(QFrame.Shape.StyledPanel)
        self.holdings_data.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.holdings_data)
        self.horizontalLayout_16.setSpacing(3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 3, -1, 3)
        self.holdings_data_1 = QFrame(self.holdings_data)
        self.holdings_data_1.setObjectName(u"holdings_data_1")
        self.holdings_data_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.holdings_data_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.holdings_data_1)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 3, -1, 3)
        self.price_ago_text = QLabel(self.holdings_data_1)
        self.price_ago_text.setObjectName(u"price_ago_text")
        self.price_ago_text.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 13px;")

        self.verticalLayout_35.addWidget(self.price_ago_text)

        self.price_ago_label = QLabel(self.holdings_data_1)
        self.price_ago_label.setObjectName(u"price_ago_label")
        self.price_ago_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 24px;")

        self.verticalLayout_35.addWidget(self.price_ago_label)


        self.horizontalLayout_16.addWidget(self.holdings_data_1)

        self.holdings_data_2 = QFrame(self.holdings_data)
        self.holdings_data_2.setObjectName(u"holdings_data_2")
        self.holdings_data_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.holdings_data_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.holdings_data_2)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, 3, -1, 3)
        self.period_change_text = QLabel(self.holdings_data_2)
        self.period_change_text.setObjectName(u"period_change_text")
        self.period_change_text.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 13px;")

        self.verticalLayout_36.addWidget(self.period_change_text)

        self.period_change = QLabel(self.holdings_data_2)
        self.period_change.setObjectName(u"period_change")
        self.period_change.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 23px;color:#2ecc71")

        self.verticalLayout_36.addWidget(self.period_change)


        self.horizontalLayout_16.addWidget(self.holdings_data_2)

        self.holdings_data_3 = QFrame(self.holdings_data)
        self.holdings_data_3.setObjectName(u"holdings_data_3")
        self.holdings_data_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.holdings_data_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.holdings_data_3)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, -1, 0)

        self.horizontalLayout_16.addWidget(self.holdings_data_3)

        self.empty_1 = QFrame(self.holdings_data)
        self.empty_1.setObjectName(u"empty_1")
        self.empty_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.empty_1.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_16.addWidget(self.empty_1)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 1)
        self.horizontalLayout_16.setStretch(3, 3)

        self.verticalLayout_33.addWidget(self.holdings_data)

        self.frame_14 = QFrame(self.portfolio)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.holdings_graph = QFrame(self.frame_14)
        self.holdings_graph.setObjectName(u"holdings_graph")
        self.holdings_graph.setFrameShape(QFrame.Shape.StyledPanel)
        self.holdings_graph.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.holdings_graph)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, 0, -1, 0)
        self.hg_buttons = QFrame(self.holdings_graph)
        self.hg_buttons.setObjectName(u"hg_buttons")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.hg_buttons.sizePolicy().hasHeightForWidth())
        self.hg_buttons.setSizePolicy(sizePolicy3)
        self.hg_buttons.setMinimumSize(QSize(0, 0))
        self.hg_buttons.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(16,16,16);\n"
"border: 1px solid rgb(16,16,16);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"background-color:rgb(45,45,45);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgb(0,170,118);\n"
"}")
        self.hg_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.hg_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.hg_buttons)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.hg_1d = QPushButton(self.hg_buttons)
        self.hg_1d.setObjectName(u"hg_1d")
        self.hg_1d.setCheckable(True)
        self.hg_1d.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.hg_1d)

        self.hg_5d = QPushButton(self.hg_buttons)
        self.hg_5d.setObjectName(u"hg_5d")
        self.hg_5d.setCheckable(True)
        self.hg_5d.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.hg_5d)

        self.hg_1mo = QPushButton(self.hg_buttons)
        self.hg_1mo.setObjectName(u"hg_1mo")
        self.hg_1mo.setCheckable(True)
        self.hg_1mo.setChecked(True)
        self.hg_1mo.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.hg_1mo)

        self.hg_6mo = QPushButton(self.hg_buttons)
        self.hg_6mo.setObjectName(u"hg_6mo")
        self.hg_6mo.setCheckable(True)
        self.hg_6mo.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.hg_6mo)

        self.hg_ytd = QPushButton(self.hg_buttons)
        self.hg_ytd.setObjectName(u"hg_ytd")
        self.hg_ytd.setCheckable(True)
        self.hg_ytd.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.hg_ytd)

        self.hg_1y = QPushButton(self.hg_buttons)
        self.hg_1y.setObjectName(u"hg_1y")
        self.hg_1y.setCheckable(True)
        self.hg_1y.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.hg_1y)

        self.horizontalLayout_17.setStretch(0, 4)
        self.horizontalLayout_17.setStretch(1, 4)
        self.horizontalLayout_17.setStretch(2, 4)
        self.horizontalLayout_17.setStretch(3, 4)
        self.horizontalLayout_17.setStretch(4, 4)
        self.horizontalLayout_17.setStretch(5, 4)

        self.verticalLayout_38.addWidget(self.hg_buttons)

        self.frame_19 = QFrame(self.holdings_graph)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 4, 0, 0)
        self.frame_15 = QFrame(self.frame_19)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: #14181c;\n"
"border: 1px solid;\n"
"border-radius: 5px;\n"
"border-color: #363f44;")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.frame_15)

        self.holdings_list_pie_2 = QFrame(self.frame_19)
        self.holdings_list_pie_2.setObjectName(u"holdings_list_pie_2")
        self.holdings_list_pie_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.holdings_list_pie_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.holdings_list_pie_2)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.holdings_list_pie_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_20)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_16)
        self.verticalLayout_42.setSpacing(6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 6, -1, 0)
        self.frame_21 = QFrame(self.frame_16)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 0, -1, 0)
        self.text_label_8 = QLabel(self.frame_21)
        self.text_label_8.setObjectName(u"text_label_8")
        self.text_label_8.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 17px;")
        self.text_label_8.setMargin(0)
        self.text_label_8.setIndent(0)

        self.horizontalLayout_38.addWidget(self.text_label_8)

        self.portfolio_combobox = QComboBox(self.frame_21)
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.addItem("")
        self.portfolio_combobox.setObjectName(u"portfolio_combobox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.portfolio_combobox.sizePolicy().hasHeightForWidth())
        self.portfolio_combobox.setSizePolicy(sizePolicy4)
        self.portfolio_combobox.setStyleSheet(u"background-color: rgba(16,16,16,255);\n"
"")

        self.horizontalLayout_38.addWidget(self.portfolio_combobox)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_38.addWidget(self.frame_22)

        self.horizontalLayout_38.setStretch(0, 20)
        self.horizontalLayout_38.setStretch(1, 30)
        self.horizontalLayout_38.setStretch(2, 30)

        self.verticalLayout_42.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_16)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, 0, -1, 0)
        self.text_label_9 = QLabel(self.frame_23)
        self.text_label_9.setObjectName(u"text_label_9")
        self.text_label_9.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 17px;")
        self.text_label_9.setMargin(0)
        self.text_label_9.setIndent(0)

        self.horizontalLayout_39.addWidget(self.text_label_9)

        self.portfolio_amount = QPlainTextEdit(self.frame_23)
        self.portfolio_amount.setObjectName(u"portfolio_amount")
        self.portfolio_amount.setEnabled(True)
        self.portfolio_amount.setMaximumSize(QSize(16777215, 49))
        self.portfolio_amount.setStyleSheet(u"background-color:rgb(16,16,16)")
        self.portfolio_amount.setTabStopDistance(10.000000000000000)
        self.portfolio_amount.setBackgroundVisible(False)

        self.horizontalLayout_39.addWidget(self.portfolio_amount)


        self.verticalLayout_42.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_16)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(16,16,16);\n"
"border: 1px solid rgb(16,16,16);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"background-color:rgb(45,45,45);\n"
"}")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.add_btn = QPushButton(self.frame_24)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(0, 30))
        self.add_btn.setCheckable(True)
        self.add_btn.setAutoExclusive(True)

        self.horizontalLayout_35.addWidget(self.add_btn)

        self.subtract_btn = QPushButton(self.frame_24)
        self.subtract_btn.setObjectName(u"subtract_btn")
        self.subtract_btn.setMinimumSize(QSize(0, 30))
        self.subtract_btn.setCheckable(True)
        self.subtract_btn.setAutoExclusive(True)

        self.horizontalLayout_35.addWidget(self.subtract_btn)

        self.delete_btn = QPushButton(self.frame_24)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(0, 30))
        self.delete_btn.setCheckable(True)
        self.delete_btn.setAutoExclusive(True)

        self.horizontalLayout_35.addWidget(self.delete_btn)

        self.reset_btn = QPushButton(self.frame_24)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setMinimumSize(QSize(0, 30))
        self.reset_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255,65,67);\n"
"border: 1px solid rgb(16,16,16);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,105,107);\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"background-color:rgb(255,145,147);\n"
"}")
        self.reset_btn.setCheckable(True)
        self.reset_btn.setAutoExclusive(True)

        self.horizontalLayout_35.addWidget(self.reset_btn)


        self.verticalLayout_42.addWidget(self.frame_24)


        self.horizontalLayout_28.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_20)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: transparent;")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.portfolio_table = QTableWidget(self.frame_17)
        self.portfolio_table.setObjectName(u"portfolio_table")
        self.portfolio_table.setStyleSheet(u"")

        self.horizontalLayout_36.addWidget(self.portfolio_table)


        self.horizontalLayout_28.addWidget(self.frame_17)

        self.horizontalLayout_28.setStretch(0, 1)
        self.horizontalLayout_28.setStretch(1, 1)

        self.horizontalLayout_37.addWidget(self.frame_20)

        self.horizontalLayout_37.setStretch(0, 2)

        self.verticalLayout_11.addWidget(self.holdings_list_pie_2)

        self.verticalLayout_11.setStretch(0, 4)
        self.verticalLayout_11.setStretch(1, 1)

        self.verticalLayout_38.addWidget(self.frame_19)


        self.horizontalLayout_34.addWidget(self.holdings_graph)

        self.holdings_pie_chart = QFrame(self.frame_14)
        self.holdings_pie_chart.setObjectName(u"holdings_pie_chart")
        self.holdings_pie_chart.setStyleSheet(u"background-color: #14181c;\n"
"border: 1px solid;\n"
"border-radius: 5px;\n"
"border-color: #363f44;")
        self.holdings_pie_chart.setFrameShape(QFrame.Shape.StyledPanel)
        self.holdings_pie_chart.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_34.addWidget(self.holdings_pie_chart)

        self.horizontalLayout_34.setStretch(0, 6)
        self.horizontalLayout_34.setStretch(1, 3)

        self.verticalLayout_33.addWidget(self.frame_14)

        self.verticalLayout_33.setStretch(0, 1)
        self.verticalLayout_33.setStretch(1, 1)
        self.verticalLayout_33.setStretch(2, 10)
        self.stackedWidget.addWidget(self.portfolio)
        self.graph = QWidget()
        self.graph.setObjectName(u"graph")
        self.graph.setStyleSheet(u"")
        self.verticalLayout_26 = QVBoxLayout(self.graph)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.graph_upper = QFrame(self.graph)
        self.graph_upper.setObjectName(u"graph_upper")
        self.graph_upper.setStyleSheet(u"")
        self.graph_upper.setFrameShape(QFrame.Shape.StyledPanel)
        self.graph_upper.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.graph_upper)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.graph_combo_frame = QFrame(self.graph_upper)
        self.graph_combo_frame.setObjectName(u"graph_combo_frame")
        self.graph_combo_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.graph_combo_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.graph_combo_frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.text_label_5 = QLabel(self.graph_combo_frame)
        self.text_label_5.setObjectName(u"text_label_5")
        self.text_label_5.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")
        self.text_label_5.setMargin(0)
        self.text_label_5.setIndent(0)

        self.verticalLayout_30.addWidget(self.text_label_5)

        self.graph_combo_box = QComboBox(self.graph_combo_frame)
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.addItem("")
        self.graph_combo_box.setObjectName(u"graph_combo_box")
        sizePolicy4.setHeightForWidth(self.graph_combo_box.sizePolicy().hasHeightForWidth())
        self.graph_combo_box.setSizePolicy(sizePolicy4)
        self.graph_combo_box.setStyleSheet(u"background-color: rgba(16,16,16,255);\n"
"")

        self.verticalLayout_30.addWidget(self.graph_combo_box)


        self.horizontalLayout_8.addWidget(self.graph_combo_frame)

        self.graph_buttons = QFrame(self.graph_upper)
        self.graph_buttons.setObjectName(u"graph_buttons")
        sizePolicy3.setHeightForWidth(self.graph_buttons.sizePolicy().hasHeightForWidth())
        self.graph_buttons.setSizePolicy(sizePolicy3)
        self.graph_buttons.setMinimumSize(QSize(0, 0))
        self.graph_buttons.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(16,16,16);\n"
"border: 1px solid rgb(16,16,16);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"background-color:rgb(45,45,45);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgb(0,170,118);\n"
"}")
        self.graph_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.graph_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.graph_buttons)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.g_1d = QPushButton(self.graph_buttons)
        self.g_1d.setObjectName(u"g_1d")
        self.g_1d.setCheckable(True)
        self.g_1d.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.g_1d)

        self.g_5d = QPushButton(self.graph_buttons)
        self.g_5d.setObjectName(u"g_5d")
        self.g_5d.setCheckable(True)
        self.g_5d.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.g_5d)

        self.g_1mo = QPushButton(self.graph_buttons)
        self.g_1mo.setObjectName(u"g_1mo")
        self.g_1mo.setCheckable(True)
        self.g_1mo.setChecked(True)
        self.g_1mo.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.g_1mo)

        self.g_6mo = QPushButton(self.graph_buttons)
        self.g_6mo.setObjectName(u"g_6mo")
        self.g_6mo.setCheckable(True)
        self.g_6mo.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.g_6mo)

        self.g_ytd = QPushButton(self.graph_buttons)
        self.g_ytd.setObjectName(u"g_ytd")
        self.g_ytd.setCheckable(True)
        self.g_ytd.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.g_ytd)

        self.g_1y = QPushButton(self.graph_buttons)
        self.g_1y.setObjectName(u"g_1y")
        self.g_1y.setCheckable(True)
        self.g_1y.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.g_1y)

        self.g_5y = QPushButton(self.graph_buttons)
        self.g_5y.setObjectName(u"g_5y")
        self.g_5y.setCheckable(True)
        self.g_5y.setChecked(False)
        self.g_5y.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.g_5y)

        self.g_max = QPushButton(self.graph_buttons)
        self.g_max.setObjectName(u"g_max")
        self.g_max.setCheckable(True)
        self.g_max.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.g_max)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.horizontalLayout_8.addWidget(self.graph_buttons)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 4)

        self.verticalLayout_26.addWidget(self.graph_upper)

        self.graph_lower = QFrame(self.graph)
        self.graph_lower.setObjectName(u"graph_lower")
        self.graph_lower.setStyleSheet(u"")
        self.graph_lower.setFrameShape(QFrame.Shape.StyledPanel)
        self.graph_lower.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.graph_lower)
        self.verticalLayout_31.setSpacing(2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, 0, -1, 0)
        self.g_name_data_frame = QFrame(self.graph_lower)
        self.g_name_data_frame.setObjectName(u"g_name_data_frame")
        self.g_name_data_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.g_name_data_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_32 = QVBoxLayout(self.g_name_data_frame)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.g_name_label = QLabel(self.g_name_data_frame)
        self.g_name_label.setObjectName(u"g_name_label")
        sizePolicy3.setHeightForWidth(self.g_name_label.sizePolicy().hasHeightForWidth())
        self.g_name_label.setSizePolicy(sizePolicy3)
        self.g_name_label.setMinimumSize(QSize(0, 0))
        self.g_name_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 25px;")

        self.verticalLayout_32.addWidget(self.g_name_label)

        self.separator_1 = QFrame(self.g_name_data_frame)
        self.separator_1.setObjectName(u"separator_1")
        self.separator_1.setStyleSheet(u"QFrame {\n"
"    border:11px solid;\n"
"	border-color: #363f44;\n"
"}")
        self.separator_1.setFrameShape(QFrame.Shape.HLine)
        self.separator_1.setFrameShadow(QFrame.Shadow.Plain)
        self.separator_1.setLineWidth(1)

        self.verticalLayout_32.addWidget(self.separator_1)

        self.g_data_frame = QFrame(self.g_name_data_frame)
        self.g_data_frame.setObjectName(u"g_data_frame")
        self.g_data_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.g_data_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.g_data_frame)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.g_price_label = QLabel(self.g_data_frame)
        self.g_price_label.setObjectName(u"g_price_label")
        self.g_price_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 27px;")

        self.horizontalLayout_13.addWidget(self.g_price_label)

        self.g_change_label = QLabel(self.g_data_frame)
        self.g_change_label.setObjectName(u"g_change_label")
        self.g_change_label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 18px;")

        self.horizontalLayout_13.addWidget(self.g_change_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_32.addWidget(self.g_data_frame)


        self.verticalLayout_31.addWidget(self.g_name_data_frame)

        self.frame_27 = QFrame(self.graph_lower)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.graph_frame = QFrame(self.frame_27)
        self.graph_frame.setObjectName(u"graph_frame")
        self.graph_frame.setStyleSheet(u"background-color: #14181c;\n"
"border: 1px solid;\n"
"border-radius: 5px;\n"
"border-color: #363f44;")
        self.graph_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.graph_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_14.addWidget(self.graph_frame)


        self.verticalLayout_31.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.graph_lower)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 14px;")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_26)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.low_label = QLabel(self.frame_26)
        self.low_label.setObjectName(u"low_label")

        self.gridLayout_3.addWidget(self.low_label, 3, 3, 1, 1)

        self.stckSplits_label = QLabel(self.frame_26)
        self.stckSplits_label.setObjectName(u"stckSplits_label")

        self.gridLayout_3.addWidget(self.stckSplits_label, 0, 5, 1, 1)

        self.open_label_2 = QLabel(self.frame_26)
        self.open_label_2.setObjectName(u"open_label_2")

        self.gridLayout_3.addWidget(self.open_label_2, 0, 0, 1, 1)

        self.date_label_2 = QLabel(self.frame_26)
        self.date_label_2.setObjectName(u"date_label_2")

        self.gridLayout_3.addWidget(self.date_label_2, 3, 5, 1, 1)

        self.high_label = QLabel(self.frame_26)
        self.high_label.setObjectName(u"high_label")

        self.gridLayout_3.addWidget(self.high_label, 0, 3, 1, 1)

        self.volume_label = QLabel(self.frame_26)
        self.volume_label.setObjectName(u"volume_label")

        self.gridLayout_3.addWidget(self.volume_label, 0, 4, 1, 1)

        self.div_label = QLabel(self.frame_26)
        self.div_label.setObjectName(u"div_label")

        self.gridLayout_3.addWidget(self.div_label, 3, 4, 1, 1)

        self.close_label = QLabel(self.frame_26)
        self.close_label.setObjectName(u"close_label")

        self.gridLayout_3.addWidget(self.close_label, 3, 0, 1, 1)


        self.verticalLayout_31.addWidget(self.frame_26)

        self.verticalLayout_31.setStretch(0, 2)
        self.verticalLayout_31.setStretch(1, 8)
        self.verticalLayout_31.setStretch(2, 3)

        self.verticalLayout_26.addWidget(self.graph_lower)

        self.verticalLayout_26.setStretch(1, 1)
        self.stackedWidget.addWidget(self.graph)
        self.funds = QWidget()
        self.funds.setObjectName(u"funds")
        self.funds.setStyleSheet(u"border: none;")
        self.verticalLayout_22 = QVBoxLayout(self.funds)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame = QFrame(self.funds)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.all_holdings_label_2 = QLabel(self.frame)
        self.all_holdings_label_2.setObjectName(u"all_holdings_label_2")
        self.all_holdings_label_2.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 30px;")

        self.verticalLayout_41.addWidget(self.all_holdings_label_2)

        self.separator_2 = QFrame(self.frame)
        self.separator_2.setObjectName(u"separator_2")
        self.separator_2.setStyleSheet(u"QFrame {\n"
"    border:2px solid white; \n"
"}")
        self.separator_2.setFrameShape(QFrame.Shape.HLine)
        self.separator_2.setFrameShadow(QFrame.Shadow.Plain)
        self.separator_2.setLineWidth(2)

        self.verticalLayout_41.addWidget(self.separator_2)


        self.verticalLayout_22.addWidget(self.frame)

        self.frame_2 = QFrame(self.funds)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_3)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_5)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_40.addWidget(self.label)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 12px;")

        self.verticalLayout_40.addWidget(self.label_2)


        self.verticalLayout_39.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_7)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_48.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 12px;")

        self.verticalLayout_48.addWidget(self.label_27)


        self.verticalLayout_39.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_6)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_28 = QLabel(self.frame_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_49.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 12px;")

        self.verticalLayout_49.addWidget(self.label_29)


        self.verticalLayout_39.addWidget(self.frame_6)


        self.horizontalLayout_18.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_4)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_10)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_24 = QLabel(self.frame_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_47.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 12px;")

        self.verticalLayout_47.addWidget(self.label_25)


        self.verticalLayout_46.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_8)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_50.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 12px;")

        self.verticalLayout_50.addWidget(self.label_31)


        self.verticalLayout_46.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_9)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_32 = QLabel(self.frame_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 20px;")

        self.verticalLayout_51.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_9)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: bold \"Segoe UI\"; font-size: 12px;")

        self.verticalLayout_51.addWidget(self.label_33)


        self.verticalLayout_46.addWidget(self.frame_9)


        self.horizontalLayout_18.addWidget(self.frame_4)


        self.verticalLayout_22.addWidget(self.frame_2)

        self.verticalLayout_22.setStretch(0, 1)
        self.verticalLayout_22.setStretch(1, 4)
        self.stackedWidget.addWidget(self.funds)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgba(16,16,16,255);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgba(16,16,16,255);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgba(16,16,16,255); }\n"
" QScrollBar:horizontal { background: rgba(16,16,16,255); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgba(16,16,16,255);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgba(16,16,16,255);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgba(16,16,16,255); }\n"
" QScrollBar:horizontal { background: rgba(16,16,16,255); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setEnabled(True)
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy5)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setEnabled(True)
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setStyleSheet(u"color: rgb(255,255,255)")
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setStyleSheet(u"background-color: rgba(16,16,16,255)")
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setStyleSheet(u"color: rgb(255,255,255)")
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"color: rgb(255,255,255)")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_29.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
#if QT_CONFIG(shortcut)
        self.g_change_label.setBuddy(self.g_change_label)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Username must be between 0 and 30 characters", None))
        self.save_username_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Indexized", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"Welcome, User!", None))
        self.quote_label.setText(QCoreApplication.translate("MainWindow", u"*RANDOM INSPIRATIONAL QUOTE*", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"-Theodore Roosevelt", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TOP GAINERS", None))
        self.g1_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.g1_change_label.setText(QCoreApplication.translate("MainWindow", u"+1.1(+11%)", None))
        self.g2_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.g2_change_label.setText(QCoreApplication.translate("MainWindow", u"+1.1(+11%)", None))
        self.g3_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.g3_change_label.setText(QCoreApplication.translate("MainWindow", u"+1.1(+11%)", None))
        self.g4_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.g4_change_label.setText(QCoreApplication.translate("MainWindow", u"+1.1(+11%)", None))
        self.g5_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.g5_change_label.setText(QCoreApplication.translate("MainWindow", u"+1.1(+11%)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TOP LOSERS", None))
        self.l1_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.l1_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.l2_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.l2_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.l3_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.l3_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.l4_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.l4_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.l5_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.l5_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CURRENCIES (USD TO ...)", None))
        self.c1_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.c1_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.c2_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.c2_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.c3_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.c3_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.c4_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.c4_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.c5_tick_label.setText(QCoreApplication.translate("MainWindow", u"NIG : 11.11$", None))
        self.c5_change_label.setText(QCoreApplication.translate("MainWindow", u"-1.1(-11%)", None))
        self.portfolio.setStyleSheet("")
        self.text_label_1.setText(QCoreApplication.translate("MainWindow", u"All portfolio holdings :", None))
        self.all_holdings_label.setText(QCoreApplication.translate("MainWindow", u"US$812.65", None))
        self.price_ago_text.setText(QCoreApplication.translate("MainWindow", u"Price __ ago: ", None))
        self.price_ago_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.period_change_text.setText(QCoreApplication.translate("MainWindow", u"Period Change:", None))
        self.period_change.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.hg_1d.setText(QCoreApplication.translate("MainWindow", u"1D", None))
        self.hg_5d.setText(QCoreApplication.translate("MainWindow", u"5D", None))
        self.hg_1mo.setText(QCoreApplication.translate("MainWindow", u"1M", None))
        self.hg_6mo.setText(QCoreApplication.translate("MainWindow", u"6M", None))
        self.hg_ytd.setText(QCoreApplication.translate("MainWindow", u"YTD", None))
        self.hg_1y.setText(QCoreApplication.translate("MainWindow", u"1Y", None))
        self.text_label_8.setText(QCoreApplication.translate("MainWindow", u"TICKERS:", None))
        self.portfolio_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"VTI", None))
        self.portfolio_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"SPY", None))
        self.portfolio_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"VOO", None))
        self.portfolio_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"SCHB", None))
        self.portfolio_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"DIA", None))
        self.portfolio_combobox.setItemText(5, QCoreApplication.translate("MainWindow", u"QQQ", None))
        self.portfolio_combobox.setItemText(6, QCoreApplication.translate("MainWindow", u"-------", None))
        self.portfolio_combobox.setItemText(7, QCoreApplication.translate("MainWindow", u"XLK", None))
        self.portfolio_combobox.setItemText(8, QCoreApplication.translate("MainWindow", u"XLF", None))
        self.portfolio_combobox.setItemText(9, QCoreApplication.translate("MainWindow", u"XLE", None))
        self.portfolio_combobox.setItemText(10, QCoreApplication.translate("MainWindow", u"XLY", None))
        self.portfolio_combobox.setItemText(11, QCoreApplication.translate("MainWindow", u"XLI", None))
        self.portfolio_combobox.setItemText(12, QCoreApplication.translate("MainWindow", u"XLV", None))
        self.portfolio_combobox.setItemText(13, QCoreApplication.translate("MainWindow", u"XLC", None))
        self.portfolio_combobox.setItemText(14, QCoreApplication.translate("MainWindow", u"XLU", None))
        self.portfolio_combobox.setItemText(15, QCoreApplication.translate("MainWindow", u"XLB", None))
        self.portfolio_combobox.setItemText(16, QCoreApplication.translate("MainWindow", u"XLRE", None))
        self.portfolio_combobox.setItemText(17, QCoreApplication.translate("MainWindow", u"VNQ", None))
        self.portfolio_combobox.setItemText(18, QCoreApplication.translate("MainWindow", u"-------", None))
        self.portfolio_combobox.setItemText(19, QCoreApplication.translate("MainWindow", u"VXUS", None))
        self.portfolio_combobox.setItemText(20, QCoreApplication.translate("MainWindow", u"IXUS", None))
        self.portfolio_combobox.setItemText(21, QCoreApplication.translate("MainWindow", u"VEU", None))
        self.portfolio_combobox.setItemText(22, QCoreApplication.translate("MainWindow", u"-------", None))
        self.portfolio_combobox.setItemText(23, QCoreApplication.translate("MainWindow", u"VIXY", None))
        self.portfolio_combobox.setItemText(24, QCoreApplication.translate("MainWindow", u"SH", None))
        self.portfolio_combobox.setItemText(25, QCoreApplication.translate("MainWindow", u"SQQQ", None))
        self.portfolio_combobox.setItemText(26, QCoreApplication.translate("MainWindow", u"-------", None))
        self.portfolio_combobox.setItemText(27, QCoreApplication.translate("MainWindow", u"BND", None))
        self.portfolio_combobox.setItemText(28, QCoreApplication.translate("MainWindow", u"AGG", None))
        self.portfolio_combobox.setItemText(29, QCoreApplication.translate("MainWindow", u"-------", None))
        self.portfolio_combobox.setItemText(30, QCoreApplication.translate("MainWindow", u"ARKK", None))
        self.portfolio_combobox.setItemText(31, QCoreApplication.translate("MainWindow", u"SOXX", None))

        self.text_label_9.setText(QCoreApplication.translate("MainWindow", u"AMOUNT: ", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.subtract_btn.setText(QCoreApplication.translate("MainWindow", u"SUBTRACT", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"RESET PORT", None))
        self.text_label_5.setText(QCoreApplication.translate("MainWindow", u"TICKERS", None))
        self.graph_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"VTI", None))
        self.graph_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"SPY", None))
        self.graph_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"VOO", None))
        self.graph_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"SCHB", None))
        self.graph_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"DIA", None))
        self.graph_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"QQQ", None))
        self.graph_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"-------", None))
        self.graph_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"XLK", None))
        self.graph_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"XLF", None))
        self.graph_combo_box.setItemText(9, QCoreApplication.translate("MainWindow", u"XLE", None))
        self.graph_combo_box.setItemText(10, QCoreApplication.translate("MainWindow", u"XLY", None))
        self.graph_combo_box.setItemText(11, QCoreApplication.translate("MainWindow", u"XLI", None))
        self.graph_combo_box.setItemText(12, QCoreApplication.translate("MainWindow", u"XLV", None))
        self.graph_combo_box.setItemText(13, QCoreApplication.translate("MainWindow", u"XLC", None))
        self.graph_combo_box.setItemText(14, QCoreApplication.translate("MainWindow", u"XLU", None))
        self.graph_combo_box.setItemText(15, QCoreApplication.translate("MainWindow", u"XLB", None))
        self.graph_combo_box.setItemText(16, QCoreApplication.translate("MainWindow", u"XLRE", None))
        self.graph_combo_box.setItemText(17, QCoreApplication.translate("MainWindow", u"VNQ", None))
        self.graph_combo_box.setItemText(18, QCoreApplication.translate("MainWindow", u"-------", None))
        self.graph_combo_box.setItemText(19, QCoreApplication.translate("MainWindow", u"VXUS", None))
        self.graph_combo_box.setItemText(20, QCoreApplication.translate("MainWindow", u"IXUS", None))
        self.graph_combo_box.setItemText(21, QCoreApplication.translate("MainWindow", u"VEU", None))
        self.graph_combo_box.setItemText(22, QCoreApplication.translate("MainWindow", u"-------", None))
        self.graph_combo_box.setItemText(23, QCoreApplication.translate("MainWindow", u"VIXY", None))
        self.graph_combo_box.setItemText(24, QCoreApplication.translate("MainWindow", u"SH", None))
        self.graph_combo_box.setItemText(25, QCoreApplication.translate("MainWindow", u"SQQQ", None))
        self.graph_combo_box.setItemText(26, QCoreApplication.translate("MainWindow", u"-------", None))
        self.graph_combo_box.setItemText(27, QCoreApplication.translate("MainWindow", u"BND", None))
        self.graph_combo_box.setItemText(28, QCoreApplication.translate("MainWindow", u"AGG", None))
        self.graph_combo_box.setItemText(29, QCoreApplication.translate("MainWindow", u"-------", None))
        self.graph_combo_box.setItemText(30, QCoreApplication.translate("MainWindow", u"ARKK", None))
        self.graph_combo_box.setItemText(31, QCoreApplication.translate("MainWindow", u"SOXX", None))

        self.g_1d.setText(QCoreApplication.translate("MainWindow", u"1D", None))
        self.g_5d.setText(QCoreApplication.translate("MainWindow", u"5D", None))
        self.g_1mo.setText(QCoreApplication.translate("MainWindow", u"1M", None))
        self.g_6mo.setText(QCoreApplication.translate("MainWindow", u"6M", None))
        self.g_ytd.setText(QCoreApplication.translate("MainWindow", u"YTD", None))
        self.g_1y.setText(QCoreApplication.translate("MainWindow", u"1Y", None))
        self.g_5y.setText(QCoreApplication.translate("MainWindow", u"5Y", None))
        self.g_max.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.g_name_label.setText(QCoreApplication.translate("MainWindow", u"E-Mini S&P 500 Sep 25 (ES=F)", None))
        self.g_price_label.setText(QCoreApplication.translate("MainWindow", u"6,417.00", None))
        self.g_change_label.setText(QCoreApplication.translate("MainWindow", u"+46.00 (+0.72%)", None))
        self.low_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stckSplits_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.open_label_2.setText(QCoreApplication.translate("MainWindow", u"Open:\n"
"50", None))
        self.date_label_2.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.high_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.volume_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.div_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.close_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.all_holdings_label_2.setText(QCoreApplication.translate("MainWindow", u"All available tickers/funds", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Best US:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"        VTI - Vanguard Total Stock Market ETF\n"
"        SPY - SPDR S&P 500 ETF Trust\n"
"        VOO - Vanguard S&P 500 ETF\n"
"        SCHB - Schwab U.S. Broad Market ETF\n"
"        DIA - SPDR Dow Jones Industrial Average ETF Trust\n"
"        QQQ - Invesco QQQ Trust (Nasdaq-100)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"International:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"        VXUS - Vanguard Total International Stock ETF\n"
"        IXUS - iShares Core MSCI Total International Stock ETF\n"
"        VEU - Vanguard FTSE All-World ex-US ETF", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Volatility inverse:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"        VIXY - ProShares VIX Short-Term Futures ETF\n"
"        SH - ProShares Short S&P500\n"
"        SQQQ - ProShares UltraPro Short QQQ", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Sectors:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"        XLK - Technology Select Sector SPDR Fund\n"
"        XLF - Financial Select Sector SPDR Fund\n"
"        XLE - Energy Select Sector SPDR Fund\n"
"        XLY - Consumer Discretionary Select Sector SPDR Fund\n"
"        XLI - Industrial Select Sector SPDR Fund\n"
"        XLV - Health Care Select Sector SPDR Fund\n"
"        XLC - Communication Services Select Sector SPDR Fund\n"
"        XLU - Utilities Select Sector SPDR Fund\n"
"        XLB - Materials Select Sector SPDR Fund\n"
"        XLRE - Real Estate Select Sector SPDR Fund\n"
"        VNQ - Vanguard Real Estate ETF", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Bonds:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"        BND - Vanguard Total Bond Market ETF\n"
"        AGG - iShares Core U.S. Aggregate Bond ETF", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Thematic:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"        ARKK - ARK Innovation ETF\n"
"        SOXX - iShares Semiconductor ETF\n"
"", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Draghi Andreas", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

