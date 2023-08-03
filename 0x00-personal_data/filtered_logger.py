#!/usr/bin/env python3
"""
Definition of filter_datum function that returns an obfuscated log message
"""

from typing import List
import re
import logging
from os import environ
import mysql.connector


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    function that returns a connector to the database 
    (mysql.connector.connection.MySQLConnection object).

    Returns:
        A MySQLConnection object using connection details from
        environment variables
    """
    userName = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    passW = environ.get("PERSONAL_DATA_DB_PASSWORD") or ""
    hos = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    dbName = environ.get("PERSONAL_DATA_DB_NAME")

    connection = mysql.connector.connection.MySQLConnection(user=userName,
                                                     password=passW,
                                                     host=hos,
                                                     database=dbName)
    return connection


def main():
    """
    Main function to retrieve user data from database and log to console
    """
    get_db()


if __name__ == '__main__':
    main()
