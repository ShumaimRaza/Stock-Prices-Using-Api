import tkinter as tk
from tkinter import ttk
import requests

API_KEY = 'H62C7PICFM215OR8'  # Replace with your Alpha Vantage API key

def retrieve_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def get_stock_prices():
    symbol = stock_var.get()
    stock_data = retrieve_stock_data(symbol)

    result_frame = tk.Frame(root, bg='white')
    result_frame.pack(pady=20)

    if 'Global Quote' in stock_data:
        global_quote = stock_data['Global Quote']
        symbol_label = tk.Label(result_frame, text='Symbol:', bg='white', font=('Arial', 12, 'bold'))
        symbol_label.grid(row=0, column=0, sticky='e')
        symbol_value_label = tk.Label(result_frame, text=global_quote['01. symbol'], bg='white', font=('Arial', 12))
        symbol_value_label.grid(row=0, column=1, sticky='w')

        price_label = tk.Label(result_frame, text='Price: $', bg='white', font=('Arial', 12, 'bold'))
        price_label.grid(row=1, column=0, sticky='e')
        price_value_label = tk.Label(result_frame, text=global_quote['05. price'], bg='white', font=('Arial', 12))
        price_value_label.grid(row=1, column=1, sticky='w')

    else:
        error_label = tk.Label(result_frame, text='Error retrieving data', bg='white', font=('Arial', 12, 'bold'), fg='red')
        error_label.grid(row=0, column=0, columnspan=2)

root = tk.Tk()
root.title("Stock Market Data App")
root.configure(bg='white')

dropdown_frame = tk.Frame(root, bg='white')
dropdown_frame.pack(pady=20)

stock_label = tk.Label(dropdown_frame, text="Select a stock:", font=('Arial', 14), bg='white')
stock_label.grid(row=0, column=0, padx=10)

stock_options = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
stock_var = tk.StringVar()
stock_dropdown = ttk.Combobox(dropdown_frame, textvariable=stock_var, values=stock_options, state="readonly", font=('Arial', 12))
stock_dropdown.grid(row=0, column=1)
stock_dropdown.current(0)

get_prices_button = tk.Button(root, text="Get Stock Prices", command=get_stock_prices, font=('Arial', 14), bg='gray', fg='white', activebackground='darkgray', activeforeground='white')
get_prices_button.pack(pady=10)

result_frame = tk.Frame(root, bg='white')
result_frame.pack(pady=20)

result_frame.columnconfigure(0, weight=1)
result_frame.columnconfigure(1, weight=1)

root.columnconfigure(0, weight=1)

root.mainloop()
