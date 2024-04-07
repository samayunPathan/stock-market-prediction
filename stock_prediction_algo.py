import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class AlgorithmicTrader:
    def __init__(self, symbol, from_date, to_date, initial_budget=5000):
        self.symbol = symbol
        self.from_date = from_date
        self.to_date = to_date
        self.initial_budget = initial_budget
        self.current_budget = initial_budget
        self.shares_owned = 0
        self.df = None
        self.ml_model = RandomForestClassifier()

    def initialize_data(self):
        self.df = yf.download(self.symbol, start=self.from_date, end=self.to_date)
        self.df = self.df.ffill().dropna()

    def calculate_moving_averages(self):
        self.df['MA50'] = self.df['Close'].rolling(window=50).mean()
        self.df['MA200'] = self.df['Close'].rolling(window=200).mean()

    def identify_golden_cross(self):
        self.df['Signal'] = 0
        self.df.loc[self.df['MA50'] > self.df['MA200'], 'Signal'] = 1

    def determine_max_shares(self):
        last_close = self.df['Close'].iloc[-1]
        self.max_shares = int(self.current_budget / last_close)

    def execute_trades(self):
        self.df['Position'] = self.df['Signal'].diff()
        for i in range(len(self.df)):
            if self.df['Position'].iloc[i] == 1:
                if self.current_budget >= 0:
                    self.shares_owned = self.max_shares
                    self.current_budget -= (self.shares_owned * self.df['Close'].iloc[i])
            elif self.df['Position'].iloc[i] == -1:
                if self.shares_owned > 0:
                    self.current_budget += (self.shares_owned * self.df['Close'].iloc[i])
                    self.shares_owned = 0

        if self.shares_owned > 0:
            self.current_budget += (self.shares_owned * self.df['Close'].iloc[-1])
            self.shares_owned = 0

    def train_ml_model(self):
      
        X = self.df[['Open', 'High', 'Low', 'Close', 'Volume']]
        y = self.df['Signal']
        self.ml_model.fit(X, y)

    def integrate_ml_strategy(self):
        X = self.df[['Open', 'High', 'Low', 'Close', 'Volume']]
        self.train_ml_model()
        predictions = self.ml_model.predict(X)
        self.df['ML_Signal'] = predictions
        self.df['ML_Position'] = self.df['ML_Signal'].diff()
    

    def evaluate_strategy(self):
        initial_value = self.initial_budget
        final_value = self.current_budget
        profit_loss = final_value - initial_value
        return profit_loss

    def print_summary(self):
        print("=== Trading Summary ===")
        print(f"Symbol: {self.symbol}")
        print(f"From: {self.from_date} To: {self.to_date}")
        print(f"Initial Budget: ${self.initial_budget}")
        print(f"Final Budget: ${self.current_budget}")
        profit_loss = trader.evaluate_strategy()
        print(f"Profit/Loss: ${profit_loss:.2f}")

# # Example usage:
# trader = AlgorithmicTrader(symbol='MSFT', from_date='2018-01-01', to_date='2023-12-31')
# trader.initialize_data()
# trader.calculate_moving_averages()
# trader.identify_golden_cross()
# trader.determine_max_shares()
# trader.execute_trades()
# trader.integrate_ml_strategy()
# trader.evaluate_strategy()
# trader.print_summary()




