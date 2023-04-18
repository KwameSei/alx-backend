#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        """ Returns a dictionary of page indexes and page data """
        data = self.dataset()
        assert page_size > 0, "Invalid page_size value"
        assert index is None or index >= 0, "Invalid index value"

        if index >= len(data):
            return {'index': index, 'next_index': None, 'page_size':
                    page_size, 'data': []}

        if index is None:
            index = 0

        next_index = index + page_size
        page_data = data[index:next_index]
        actual_page_size = len(page_data)

        while actual_page_size < page_size and next_index < len(data):
            page_data += [data[next_index]]
            next_index += 1
            actual_page_size += 1

        return {'index': index, 'next_index': next_index,
                'page_size': page_size,
                'data': page_data}
