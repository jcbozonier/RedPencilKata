import unittest
from red_line_promotion import price_changed

def always_passing_test():
  assert True

class given_a_good_with_no_price_change_ever(unittest.TestCase):
    def setUp(self):
        self.original_good_price = 100.00
    def test_when_price_is_changed_to_same_price(self):
        red_line_promotion_started = price_changed(from_price=100.00, to_price=100.00)
        self.assertFalse(red_line_promotion_started, "It should not start a red line promotion.")
