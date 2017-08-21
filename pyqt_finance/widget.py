from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from yahoo_historical import Fetcher
import datetime as dt

class QStockWidget(QWidget):
    def __init__(self, *args):
        super(QWidget, self).__init__()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.form = QFormLayout()
        self.form.addWidget(self.canvas)
        self.setLayout(self.form)
        self.ticker = None
        if args:
            self.ticker = args[0]

    def plot(self, *args):
        if args:
            ticker = args[0]
        else:
            ticker = self.ticker
            if ticker == None:
                raise InvalidTickerException(str(ticker))
        try:
            data = Fetcher(ticker, [2007,1,1]).getDatePrice()
        except KeyError:
            raise InvalidTickerException(str(ticker))
        except IndexError:
            raise InvalidTickerException(str(ticker))
        except UnboundLocalError:
            raise InvalidTickerException(str(ticker))
        dates = []
        for date in data["Date"]:
            date = date.split("-")
            date[0], date[1] = date[1], date[0]
            date[1], date[2] = date[2], date[1]
            dates.append("/".join(date))

        dates = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

        self.figure.clear()  # reset the figure
        self.figure.suptitle(ticker)
        ax = self.figure.add_subplot(111)
        ax.plot(dates, data["Adj Close"])
        self.canvas.draw()

    def clear(self):
        """Clears the current graph"""
        self.figure.clear()

class InvalidTickerException(Exception):
    def __init__(self, ticker):
        self.msg = "Invalid ticker: " + ticker
