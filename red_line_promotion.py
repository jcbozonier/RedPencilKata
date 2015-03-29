def price_changed(from_price, to_price):
    return to_price/from_price <= 0.95 and to_price/from_price >= 0.7
