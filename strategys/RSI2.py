import backtrader as bt

class RSI2_STRATEGY(bt.Strategy):
    def __init__(self):
        self.rsi2 = bt.ind.RelativeStrengthIndex(self.data, period=2, upperband=90, lowerband=10)
        self.sma8 = bt.ind.SimpleMovingAverage(self.data, period=8)
        self.sma20 = bt.ind.MovingAverageSimple(self.data, period=20)
        self.sma200 = bt.ind.SimpleMovingAverage(self.data, period=200)

    def next(self):
        if not self.position:
            if self.rsi2 <= 10 and self.data.close > self.sma200:
                self.buy()
        else:
            if self.rsi2 >= 90:
                self.sell()