import backtrader as bt

class BUY123_STRETEGY(bt.Strategy):
    """A simple strategy,
    at bottom in dayly chart"
    """
    def __init__(self):
        self.sma9 = bt.ind.SimpleMovingAverage(self.data, period=9)
        self.rsi2 = bt.ind.RelativeStrengthIndex(self.data, period=2)

    def next(self):
        if not self.position:
            low1 = min(self.data.low.get(ago=-1))
            low2 = min(self.data.low.get(ago=-2))
            if self.data.close > self.sma9 and (low1 < low2 and self.data.low > low1):
                self.buy()
        else:
            if self.data.close[-1] < self.sma9 and self.data.close < self.data.close[-1]:
                self.sell()