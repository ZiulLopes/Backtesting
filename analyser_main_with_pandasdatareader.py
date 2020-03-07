import pandas as pd
import pandas_datareader as pdr
import backtrader as bt
import backtrader.analyzers as btanalyzers
from classes.PandasData import *
from strategys.SMACROSS import *
from strategys.RSI2 import *


def printTradeAnalysis(analyzer):
    '''
    Function to print the Technical Analysis results in a nice format.
    '''
    #Get the results we are interested in
    total_open = analyzer.total.open
    total_closed = analyzer.total.closed
    total_won = analyzer.won.total
    total_lost = analyzer.lost.total
    win_streak = analyzer.streak.won.longest
    lose_streak = analyzer.streak.lost.longest
    pnl_net = round(analyzer.pnl.net.total,2)
    strike_rate = (total_won / total_closed) * 100
    #Designate the rows
    h1 = ['Total Open', 'Total Closed', 'Total Won', 'Total Lost']
    h2 = ['Strike Rate','Win Streak', 'Losing Streak', 'PnL Net']
    r1 = [total_open, total_closed,total_won,total_lost]
    r2 = [strike_rate, win_streak, lose_streak, pnl_net]
    #Check which set of headers is the longest.
    if len(h1) > len(h2):
        header_length = len(h1)
    else:
        header_length = len(h2)
    #Print the rows
    print_list = [h1,r1,h2,r2]
    row_format ="{:<15}" * (header_length + 1)
    print("Trade Analysis Results:")
    for row in print_list:
        print(row_format.format('',*row))

def printSQN(analyzer):
    sqn = round(analyzer.sqn,2)
    print('SQN: {}'.format(sqn))

df = pdr.DataReader("ITUB4.SA", start='2010-1-1', end='2020-3-7', data_source='yahoo')

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
printTradeAnalysis(firstStrat.analyzers.ta.get_analysis())
printSQN(firstStrat.analyzers.sqn.get_analysis())

#Finally plot the end results
#cerebro.plot(style='candlestick')