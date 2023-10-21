#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    Invalid input, return an empty range
    """
    #if page <= 0 or page_size <= 0:
     #   return (0, 0)

    start_index = page * page_size
    end_index = start_index - page_size
    return (end_index, start_index)
