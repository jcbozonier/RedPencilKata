import datetime

def red_pencil_promotion_started(from_price, to_price, todays_date=datetime.datetime.now(), last_price_change_date=datetime.datetime.min):
    time_delta_since_last_price_change = todays_date - last_price_change_date
    if time_delta_since_last_price_change.days > 30:
        return to_price/from_price <= 0.95 and to_price/from_price >= 0.7

def reduce_price_of(original_price, by):
    return (1-by)*original_price

class Good():
    def __init__(self, price):
        self.price = price
        self.price_reduction_history = []
    def reduce_price(self, by, effective=datetime.datetime.now()):
        current_price = self.get_price(effective)
        self.reduced_price = reduce_price_of(current_price, by=by)
        self.price_reduction_history.append((by, self.reduced_price, effective))
        if len(self.price_reduction_history) == 1:
            return red_pencil_promotion_started(self.price, self.reduced_price, todays_date=effective)
        return red_pencil_promotion_started(self.price, self.reduced_price, todays_date=effective, last_price_change_date=self.price_reduction_history[0][2])
    def is_redline_promotion_effective_now(self):
        return red_pencil_promotion_started(self.price, self.reduced_price)
    def get_price(self, effective):
        most_recent_price_found = self.price
        for item in self.price_reduction_history:
            if item[2] <= effective:
                most_recent_price_found = item[1]
            else:
                break
        return most_recent_price_found
