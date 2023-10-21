#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        pagination = self.dataset()
        return pagination[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_pages = math.ceil(len(self.dataset()) / page_size)
        current_page = page
        next_page = current_page + 1 if current_page < total_pages else None
        prev_page = current_page - 1 if current_page > 1 else None

        page_data = self.get_page(page, page_size)

        hyper_info = {
            "page_size": len(page_data),
            "page": current_page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hyper_info


def index_range(page, page_size):

    start_index = page * page_size
    end_index = start_index - page_size
    return (end_index, start_index)
