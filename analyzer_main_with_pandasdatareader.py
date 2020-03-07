import pandas as pd
import pandas_datareader as pdr
import backtrader as bt
import backtrader.analyzers as btanalyzers
from classes.PandasData import *
from classes.Analyzer import *
from strategys.RSI2 import *


df = pdr.DataReader("ITUB4.SA", start='2018-1-1', end='2020-3-7', data_source='yahoo')
data = bt.feeds.PandasData(dataname=df)

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000.0)
cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
cerebro.adddata(data)

# Strategy
cerebro.addstrategy(RSI2_STRATEGY)


# Add the analyzers we are interested in
cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")


print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run over everything
strategies = cerebro.run()
firstStrat = strategies[0]

#Get final portfolio Value
portvalue = cerebro.broker.getvalue()

print('Final Portfolio Value: ${}'.format(portvalue))

# print the analyzers
Analyzer.printTradeAnalysis(firstStrat.analyzers.ta.get_analysis())
Analyzer.printSQN(firstStrat.analyzers.sqn.get_analysis())

#Finally plot the end results
#cerebro.plot(style='candlestick')