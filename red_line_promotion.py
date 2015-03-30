import datetime

def price_changed(from_price, to_price, todays_date=datetime.datetime.now(), last_price_change_date=datetime.datetime.min):
    time_delta_since_last_price_change = todays_date - last_price_change_date
    if time_delta_since_last_price_change.days > 30:
        return to_price/from_price <= 0.95 and to_price/from_price >= 0.7

def reduce_price_of(original_price, by):
    return (1-by)*original_price
