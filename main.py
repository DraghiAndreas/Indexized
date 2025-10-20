import sys
import os
import platform

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHeaderView
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from functionality.project import hist
from functionality.basic import *
from functionality.portfolio import *
from functionality.cache_test import *

from modules import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


widgets = None

class MplCanvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 4, dpi = 100):
        self.fig = Figure(figsize=(width,height),dpi=dpi)
        self.ax = self.fig.add_subplot()
        super().__init__(self.fig)
        self.setParent(parent)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui


        self.canvas = MplCanvas(widgets.graph_frame, 5,4,100)
        layout = QVBoxLayout(widgets.graph_frame)
        layout.addWidget(self.canvas)
        widgets.graph_frame.setLayout(layout)

        self.graph_period = '1mo'
        self.graph_tick = 'VTI'

        self.graph_data_update()
        
        n = get_username()
        if n:
            self.username = n
        else:
            self.username = "User"
        self.updateUsername()

        Settings.ENABLE_CUSTOM_TITLE_BAR = True


        title = "Indexized"
        description = "Indexized - Index funds made just a little bit easier"
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)


        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        UIFunctions.uiDefinitions(self)

        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        widgets.quote_label.setText(random_quote()) #Random Quoate
        self.updateTop5()

        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.comboBox.currentIndexChanged.connect(lambda data: print(data))

        widgets.g_1d.clicked.connect(self.buttonGraph)
        widgets.g_1mo.clicked.connect(self.buttonGraph)
        widgets.g_1y.clicked.connect(self.buttonGraph)
        widgets.g_5d.clicked.connect(self.buttonGraph)
        widgets.g_5y.clicked.connect(self.buttonGraph)
        widgets.g_6mo.clicked.connect(self.buttonGraph)
        widgets.g_max.clicked.connect(self.buttonGraph)
        widgets.g_ytd.clicked.connect(self.buttonGraph)
        widgets.graph_combo_box.currentIndexChanged.connect(self.combo_changed)

        widgets.hg_1d.clicked.connect(self.buttonGraph)
        widgets.hg_1mo.clicked.connect(self.buttonGraph)
        widgets.hg_1y.clicked.connect(self.buttonGraph)
        widgets.hg_5d.clicked.connect(self.buttonGraph)
        widgets.hg_6mo.clicked.connect(self.buttonGraph)
        widgets.hg_ytd.clicked.connect(self.buttonGraph)

        widgets.save_username_btn.clicked.connect(self.saveUsername)




        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.show()

        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def saveUsername(self):
        user = widgets.username_input.toPlainText()
        if not user:
            print('Username cannot be empty')
        elif len(user)>30:
            print('Username cannot have over 30 characters')
        else:
            self.username = user
            self.updateUsername()
            save_user(user)
        
    
    def updateUsername(self):
        text = 'Welcome, '+ self.username +'!' 
        widgets.welcome_label.setText(text)


    def buttonGraph(self):
        text = self.sender().objectName()[2:] #GRABBING JUST THE PERIOD FROM THE NAME
        self.graph_period = text
        self.graph_data_update()

    def updateTop5(self):
        l_asc = get_top_5(1)
        l_desc = get_top_5(0)
        curr = get_currencies()

        widgets.date_label.setText(f'All data is updated as of : {get_last_update()} (YYYY-DD-MM)')

        l_tick_labels = [widgets.l1_tick_label,widgets.l2_tick_label,widgets.l3_tick_label,widgets.l4_tick_label,widgets.l5_tick_label]
        l_change_labels = [widgets.l1_change_label,widgets.l2_change_label,widgets.l3_change_label,widgets.l4_change_label,widgets.l5_change_label]
        loser_frames = [widgets.loser1,widgets.loser2,widgets.loser3, widgets.loser4, widgets.loser5]

        g_tick_labels = [widgets.g1_tick_label,widgets.g2_tick_label,widgets.g3_tick_label,widgets.g4_tick_label,widgets.g5_tick_label]
        g_change_labels = [widgets.g1_change_label,widgets.g2_change_label,widgets.g3_change_label,widgets.g4_change_label,widgets.g5_change_label]
        gainer_frames = [widgets.gainer1, widgets.gainer2, widgets.gainer3, widgets.gainer4, widgets.gainer5]

        c_tick_labels = [widgets.c1_tick_label,widgets.c2_tick_label,widgets.c3_tick_label,widgets.c4_tick_label,widgets.c5_tick_label]
        c_change_labels = [widgets.c1_change_label,widgets.c2_change_label,widgets.c3_change_label,widgets.c4_change_label,widgets.c5_change_label]
        currency_frames = [widgets.currency1, widgets.currency2, widgets.currency3, widgets.currency4, widgets.currency5]

        for i in range(len(l_tick_labels)):
            l_tick_labels[i].setText(f'{l_asc[i][0]}: {l_asc[i][2]}$')
            l_change_labels[i].setText(f'{l_asc[i][4]}$({l_asc[i][3]}%)')
            self.set_stylesheet(loser_frames[i],l_change_labels[i],l_tick_labels[i],l_asc[i][4])

            g_tick_labels[i].setText(f'{l_desc[i][0]}: {l_desc[i][2]}$')
            g_change_labels[i].setText(f'{l_desc[i][4]}$({l_desc[i][3]}%)')
            self.set_stylesheet(gainer_frames[i],g_change_labels[i],g_tick_labels[i],l_desc[i][4])

            #EURUSD=X JPYUSD=X GBPUSD=X CNYUSD=X CHFUSD=X"
            match curr[i][0]:
                case 'EURUSD=X':
                    tn = 'EUR'
                case 'JPYUSD=X':
                    tn = 'JPY'
                case 'GBPUSD=X':
                    tn = 'GBP'
                case 'CNYUSD=X':
                    tn = 'CNY'
                case 'CHFUSD=X':
                    tn = 'CHF'

            c_tick_labels[i].setText(f'{tn}: {curr[i][2]}$')
            c_change_labels[i].setText(f'{curr[i][4]}$({curr[i][3]}%)')
            self.set_stylesheet(currency_frames[i],c_change_labels[i],c_tick_labels[i],curr[i][4])

    def set_stylesheet(self,sheet,text_change,text_tick,val):
        if val > 0:
            sheet.setStyleSheet('border: 1px solid #2ecc71')
            text_change.setStyleSheet('font: bold "Segoe UI"; font-size: 19px;color:#2ecc71; border: none;')
        else:
            sheet.setStyleSheet('border: 1px solid #ff4143;')
            text_change.setStyleSheet('font: bold "Segoe UI"; font-size: 19px;color:#ff4143;border: none;')
        text_tick.setStyleSheet('font: bold "Segoe UI"; font-size: 19px;border:none;')

    def combo_changed(self, index):
        text = widgets.graph_combo_box.itemText(index)
        if text != '-------':
            print(f'Option changed: {text}')
            self.graph_tick = text
            self.graph_data_update()
        else:
            print('Separator')

    def graph_data_update(self):
        print(self.graph_period)


        ticker = yf.Ticker(self.graph_tick)
        pand = ticker.history(period=self.graph_period,interval = period_to_interval(self.graph_period))
        prices = pand['Close'].round(2).tolist()

        open_price = pand['Open'].iloc[-1].round(2)
        high_price = pand['High'].iloc[-1].round(2)
        low_price = pand['Low'].iloc[-1].round(2)
        close_price = pand['Close'].iloc[-1].round(2)
        volume = int(pand['Volume'].iloc[-1])
        dividends = pand['Dividends'].iloc[-1].round(2)
        stockSplits = pand['Stock Splits'].iloc[-1].round(2)
        latest_date = pand.index[-1].strftime('%Y-%m-%d')

        widgets.open_label_2.setText(f'Open:\n{open_price}$')
        widgets.close_label.setText(f'Close:\n{close_price}$')
        widgets.high_label.setText(f'High:\n{high_price}$')
        widgets.low_label.setText(f'Low:\n{low_price}$')
        widgets.volume_label.setText(f'Volume:\n{volume}')
        widgets.div_label.setText(f'Dividends:\n{dividends}')
        widgets.stckSplits_label.setText(f'Stock Splits:\n{stockSplits}')
        widgets.date_label_2.setText(f'Date:\n{latest_date}')

        dates = date_selector(pand,self.graph_period)
        start = prices[0]
        end = prices[-1]
        change = round(end - start, 2)
        percent = round((change / start) * 100, 2)

        self.graph_creatoraa(prices,change,dates)
        if change > 0:
            widgets.g_change_label.setStyleSheet('color: #2ecc71;font-size: 18px;font: bold "Segoe UI";')
            change = '+'+str(change)
            percent = '+'+str(percent)
        else:
            widgets.g_change_label.setStyleSheet('color: #ff4143;font-size: 18px;font: bold "Segoe UI";')
        widgets.g_price_label.setText('$'+str(end))
        widgets.g_change_label.setText(f'{change}$ ({percent}%)')
        widgets.g_name_label.setText(tick_full(self.graph_tick))

    def graph_creatoraa(self, prices, change, dates):
        ax = self.canvas.ax
        fig = self.canvas.fig

        ax.clear()

        x_axis = range(len(prices))
        fig.patch.set_facecolor('#14181c')
        ax.set_facecolor('#14181c')

        for spine in ax.spines.values():
            spine.set_edgecolor('#14181c')

        ax.grid(axis='y', color='#252b30')
        ax.plot(prices, color=graph_color(change))
        ax.fill_between(x_axis, prices, min(prices), color=graph_color(change), alpha=0.3)

        ax.tick_params(axis='both',color = '#14181c')
        ax.set_ylabel('USD$', color="#FFFFFF")
        ax.set_xticks(x_axis)
        ax.set_xticklabels(dates, color="#FFFFFF")
        ax.set_yticklabels(ax.get_yticks(), color="#FFFFFF")  # fixed typo

        self.canvas.draw()  # update the canvas

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            if widgets.stackedWidget.currentWidget() != widgets.home:
                widgets.quote_label.setText(random_quote())
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.graph)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.portfolio) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            widgets.stackedWidget.setCurrentWidget(widgets.funds)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        print(f'Button "{btnName}" pressed!')


    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
