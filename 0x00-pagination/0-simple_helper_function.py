#!/usr/bin/env python3


""" this module contains a pagination function """


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        arg 1 - page
        arg 2 - page_size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
