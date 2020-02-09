import backtrader as bt
import backtrader.feeds as btfeeds
import datetime

datapath = 'IBOV.csv'

data = btfeeds.YahooFinanceCSVData(
    dataname=datapath,
    reversed=True,
    fromdate=datetime.datetime(2015, 1, 1),
    todate=datetime.datetime(2020, 1, 31),
    timeframe=bt.TimeFrame.Weeks
    )


class CrossSMA(bt.Strategy):

    params = dict(
        pfast=8, 
        pslow=20 
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)
        sma2 = bt.ind.SMA(period=self.p.pslow)
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()

        elif self.crossover < 0:
            self.close()


startcash = 150000

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.broker.setcash(startcash)
cerebro.addstrategy(CrossSMA)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot(style='candlestick')