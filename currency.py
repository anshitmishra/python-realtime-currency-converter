from locale import currency
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QLineEdit,QComboBox,QPushButton
from PyQt5 import uic
from PyQt5 import QtGui
import requests
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("currency.ui",self)

        self.setWindowTitle("Currency Converter")
        self.setWindowIcon(QtGui.QIcon('image/logo.ico'))
        # tagging items
        self.MainDisplay = self.findChild(QLabel,"label")
        self.Amount = self.findChild(QLineEdit,"lineEdit")
        self.fromCurrency = self.findChild(QComboBox,"comboBox")
        self.toCurrency = self.findChild(QComboBox,"comboBox_2")
        self.Exchange = self.findChild(QPushButton,"pushButton_2")
        self.Convert = self.findChild(QPushButton,"pushButton")


        # adding list to combobox
        currencyList = ("AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY","COP","CRC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLE","SLL","SOS","SRD","SSP","STN","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VES","VND","VUV","WST","XAF","XCD","XDR","XOF","XPF","YER","ZAR","ZMW","ZWL")
        self.fromCurrency.addItems(currencyList)
        self.toCurrency.addItems(currencyList)
        self.fromCurrency.setCurrentText("USD")
        self.toCurrency.setCurrentText("INR")
        

        # exchange event listner
        self.Exchange.clicked.connect(lambda:self.ExchangeCurr())
        self.Convert.clicked.connect(lambda:self.ConvertCurr())





        self.show()

    def ConvertCurr(self):
        self.Convert.setText("Converting...")
        url = "https://api.exchangerate-api.com/v4/latest/"+self.fromCurrency.currentText()
        data = requests.get(url).json()
        Amount = self.Amount.text()
        if Amount == "":
            self.Convert.setText("Convert")
            self.MainDisplay.setText("enter value")
            return
        rates = data['rates']
        AfterCOnvert = round(float(Amount) * float(rates[self.toCurrency.currentText()]),2)
        self.MainDisplay.setText(str(AfterCOnvert))
        self.Convert.setText("Convert")
        


    def ExchangeCurr(self):
        fromCurr = self.fromCurrency.currentText()
        toCurr = self.toCurrency.currentText()
        self.fromCurrency.setCurrentText(toCurr)
        self.toCurrency.setCurrentText(fromCurr)



app = QApplication(sys.argv)
UIWindow= UI()
app.exec_()

