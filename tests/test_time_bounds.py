import time
import random
import unittest

from unittest.mock import patch

from app.api.time_bounds import bounds_from_period
from tests.common import TestPeriods


class TestTimeBounds(unittest.TestCase):
    mocked_time: float = time.time()

    def test_bounds_from_period(self):
        period, expected_bounds = TestPeriods.generate_period(self.mocked_time)

        with patch("app.api.time_bounds.time.time", return_value=self.mocked_time):
            actual_bounds = bounds_from_period(period)

        self.assertEqual(expected_bounds, actual_bounds)


    def test_bounds_from_period_less_than_a_month(self):
        period, expected_bounds = TestPeriods.generate_period_with_days_number(self.mocked_time, random.randint(1, 30))

        with patch("app.api.time_bounds.time.time", return_value=self.mocked_time):
            actual_bounds = bounds_from_period(period)

        self.assertEqual(expected_bounds, actual_bounds)
