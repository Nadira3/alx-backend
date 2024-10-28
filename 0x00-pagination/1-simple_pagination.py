#!/usr/bin/env python3


""" this module contains a pagination function """


from typing import Tuple, dataclass_transform
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Returns a tuple of start and end indexes
        based on page number and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset."""
        # Check that page and page_size are integers greater than 0
        assert isinstance(page, int) and isinstance(page_size, int)\
            and page > 0 and page_size > 0

        # Get the index range for the pagination
        irange = index_range(page, page_size)
        dataset = self.dataset()

        # Check if the index range is out of bounds
        if irange[0] >= len(dataset) or irange[1] > len(dataset):
            return []  # Return an empty list if out of range

        # Return the sliced dataset for the requested page
        return dataset[irange[0]:irange[1]]
