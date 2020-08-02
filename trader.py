import backtrader as bt
import datetime
from strategies import TestStrategy

cerebro = bt.Cerebro()

cerebro.broker.set_cash(100000)

data = bt.feeds.YahooFinanceCSVData(
    dataname='oracle.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2000, 1, 3),
    # Do not pass values after this date
    todate=datetime.datetime(2014, 12, 31),
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(bt.sizers.FixedSize, stake=100)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()