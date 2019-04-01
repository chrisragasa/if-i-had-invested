from numbers import Number

def get_prev_price(data, date):
    """Gets the closing stock price for a specified month
    
    Args:
        1) data - JSON object that holds API data
        2) month - month to get close price from. 
        Must be passed in the following format:
            "YYYY-MM"
            "2019-01"
    
    Returns:
        Closing stock price for a specified month
        If error or no valid stock price data, returns -1
    """
    if not _is_valid_data(data):
        return -1
    else:
        monthly_time_series = data.get("Monthly Time Series")
        for m, p in monthly_time_series.items():
            if date in m:
                return p["4. close"]
        return -1

def get_current_price(data):
    """Gets the most recent opening stock price
    
    Args:
        1) data - JSON object that holds API data
    
    Returns:
        Closing stock price for a specified month
        If error or no valid stock price data, returns -1
    """
    if not _is_valid_data(data):
        return -1
    else:
        last_refreshed_date = data["Meta Data"]["3. Last Refreshed"].split(" ")[0]
        prices = data["Time Series (Daily)"]
        current_price = prices.get(last_refreshed_date)
        return current_price["1. open"]

def dollars_to_shares(dollars, shareprice):
    if not isinstance(dollars, Number) or not isinstance(shareprice, Number):
        return -1
    if dollars < 0 or shareprice <= 0:
        return -1
    return dollars // shareprice

def shares_to_dollars(sharecount, shareprice):
    if not isinstance(sharecount, Number) or not isinstance(shareprice, Number):
        return -1
    if sharecount < 0 or shareprice < 0:
        return -1 
    return sharecount * shareprice

def _is_valid_data(data):
    if data.get("Note") or data.get("Error Message"):
        return False
    else:
        return True




