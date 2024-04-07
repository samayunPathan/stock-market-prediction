from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit
import stock_prediction_algo  # import the separate algorithmic module

class AlgoTraderGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.symbol_label = QLabel("Stock Symbol:")
        self.symbol_input = QLineEdit()
        self.from_date_label = QLabel("From Date (YYYY-MM-DD):")
        self.from_date_input = QLineEdit()
        self.to_date_label = QLabel("To Date (YYYY-MM-DD):")
        self.to_date_input = QLineEdit()
        self.budget_label = QLabel("Initial Budget:")
        self.budget_input = QLineEdit()

        self.run_button = QPushButton("Run Strategy (Backtest)")
        self.run_button.clicked.connect(self.run_strategy)

        self.output_label = QLabel("Strategy Results:")
        self.output_text = QTextEdit(readOnly=True)

        self.layout.addWidget(self.symbol_label)
        self.layout.addWidget(self.symbol_input)
        self.layout.addWidget(self.from_date_label)
        self.layout.addWidget(self.from_date_input)
        self.layout.addWidget(self.to_date_label)
        self.layout.addWidget(self.to_date_input)
        self.layout.addWidget(self.budget_label)
        self.layout.addWidget(self.budget_input)
        self.layout.addWidget(self.run_button)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_text)

        self.setWindowTitle("Algorithmic Trading Backtest")
        self.show()

    def run_strategy(self):
        # user input
        symbol = self.symbol_input.text()
        from_date = self.from_date_input.text()
        to_date = self.to_date_input.text()
        try:
            initial_budget = float(self.budget_input.text())
        except ValueError:
            self.output_text.setText("Invalid budget format. Please enter a number.")
            return

        self.output_text.clear()

        # create instance of AlgorithmicTrader 
        trader = stock_prediction_algo.AlgorithmicTrader(symbol, from_date, to_date, initial_budget)
        trader.initialize_data()
        trader.calculate_moving_averages()
        trader.identify_golden_cross()
        trader.determine_max_shares()
        trader.execute_trades()
        final_value = trader.evaluate_strategy()

        # results
        output_text = f"Final Value: ${final_value:.2f}\n"
        output_text += f"Profit/Loss: ${final_value - initial_budget:.2f}"
        self.output_text.setText(output_text)

# create and run the GUI
if __name__ == '__main__':
    app = QApplication([])
    window = AlgoTraderGUI()
    app.exec_()
