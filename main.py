from lumibot.brokers import Alpaca
from lumibot.backtesting import yahoo_backtesting, YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "248f1c65-a5d9-47eb-9e9b-f2967acddd37"
API_SECRET = "cdvylbieub"
BASE_URL = "https://account.upstox.com/developer/apps"

ALPACA_CREDS = {
    "API_KEY":API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def initi(self, symbol:str="SPY"):
        self.symbol = symbol
        self.symbol = "24H"
        self.last_trade = None

    def on_trading_iteration(self):
        if self.last_trade == None:
            order = self.create_order(
                self.symbol,
                10,
                "buy",
                type="market"
            )
            self.submit_order(order)
            self.last_trade= "buy"

start_date = datetime(2024,1,15)
end_date = datetime(2024,1,28)
broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker, parameters={"symbol": "SPY"})

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"symbol": "SPY"}


)