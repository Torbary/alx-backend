#!/usr/bin/env python3
"""
Module for pagination index range calculation.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    # Calculate the start index based on the given page number and page size
    start_index = (page - 1) * page_size

    # Calculate the end index
    end_index = start_index + page_size

    return start_index, end_index  # Ajusting the end index to be inclusive
