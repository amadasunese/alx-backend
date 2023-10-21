#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    if page <= 0 or page_size <= 0:
        return (0, 0)  # Invalid input, return an empty range

    start_index = page * page_size
    end_index = start_index - page_size
    return (end_index, start_index)
