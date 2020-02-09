import backtrader as bt
import backtrader.feeds as btfeeds
import datetime
import pandas
from strategys.BUY123 import *
from strategys.RSI2 import *


#datapath = 'datasets/WEGE3.SA.csv'
datapath = 'datasets/MGLU3.M15.csv'

# data = btfeeds.YahooFinanceCSVData(
#     dataname=datapath,
#     reversed=True,
#     fromdate=datetime.datetime(2015, 1, 1),
#     todate=datetime.datetime.now(),
#     timeframe=bt.TimeFrame.Days
#     )

data = btfeeds.GenericCSVData(
    dataname='datasets/MGLU3.M15.csv',
    reversed=False,
    fromdate=datetime.datetime(2020, 2, 1),
    todate=datetime.datetime(2020, 2, 8),

    nullvalue=0.0,

    dtformat=('%Y-%m-%d %H:%M:%S'),

    datetime=0,
    open=1,
    high=2,
    low=3,
    close=4,
    volume=5,
    openinterest=None
)


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.adddata(data)
    cerebro.broker.setcash(100000.0)
    cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
    cerebro.addstrategy(BUY123_STRETEGY)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot(style='candlestick')