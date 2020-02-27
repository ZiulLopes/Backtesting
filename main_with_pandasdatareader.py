import pandas as pd
import pandas_datareader as pdr
import backtrader as bt
from classes.PandasData import *
from strategys.SMACROSS import *

df = pdr.DataReader("ITUB4.SA", start='2015-1-1', end='2020-2-27', data_source='yahoo')

data = bt.feeds.PandasData(dataname=df)

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000.0)
cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
cerebro.addstrategy(SmaCross, pfast=8, pslow=20)
cerebro.adddata(data)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot(style='candlestick', barup='green', bardown='red')