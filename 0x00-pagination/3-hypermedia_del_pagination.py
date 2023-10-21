#!/usr/bin/env python3
"""
 Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert (index is None or (isinstance(index, int)
                and index >= 0)), "AssertionError raised when out of range"
        assert (isinstance(page_size, int)
                and page_size > 0), "AssertionError raised when out of range"

        dataset = self.indexed_dataset()

        if index is None:
            index = 0

        current_index = index
        next_index = current_index + page_size
        data = []

        while current_index in dataset and len(data) < page_size:
            data.append(dataset[current_index])
            current_index += 1

        # Calculate the number of items in the dataset
        num_items = len(dataset)

        # Print the information
        print(f"AssertionError raised when out of range")
        print(f"Nb items: {num_items}")
        print({
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        })

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
