from flask import Flask, render_template, request
from AlphaVantageAPI import AlphaVantageAPI
from util import get_prev_price, get_current_price, dollars_to_shares, shares_to_dollars

app = Flask(__name__)


@app.route('/stock', methods=['POST'])
def stock():
    # parse form
    ticker = request.form['ticker']
    month = request.form['month']
    year = request.form['year']
    date_formatted = year + "-" + month

    api = AlphaVantageAPI(ticker)

    # call the api to get stock data
    curr_data = api.get_TIME_SERIES_DAILY()
    prev_data = api.get_TIME_SERIES_MONTHLY()

    # get the specific stock prices from json object
    prev_price = float(get_prev_price(prev_data, date_formatted))
    curr_price = float(get_current_price(curr_data))

    # calculate the wealth difference using $10000 initial investment
    dollars_investment = 10000
    init_shares = dollars_to_shares(dollars_investment, prev_price)
    curr_val = shares_to_dollars(init_shares, curr_price)
    
    # populate content to pass to template
    wealth = {}
    wealth['prev_price'] = format(prev_price, '.2f')
    wealth['curr_price'] = format(curr_price, '.2f')
    wealth['curr_val'] = format(curr_val, '.2f')
        
    return render_template('stock.html', content=wealth)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)