import sys
import os
import platform
import pandas as pd
import numpy as np
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHeaderView, QAbstractItemView, QTableWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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

        cache()
        self.graph_period = '1mo'
        self.graph_period_port = '1mo'
        self.graph_tick = 'VTI'

        self.canvas = MplCanvas(widgets.graph_frame, 5,4,100)
        layout = QVBoxLayout(widgets.graph_frame)
        layout.addWidget(self.canvas)
        widgets.graph_frame.setLayout(layout)

        check()
        self.pieChart = MplCanvas(widgets.holdings_pie_chart,5,4,100)
        layout2 = QVBoxLayout(widgets.holdings_pie_chart)
        layout2.addWidget(self.pieChart)
        widgets.holdings_pie_chart.setLayout(layout2)

        self.portGraph=MplCanvas(widgets.frame_15,5,4,100)
        layout3 = QVBoxLayout(widgets.frame_15)
        layout3.addWidget(self.portGraph)
        widgets.frame_15.setLayout(layout3)

        widgets.portfolio_table.setColumnCount(3)
        widgets.portfolio_table.setHorizontalHeaderLabels(['Ticker','Amount','Price'])
        widgets.portfolio_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.portfolio_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        widgets.portfolio_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        row = widgets.portfolio_table.rowCount()
        widgets.portfolio_table.insertRow(row)

        widgets.portfolio_table.setItem(row,0,QTableWidgetItem('VTI'))
        widgets.portfolio_table.setItem(row,1,QTableWidgetItem('1.32'))
        widgets.portfolio_table.setItem(row,2,QTableWidgetItem('$241'))

        self.portfolio_graph_update()
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

        widgets.hg_1d.clicked.connect(self.button_graph_port)
        widgets.hg_1mo.clicked.connect(self.button_graph_port)
        widgets.hg_1y.clicked.connect(self.button_graph_port)
        widgets.hg_5d.clicked.connect(self.button_graph_port)
        widgets.hg_6mo.clicked.connect(self.button_graph_port)
        widgets.hg_ytd.clicked.connect(self.button_graph_port)

        widgets.save_username_btn.clicked.connect(self.saveUsername)

        widgets.add_btn.clicked.connect(self.add_stock)
        widgets.subtract_btn.clicked.connect(self.subtract_stock)
        widgets.delete_btn.clicked.connect(self.delete_stock)
        widgets.reset_btn.clicked.connect(self.reset_port)


        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseLeftBox)

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

    def button_graph_port(self):
        text = self.sender().objectName()[3:]
        self.graph_period_port = text
        self.portfolio_graph_update()

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


    
    def set_stylesheet2(self,text,val):
        if val > 0:
            text.setStyleSheet('font: bold "Segoe UI"; font-size: 23px;border:none; color: #2ecc71;')
        else:
            text.setStyleSheet('font: bold "Segoe UI"; font-size: 23px;border:none; color: #ff4143;')



    def subtract_stock(self):
        amount = widgets.portfolio_amount.toPlainText()
        index = widgets.portfolio_combobox.currentIndex()
        tick = widgets.portfolio_combobox.itemText(index)
        try:
            amount = float(amount)
            if amount < 0:
                print(f'{amount} is a NEGATIVE number, it will be interpreted as {abs(amount)}')
                amount = abs(amount)
        except ValueError:
            print('Amount is not valid!')
            return
        if tick == '-------':
            print('Select one of the valid TICKERS!')
            return        
        subtract(tick,amount)
        self.portfolio_graph_update()

    def add_stock(self):
        amount = widgets.portfolio_amount.toPlainText()
        index = widgets.portfolio_combobox.currentIndex()
        tick = widgets.portfolio_combobox.itemText(index)
        try:
            amount = float(amount)
            if amount < 0:
                print(f'{amount} is a NEGATIVE number, it will be interpreted as {abs(amount)}')
                amount = abs(amount)
        except ValueError:
            print('Amount is not valid!')
            return
        if tick == '-------':
            print('Select one of the valid TICKERS!')
            return
        add_one(tick, amount)
        self.portfolio_graph_update()

    def delete_stock(self):
        index = widgets.portfolio_combobox.currentIndex()
        tick = widgets.portfolio_combobox.itemText(index)
        if tick == '-------':
            print('Select one of the valid TICKERS!')
            return        
        delete_one(tick)
        self.portfolio_graph_update()
    
    def reset_port(self):
        reset()
        check()
        self.portfolio_graph_update()

    def portfolio_graph_update(self):
        all = np.array(get_all())
        if all.size:
            tick = all[:,0]
            val = all[:,1].astype(float)
        else:
            tick = np.array([])
            val = np.array([])
        self.update_pie_chart(tick,val)
        self.update_total(tick,val)
        self.update_portfolio_graph(tick,val)
        self.update_port_table(tick, val)
    
    def update_total(self,tick, am):
        total = np.array([price_return(t)*am[i] for i,t in enumerate(tick,0)])
        widgets.all_holdings_label.setText(f'US${round(np.sum(total),2)}')    
    
    def update_port_table(self,tick, val):
        widgets.portfolio_table.setRowCount(0)
        print(tick)
        for i,t in enumerate(tick,0):
            price = price_return(t)*val[i]
            print(val[i])
            self.add_row(t,val[i],price)
    
    def add_row(self,tick,amount,price):
        tab = widgets.portfolio_table
        row = tab.rowCount()
        tab.insertRow(row)
        tab.setItem(row,0,QTableWidgetItem(tick))
        tab.setItem(row,1,QTableWidgetItem(str(round(amount,2))))
        tab.setItem(row,2,QTableWidgetItem(f'${price}'))

    def update_pie_chart(self,tick,vals):
        ax = self.pieChart.ax
        fig = self.pieChart.fig
        ax.clear()
        fig.patch.set_facecolor('#14181c')
        ax.set_facecolor('#14181c')

        wedges, texts, autotexts = ax.pie(
            vals,
            labels=tick,
            colors = [map_change(get_change(t)) for t in tick],
            explode = [0.1 if val == max(vals) else 0 for val in vals],
            autopct='%1.1f%%',          
            startangle=90,             
            textprops={'color': 'white', 'fontsize': 10},  
            wedgeprops={'edgecolor': '#14181c', 'linewidth': 1},
            radius=2
        )

        ax.set_title("Portfolio Holdings", color='white', fontsize=13, pad=20, weight='bold')

        ax.axis('equal')

        self.pieChart.draw()

    def update_portfolio_graph(self,tickers,amounts):
        total_values = None
        first = True
        interval = period_to_interval(self.graph_period_port)
        for ticker_name, amount in zip(tickers, amounts):
            ticker = yf.Ticker(ticker_name)
            hist = ticker.history(period=self.graph_period_port, interval=interval)
            if first:
                print('Entered LOOP')
                dates = date_selector(hist,self.graph_period_port)
                first = False

            closes = hist['Close'].round(2)

            values = closes * amount

            if total_values is None:
                total_values = values
            else:
                total_values = total_values.add(values, fill_value=0)
        print('Exit loop')
        if total_values is not None and not total_values.empty:
            total_values = total_values.to_numpy()
            start = round(total_values[0],2)
            end = total_values[-1]
            change = round(end - start, 2)
            percent = round((change / start) * 100, 2)

            widgets.price_ago_text.setText(f'Price {self.graph_period_port} ago:')
            widgets.price_ago_label.setText(f'${start}')
            
            if change > 0:
                widgets.period_change.setText(f'+${change}({percent}%)')
            else:
                widgets.period_change.setText(f'-${abs(change)}({percent}%)')
            self.set_stylesheet2(widgets.period_change,change)

            self.graph_creatoraa(self.portGraph,total_values,change,dates)
        else:
            ax = self.portGraph.ax
            fig = self.portGraph.fig

            ax.clear()
            fig.patch.set_facecolor('#14181c')
            ax.set_facecolor('#14181c')

            for spine in ax.spines.values():
                spine.set_edgecolor('#14181c')

            ax.grid(axis='y', color='#252b30')

            ax.tick_params(axis='both',color = '#14181c')
            ax.set_ylabel('USD$', color="#FFFFFF")
            ax.set_xticklabels([])
            ax.set_yticklabels([])

            self.portGraph.draw()

            widgets.price_ago_text.setText(f'Price {self.graph_period_port} ago:')
            widgets.price_ago_label.setText(f'$0')
            widgets.period_change.setText(f'+$0(0%)')
    
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

        print(f'{self.graph_tick} : start : {start} | end : {end} | change : {change} | percent : {percent}')

        self.graph_creatoraa(self.canvas,prices,change,dates)
        if change > 0:
            widgets.g_change_label.setStyleSheet('color: #2ecc71;font-size: 18px;font: bold "Segoe UI";')
            change = '+'+str(change)
            percent = '+'+str(percent)
        else:
            widgets.g_change_label.setStyleSheet('color: #ff4143;font-size: 18px;font: bold "Segoe UI";')
        widgets.g_price_label.setText('$'+str(end))
        widgets.g_change_label.setText(f'{change}$ ({percent}%)')
        widgets.g_name_label.setText(tick_full(self.graph_tick))

    def graph_creatoraa(self,canvas, prices, change, dates):
        ax = canvas.ax
        fig = canvas.fig

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

        canvas.draw()  # update the canvas

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
