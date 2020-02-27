
import backtrader.feeds as btfeed

class PandasData(btfeed.feed.DataBase):
    params = (
        ('datetime', -1),
        ('open', -1),
        ('high', -1),
        ('low', -1),
        ('close', -1),
        ('volume', -1),
        ('openinterest', -1),
    )