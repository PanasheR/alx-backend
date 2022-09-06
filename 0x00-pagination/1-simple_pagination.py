#!/usr/bin/env python3
"""
func named index_range takes two integer arguments page and page_size
"""
import csv
import math
from typing import List


class Server:
    """class to paginate database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dataset cached
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        assert to verify both arguments are integers greater than 0
        index_range to find correct indexes to paginate dataset correctly
        and return appropriate page of the dataset
        """
        assert (isinstance(page, int) and isinstance(page_size, int)
                and page > 0 and page_size > 0)
        range = index_range(page, page_size)
        self.dataset()
        return self.__dataset[range[0]:range[1]]


def index_range(page, page_size):
    """
    func named index_range takes two integer arguments:page & page_size.
    func should return tuple of size two containing:
    start index and end index corresponding to
    range of indexes to return in a list
    for those particular pagination parameters.
    Page numbers are 1-indexed
    """
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
