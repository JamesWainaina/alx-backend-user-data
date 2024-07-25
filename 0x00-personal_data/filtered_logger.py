#!/usr/bin/env python3

"""
These are Personal Data projects
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Function to filter a message based on a list of fields

    Parameters
    ----------
    fields : List[str]
        List of fields to filter
    redaction : str
        String to replace field values with
    message : str
        String to filter
    separator : str
        String to separate fields

    Returns
    -------
    str
        Filtered message
    """
    for field in fields:
        message = re.sub(
            rf'({field})=([^{separator}]*)', rf'\1={redaction}', message)
    return message
