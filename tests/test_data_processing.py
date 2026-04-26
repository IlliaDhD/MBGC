import logging
import unittest

from app.data_processing.data_processing import map_description_to_category
from tests.common import TestTransactions as transactions


class DataProcessingTests(unittest.TestCase):

    def test_map_description_to_category(self):
        categories = transactions.generate_categories()
        mappings = transactions.generate_mappings(list(categories.keys()))
        (test_d, t_mapped_d, new_inst) = transactions.generate_test_data(
            mappings, categories)

        actual_d, actual_new_inst = map_description_to_category(
            test_d, categories, mappings)

        logging.info(
            "Simulated mapping for %s transactions",
            len(actual_d))

        self.assertEqual(actual_d, t_mapped_d)
        self.assertEqual(actual_new_inst, new_inst)
