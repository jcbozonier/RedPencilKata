import unittest, datetime
from red_line_promotion import *

def always_passing_test():
  assert True

class given_a_good_with_no_price_change_ever(unittest.TestCase):
    def setUp(self):
        self.good = Good(price = 100.00)
    def test_when_price_is_changed_to_same_price(self):
        self.good.reduce_price(by=0.0)
        self.assertFalse(self.good.is_redline_promotion_effective_now(), "It should not start a red line promotion.")
    def test_when_price_is_reduced_by_5_percent(self):
        self.good.reduce_price(by=0.05)
        self.assertTrue(self.good.is_redline_promotion_effective_now(), "It should start a red line promotion.")
    def test_when_price_is_reduced_by_30_percent(self):
        self.good.reduce_price(by=0.30)
        self.assertTrue(self.good.is_redline_promotion_effective_now(), "It should start a red line promotion.")
    def test_when_price_is_reduced_by_5_percent_to_30_percent(self):
        self.good.reduce_price(by=0.10)
        self.assertTrue(self.good.is_redline_promotion_effective_now(), "It should start a red line promotion.")

class given_a_good_with_multiple_price_changes_one_yesterday_one_today(unittest.TestCase):
    def setUp(self):
        self.yesterday = datetime.datetime.strptime('2015-03-28 12:14:12', '%Y-%m-%d %H:%M:%S')
        self.today = datetime.datetime.strptime('2015-03-29 12:14:12', '%Y-%m-%d %H:%M:%S')
        self.good = Good(price=100.00)
        self.good.reduce_price(by=0.05, effective=self.yesterday)
        self.good.reduce_price(by=0.1, effective=self.today)
    def test_when_price_is_calculated_for_yesterday(self):
        good_price = self.good.get_price(effective=self.yesterday)
        self.assertEqual(good_price, 95.00, "It should have only the inital price reduction.")
    def test_when_price_is_calculated_for_today(self):
        good_price = self.good.get_price(effective=self.today)
        self.assertEqual(good_price, 85.50, "It should compound the price reductions.")

class given_a_good_with_a_price_change_in_the_last_thirty_days(unittest.TestCase):
    def setUp(self):
        self.todays_date = datetime.datetime.strptime('2015-03-29 12:14:12', '%Y-%m-%d %H:%M:%S')
        self.good = Good(price=200.00)
        self.good.reduce_price(by=0.05, effective=datetime.datetime.strptime('2015-03-01 17:59:59', '%Y-%m-%d %H:%M:%S'))
    def test_when_price_is_reduced_by_5_percent(self):
        red_line_promotion_started = self.good.reduce_price(by=0.05, effective=self.todays_date)
        self.assertFalse(red_line_promotion_started, "It should NOT start a red line promotion.")

class given_a_good_with_a_price_change_before_the_last_thirty_days(unittest.TestCase):
    def setUp(self):
        self.todays_date = datetime.datetime.strptime('2015-03-29 12:14:12', '%Y-%m-%d %H:%M:%S')
        self.good = Good(price=200.00)
        self.good.reduce_price(by=0.05, effective=datetime.datetime.strptime('2015-02-26 11:59:59', '%Y-%m-%d %H:%M:%S'))
    def test_when_price_is_reduced_by_5_percent(self):
        red_line_promotion_started = self.good.reduce_price(by=0.05, effective=self.todays_date)
        self.assertTrue(red_line_promotion_started, "It should start a red line promotion.")

class given_a_good_in_a_red_pencil_promotion(unittest.TestCase):
    def setUp(self):
        self.yesterday = datetime.datetime.strptime('2015-03-28 12:14:12', '%Y-%m-%d %H:%M:%S')
        self.today = datetime.datetime.strptime('2015-03-29 12:14:12', '%Y-%m-%d %H:%M:%S')
        self.good = Good(price=200.00)
        red_line_promotion_started = self.good.reduce_price(by=0.05, effective=self.yesterday)
        assert red_line_promotion_started, "A redline promotion should be started."
    def test_when_price_is_reduced_by_5_percent(self):
        red_line_promotion_started = self.good.reduce_price(by=0.05, effective=self.today)
        self.assertFalse(red_line_promotion_started, "It should NOT start another red line promotion.")

class given_a_good_price(unittest.TestCase):
    def test_when_reduced_by_some_percentage(self):
        good_price = 100.00
        reduced_price = reduce_price_of(good_price, by=0.05)
        self.assertEqual(reduced_price, 95.00, "It should reduce the price by the percentage amount.")
