#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Dataset indexed by sorting position, starting at 0
        """
        dataset = self.indexed_dataset()

        # Assert that index is valid
        assert isinstance(index, int) and index >= 0 and index < len(dataset)

        data = []
        i = index
        while len(data) < page_size and i < len(dataset):
            # Only add to `data` if the key `i` exists in `dataset`
            if i in dataset:
                data.append(dataset[i])
            i += 1  # Increment `i` each time to move to the next item

        # Calculate the new index for the next page
        new_index = i

        # Prepare the response with the appropriate data
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": new_index if new_index < len(dataset) else None
        }
