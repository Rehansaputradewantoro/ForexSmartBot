import MetaTrader5 as mt5
import pandas as pd
import time

# Initialize the MT5 connection
def initialize_mt5():
    if not mt5.initialize():
        print("Initialization failed")
        mt5.shutdown()
        return False
    return True

# Login to your MT5 account
def login(account_number, password, server):
    authorized = mt5.login(account_number, password=password, server=server)
    if not authorized:
        print(f"Failed to connect to account #{account_number}, error code: {mt5.last_error()}")
        return False
    print(f"Connected to account #{account_number}")
    return True

# Fetch historical data
def get_data(symbol, timeframe, bars):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    if rates is None or len(rates) == 0:
        print(f"No data for {symbol}")
        return None
    data = pd.DataFrame(rates)
    data['time'] = pd.to_datetime(data['time'], unit='s')
    return data

# Calculate moving averages and generate signals
def generate_signal(data):
    data['SMA_10'] = data['close'].rolling(window=10).mean()
    data['SMA_20'] = data['close'].rolling(window=20).mean()
    if data['SMA_10'].iloc[-1] > data['SMA_20'].iloc[-1]:
        return 'buy'
    elif data['SMA_10'].iloc[-1] < data['SMA_20'].iloc[-1]:
        return 'sell'
    else:
        return 'hold'

# Adjust trade amount between $10 and $100
def adjust_amount(profit_history):
    base_amount = 10.0
    if profit_history:
        recent_profit = sum(profit_history[-5:])
        adjusted_amount = base_amount + recent_profit
        return min(max(adjusted_amount, 10.0), 100.0)
    else:
        return base_amount

# Place an order
def place_order(symbol, order_type, volume):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"{symbol} not found")
        return False
    if not symbol_info.visible:
        if not mt5.symbol_select(symbol, True):
            print(f"Failed to select {symbol}")
            return False

    point = symbol_info.point
    price = mt5.symbol_info_tick(symbol).ask if order_type == 'buy' else mt5.symbol_info_tick(symbol).bid
    deviation = 20

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_BUY if order_type == 'buy' else mt5.ORDER_TYPE_SELL,
        "price": price,
        "deviation": deviation,
        "magic": 10032021,
        "comment": "Forex Trading Bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order failed, retcode={result.retcode}")
        return False
    print(f"Order executed successfully, {order_type} {volume} lots of {symbol}")
    return True

# Main trading loop
def run_bot():
    symbols = ['EURUSD', 'USDJPY']  # You can add more symbols
    profit_history = []

    while True:
        for symbol in symbols:
            data = get_data(symbol, mt5.TIMEFRAME_M5, 50)
            if data is None:
                continue

            signal = generate_signal(data)
            print(f"{symbol}: {signal}")

            if signal != 'hold':
                amount = adjust_amount(profit_history)
                volume = amount / 10000  # Convert dollar amount to lot size (assuming $10,000 per lot)
                success = place_order(symbol, signal, volume)
                if success:
                    # Simulate profit/loss for demonstration purposes
                    profit = (volume * 100) if signal == 'buy' else (-volume * 100)
                    profit_history.append(profit)
                    if len(profit_history) > 10:
                        profit_history.pop(0)
        time.sleep(300)  # Wait for 5 minutes before next iteration

# Entry point
if __name__ == "__main__":
    if initialize_mt5():
        account_number = 12345678      # Replace with your MT5 account number
        password = "your_password"     # Replace with your MT5 account password
        server = "YourBroker-Server"   # Replace with your broker's server name

        if login(account_number, password, server):
            run_bot()
        mt5.shutdown()
