import random
from typing import Dict, List, Tuple

from config import Config


class TestTransactions:
    @staticmethod
    def rand_num(a: int = 1, b: int = 20) -> int:
        return random.randint(a, b)

    @classmethod
    def generate_categories(cls) -> Dict[str, str]:
        categories: Dict[str, str] = {}

        for _ in range(cls.rand_num(b=10)):
            key = f"{cls.rand_num()}.{cls.rand_num()}"
            categories[key] = f"Test:{cls.rand_num()}"

        return categories

    @classmethod
    def generate_mappings(cls, categories: List[str]) -> Dict[str, str]:
        mappings: Dict[str, str] = {}

        for n in range(cls.rand_num(b=30)):
            key = f"Institution_{n}"
            mappings[key] = random.choice(categories)

        return mappings

    @classmethod
    def generate_test_data(
            cls, mappings: Dict[str, str],
            categories: Dict[str, str]
    ) -> Tuple[List[Dict[str, str]], List[Dict[str, str]], List[str]]:
        institutions: List[str] = [key for key in mappings.keys()]
        new_institutions: List[str] = []
        data_rows: List[Dict[str, str]] = []
        result_rows: List[Dict[str, str]] = []

        for _ in range(cls.rand_num(b=30)):
            institution = random.choice(institutions)
            data_rows.append({'description': institution})
            # creates an expected result
            result_rows.append({
                'description': institution,
                'operationCategory': categories[mappings[institution]]
                })

        for num in range(cls.rand_num(b=10)):  # the loop adds new institutions
            new_institution = f"New_institution_{num}"
            data_rows.append({'description': new_institution})
            result_rows.append({
                'description': new_institution,
                'operationCategory': "test"})
            new_institutions.append(new_institution)

        return data_rows, result_rows, new_institutions


class TestPeriods:

    @staticmethod
    def generate_period(
     start_time: float) -> Tuple[int, List[Tuple[float, float]]]:
        periods_number = random.randint(1, 10)
        expected_bounds: List[Tuple[float, float]] = []
        period: int = Config.month_unix_period * periods_number

        for _ in range(periods_number):
            from_time = start_time - Config.month_unix_period
            expected_bounds.append((from_time, start_time))
            start_time = from_time

        return period, expected_bounds

    @staticmethod
    def generate_period_with_days_number(
     start_time: float,
     days_number: int) -> Tuple[int, List[Tuple[float, float]]]:
        period = days_number * Config.day_unix_period
        from_time = start_time - period
        expected_bounds: List[Tuple[float, float]] = [(from_time, start_time)]

        return period, expected_bounds
