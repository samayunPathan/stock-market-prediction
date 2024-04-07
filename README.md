
# Stock market prediction 


Key Features:
- Initializing Class: Create a class to encapsulate the trading strategy, allowing initialization with parameters such as symbol, from date, and to date. Example: class_Name(“AAPL”,”2018-01-01”,”2023-12-31”)
- Setting the Stage: Install the yfinance library to access historical market data.
- Data Acquisition: Download historical data for the specified symbol within the provided date range.
- Data Cleanup: Filter out duplicate data points and handle NaN values by forward filling.
- Analytical Insights: Compute the moving averages for 50 and 200 days.
- Golden Opportunity: Identify the golden cross, signaling a bullish trend, and take a buying position.
- Investment Strategy: Determine the maximum quantity of shares to purchase within the $5000 budget.
- Timely Actions: When the golden cross reverses, sell the position and close the trade. When you are in a position you can’t buy other stock.
- Final Touches: Forcefully close the position on the last row if a position is still open.
- Evaluation: Calculate profits or losses to assess the success of the trading strategy.
- initialial $5000 budget using a modular and flexible class-based approach.






#### Technologies:

- Algorithm : RandomForestClassifier
- yfinance library to access historical market data



## Installation

- Create a virtual environment:
 ``` bash 
 python -m venv venv
 ```
- Activate the virtual environment: 
```
source venv/scripts/activate 
```
- Install dependencies: 
```
pip install -r requirements.txt
```
- run : 
```
python stock_prediction_GUI.py
```




 
    