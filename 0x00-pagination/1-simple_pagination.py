#!/usr/bin/env python3
"""
Simple helper function
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Invalid input, return an empty range
    """

    start_index = page * page_size
    end_index = start_index - page_size
    return (end_index, start_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass
