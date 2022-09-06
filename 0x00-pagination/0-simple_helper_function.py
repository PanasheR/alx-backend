#!/usr/bin/env python3
"""
func named index_range takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """
    func should return tuple of size two containing:
    start index and end index corresponding to
    range of indexes to return in a list
    for those particular pagination parameters.
    """
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
