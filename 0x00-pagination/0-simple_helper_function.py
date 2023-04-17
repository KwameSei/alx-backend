#!/usr/bin/env python3
""" Returning indexes of pages """


def index_range(page: int, page_size: int) -> tuple:
    """ Using the range function to return indexes of pages """
    index_start = (page - 1) * page_size    # start page
    index_end = page * page_size    # end page

    return index_start, index_end
