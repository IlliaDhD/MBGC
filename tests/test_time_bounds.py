import time, unittest
from unittest.mock import patch

from app.api.time_bounds import bounds_from_period
from tests.common import TestPeriods


class TestTimeBounds(unittest.TestCase):


    def test_bounds_from_period(self):
        mocked_time: float = time.time()
        period, expected_bounds = TestPeriods.generate_period(mocked_time)

        with patch("app.api.time_bounds.time.time", return_value=mocked_time):
            actual_bounds = bounds_from_period(period)

        self.assertEqual(expected_bounds, actual_bounds)