import backtrader as bt

class RSI_STRATEGY(bt.Strategy):

    def __init__(self):
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=14)
        self.sma = bt.ind.SimpleMovingAverage(self.data, period=20)
        self.sma2 = bt.ind.SimpleMovingAverage(self.data, period=200)

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy()
        else:
            if self.data.close[-1] > self.sma and self.data.close < self.sma:
                self.sell()