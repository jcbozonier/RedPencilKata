import unittest, datetime
from red_line_promotion import price_changed

def always_passing_test():
  assert True

class given_a_good_with_no_price_change_ever(unittest.TestCase):
    def setUp(self):
        self.original_good_price = 100.00
    def test_when_price_is_changed_to_same_price(self):
        red_line_promotion_started = price_changed(from_price=self.original_good_price,
                                                   to_price=self.original_good_price)
        self.assertFalse(red_line_promotion_started, "It should not start a red line promotion.")
    def test_when_price_is_reduced_by_5_percent(self):
        red_line_promotion_started = price_changed(from_price=self.original_good_price,
                                                   to_price=(1 - 0.05) * self.original_good_price)
        self.assertTrue(red_line_promotion_started, "It should start a red line promotion.")
    def test_when_price_is_reduced_by_30_percent(self):
        red_line_promotion_started = price_changed(from_price=self.original_good_price,
                                                   to_price=(1 - 0.30) * self.original_good_price)
        self.assertTrue(red_line_promotion_started, "It should start a red line promotion.")
    def test_when_price_is_reduced_by_5_percent_to_30_percent(self):
        red_line_promotion_started = price_changed(from_price=self.original_good_price,
                                                   to_price=(1 - 0.10) * self.original_good_price)
        self.assertTrue(red_line_promotion_started, "It should start a red line promotion.")

class given_a_good_with_a_price_change_in_the_last_thirty_days(unittest.TestCase):
    def setUp(self):
        self.last_price_change_date = datetime.datetime.strptime('2015-03-01 17:59:59', '%Y-%m-%d %H:%M:%S')
        self.todays_date = datetime.datetime.strptime('2015-03-29 12:14:12', '%Y-%m-%d %H:%M:%S')
        self.original_good_price = 200.00
    def test_when_price_is_reduced_by_5_percent(self):
        red_line_promotion_started = price_changed(from_price = self.original_good_price,
                                                   to_price = (1 - 0.05) * self.original_good_price,
                                                   todays_date = self.todays_date,
                                                   last_price_change_date=self.last_price_change_date)
        self.assertFalse(red_line_promotion_started, "It should NOT start a red line promotion.")
