#!/usr/bin/env python3

"""
These are Personal Data projects
"""

from typing import List
import re
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor method
            """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats a record
        Returns
        _ _ _ _ _

        str
        formatted record
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """
    Logger function for creating a logger
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(
        RedactingFormatter(
            list(
                ("name",
                 "email",
                 "phone",
                 "ssn",
                 "password"))))
