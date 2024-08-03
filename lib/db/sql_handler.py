import mysql.connector
import logging

from typing import Optional, Any

from lib.constant_values import Queries


sql_log = logging.getLogger(__file__)


# this library will pydantic tomake sure that typing are respected
class SqlHandler:
    """..."""

    # decorator to make sure connection already created before any queries
    def connected(self):
        """..."""

    def __init__(
        self, username: str, password: str, ip_addr: str, db_name: Optional[str] = None
    ) -> None:
        """..."""
        self.is_connected_to_db = None

    def connect_to_db(self): ...

    def check_query(self): ...

    def create_table(self): ...

    def insert_into(self): ...

    def show_db(self):
        """Show current existing database  in the current connection

        from sql command, e.g:
            > SHOW DATABASES;
            +------------------+
            |  Database        |
            +------------------+
            | database A       |
            | database B       |
            | database C       |
            +------------------+

        :return :"""

    def describe_table(self, name_table: str):
        """Show the all contain of a table

        from sql command, e.g:
            > DESCRIBE table_to_desc;

        :param name_table: Name of the table to describe/display
        :param return:"""

    def alter_table(
        self, table_name: str, command: str, item_name: str, value: Optional[Any]
    ):
        """Alter item directly in the table"""

    def drop_table(self, table_name: str):
        """Drop a table from current database on run"""

    def use_db(self, db_name: str):
        """Select the database to use during the session"""

    def create_db(self, db_name: str):
        """Create a database into server"""

    def drop_db(self, db_name: str):
        """Delete a database from server"""
    
    def __enter__(self):
        """..."""
    
    def __exit__(self):
        """..."""
