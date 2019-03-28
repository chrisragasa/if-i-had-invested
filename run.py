from flask import Flask, render_template, request
import api_requests
import requests
import json

app = Flask(__name__)

apikey = "JQFUK84U8Y69YDYX"

def get_last_refreshed_closed_price(ticker):
    r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=" + apikey)
    data = json.loads(r.text)

    # check for invalid API call
    if data.get("Error Message"):
        print("Invalid API Call")
        return data

    # get the most recently refreshed stock prices (daily)
    last_refreshed_date = data["Meta Data"]["3. Last Refreshed"]
    stock_prices = data["Time Series (Daily)"][last_refreshed_date]
    return stock_prices

@app.route('/stock', methods=['POST'])
def stock():
    ticker = request.form['ticker']
    data = get_last_refreshed_closed_price(ticker)
    return render_template('stock.html', stock_data=data)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)