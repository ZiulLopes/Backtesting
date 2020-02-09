import backtrader as bt

class SMA9_STRETEGY(bt.Strategy):

    def __init__(self):
        self.sma9 = bt.ind.SimpleMovingAverage(self.data, period=9)

    def next(self):
        if not self.position:
            if self.data.close[-1] < self.sma9 and self.data.close > self.data.close[-1] and self.data.close > self.sma9:
                self.buy()
        else:
            if self.data.close[-1] > self.sma9 and self.data.close < self.sma9:
                self.sell()