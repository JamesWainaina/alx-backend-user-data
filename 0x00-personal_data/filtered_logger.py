#!/usr/bin/env python3

"""
These are Personal Data projects
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """
    Function that returns the log message obfuscated.
    """

    for field in fields:
        message = re.sub(
            rf'({field})=([^{seperator}]*)', rf'\1={redaction}', message
        )
    return message
