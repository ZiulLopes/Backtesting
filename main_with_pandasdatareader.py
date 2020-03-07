import pandas as pd
import pandas_datareader as pdr
import backtrader as bt
from classes.PandasData import *
from strategys.SMACROSS import *
from strategys.RSI2 import *

df = pdr.DataReader("ITUB4.SA", start='2010-1-1', end='2020-3-7', data_source='yahoo')

data = bt.feeds.PandasData(dataname=df)

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000.0)
cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
cerebro.addstrategy(RSI2_STRATEGY)
cerebro.adddata(data)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot(style='candlestick', barup='green', bardown='red')