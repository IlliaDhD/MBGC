import logging
import unittest

from app.data_processing.data_processing import map_description_to_category
from tests.common import TestTransactions


class DataProcessingTests(unittest.TestCase):


    def test_map_description_to_category(self):
        categories = TestTransactions.generate_categories()
        mappings = TestTransactions.generate_mappings(list(categories.keys()))
        test_data, mapped_data, new_institutions = TestTransactions.generate_test_data(mappings, categories)

        actual_mapped_data, actual_new_institutions = map_description_to_category(test_data, categories, mappings)
        operation_category = [record['operationCategory'] for record in mapped_data]

        logging.info(f"Simulated data category mapping for {len(actual_mapped_data)} transactions")

        self.assertEqual(list(actual_mapped_data.get('operationCategory')), operation_category)
        self.assertEqual(actual_new_institutions, new_institutions)
