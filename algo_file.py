import pandas as pd
import yfinance as yf
class AlgorithmicTrader:
    def __init__(self, symbol, from_date, to_date, initial_budget=5000):
        self.symbol = symbol
        self.from_date = from_date
        self.to_date = to_date
        self.initial_budget = initial_budget
        self.current_budget = initial_budget
        self.shares_owned = 0
        self.df = None
        
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
        # Forcefully close the position on the last row if a position is still open
        if self.shares_owned > 0:
            self.current_budget += (self.shares_owned * self.df['Close'].iloc[-1])
            self.shares_owned = 0
        
    def evaluate_strategy(self):
        final_value = self.current_budget + (self.shares_owned * self.df['Close'].iloc[-1])
        return final_value - self.initial_budget
        
        