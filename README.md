# ForexSmartBot

Automated forex trading bot written in Python. It trades currency pairs such as **EURUSD**, **USDJPY** and more, using a simple moving average crossover strategy. The bot adjusts trade amounts dynamically between a specific range based on recent trading performance, aiming to optimize the investment per operation.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Customization and Improvement](#customization-and-improvement)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Contact](#contact)
- [Contribution](#contribution)

## Features

- **Multiple Currency Pairs**: Trades on stable pairs like EURUSD and USDJPY.
- **Moving Average Crossover Strategy**: Utilizes 10-period and 20-period simple moving averages to generate buy/sell signals.
- **Dynamic Trade Amounts**: Automatically adjusts the trade amount between $10 and $100 based on recent profits or losses.
- **MetaTrader 5 Integration**: Connects to MT5 via its Python API for live trading.
- **Educational Purpose**: Designed to help users understand automated trading systems and how to improve them.

## Prerequisites

- **Python 3.x** installed on your system.
- **MetaTrader 5** platform installed.
- A **demo or live trading account** with a broker that supports MT5.
- Required Python packages: Install using `pip install -r requirements.txt`.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/CryptoJoma/ForexSmartBot.git
   cd ForexSmartBot
2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   
## Usage
1. **Configure Account Details**:
- Open forex_bot.py in a text editor.
- Replace account_number, password, and server with your MT5 account credentials.
  
2. **Select Currency Pairs**:
-Modify the symbols list in the run_bot() function to include other stable currency pairs if desired.

3. **Run the Bot**:

   ```bash
   python forex_bot.py
   
## How It Works
- **Initialization**: Connects to MT5 and logs into your trading account.
- **Data Retrieval**: Fetches recent price data for selected currency pairs.
- **Signal Generation**: Calculates moving averages to generate buy/sell/hold signals.
- **Dynamic Amount Adjustment**: Adjusts trade amounts between $10 and $100 based on recent performance.
- **Order Execution**: Places market orders based on generated signals.
- **Continuous Operation**: Runs in a loop, updating every 5 minutes.
  
## Customization and Improvement
- **Strategy Enhancement**: Implement more sophisticated trading strategies or indicators.
- **Risk Management**: Add stop-loss and take-profit levels, or position sizing based on volatility.
- **Error Handling**: Improve logging and error handling for robustness.
- **Backtesting**: Use historical data to test and refine strategies before live trading.

## Disclaimer
- **Financial Risk**: Trading foreign exchange on margin carries a high level of risk and may not be suitable for all investors. Use it responsibly and at your own risk.
- **Educational Purpose**: This bot is provided for educational purposes and does not constitute financial advice.
- **No Warranty**: The software is provided "as is", without warranty of any kind.

## License
This code is provided under the Apache 2.0 License

## Contact
For any questions or support, please contact coffee@joma.dev

## Contribution
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
