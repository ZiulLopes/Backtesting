import backtrader as bt
import backtrader.feeds as btfeeds
import datetime
from strategys.BUY123 import *

datapath = 'datasets/QUAL3.SA.csv'

data = btfeeds.YahooFinanceCSVData(
    dataname=datapath,
    reversed=True,
    fromdate=datetime.datetime(2015, 1, 1),
    todate=datetime.datetime(2020, 2, 3),
    timeframe=bt.TimeFrame.Days
    )


startcash = 100000

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.broker.setcash(startcash)
cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
cerebro.addstrategy(BUY123_STRETEGY)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot(style='candlestick')