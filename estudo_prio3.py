import backtrader as bt
import backtrader.feeds as btfeeds
import datetime

datapath = 'PRIO3.SA.csv'

data = btfeeds.YahooFinanceCSVData(
    dataname=datapath,
    reversed=True,
    fromdate=datetime.datetime(2019, 1, 1),
    todate=datetime.datetime(2019, 12, 31),
    timeframe=bt.TimeFrame.Weeks
    )


class CloseSMA(bt.Strategy):

    def __init__(self):
        self.sma = bt.ind.SimpleMovingAverage(self.data, period=20)

    def next(self):
        if not self.position:
            if self.data.close > self.sma:
                self.buy()

        elif self.data.close < self.sma:
            self.sell()


startcash = 150000

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.broker.setcash(startcash)
cerebro.addstrategy(CloseSMA)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot(style='candlestick')