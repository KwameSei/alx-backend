#!/usr/bin/env python3
""" Returning indexes of pages """
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

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returning a page with data """
        assert isinstance(page, int) and page > 0, \
            "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0"

        data = self.dataset()   # getting data using dataset method
        if len(data) == 0:
            return []

        index_start, index_end = index_range(page, page_size)
        if index_start >= len(data):
            return []
        return data[index_start:index_end]

    def index_range(page: int, page_size: int) -> tuple:
        """ Using the range function to return indexes of pages """
        index_start = (page - 1) * page_size    # start page
        index_end = page * page_size    # end page

        return index_start, index_end

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """ Returning a dictionary with key-value pairs """
        assert isinstance(page, int) and page > 0, \
            "Invalid page value"
        assert isinstance(page_size, int) and page_size > 0, \
            "Invalid page size value"

        get_data = self.dataset()    # getting data using dataset method
        received_data = self.get_page(page, page_size)
        page_count = len(get_data) / page_size
        total_pages = math.ceil(page_count)

        if not received_data:
            return {
                "page_size": page_size,
                "page": page,
                "data": [],
                "next_page": None,
                "prev_page": None,
                "total_pages": total_pages,
            }

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        if page >= total_pages:
            next_page = None
        else:
            next_page = page + 1

        return {
            "page_size": page_size,
            "page": page,
            "data": received_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
