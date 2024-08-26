import mysql.connector
import logging
import re

from mysql.connector import MySQLConnection, Error as MySqlError
from typing import Optional, Tuple, Union, List, Any

from lib.constant_values import Queries


sql_log = logging.getLogger(__file__)


# this library will use pydantic to make sure that typing are respected
class SqlHandler:
    """Object that help to interact directly with SQL database by doing
    different type of Queries."""

    # decorator to make sure connection already created before any queries, if not 
    # it will create the connection
    def connected(self):
        """..."""

    def __init__(
        self, host_name:Optional[str]="localhost", user_name: Optional[str]="root", password: Optional[str]="",port:Optional[int]=3306, db_name: Optional[str] = "VerbenLernen"
    ) -> None:
        """Initialization of the object SqlHandler. One object can only be connected at one database
        at the time.

        :param host_name: Ip address to the host/server, defaults to "localhost"/"127.0.0.1"
        :param user_name: name of the server, defaults to "root"
        :param password: password to connect to the server, defaults to ""
        :param port: communication port to use to communicate with the server, defaults to 3306
        :param db_name: Name of the database, defaults to "VerbenLernen"
        """
        # TODO: check typing
        self.host_name = host_name # IP address of the host
        self.user_name = user_name
        self.password = password
        self.port = port
        self.db_name = db_name
        self._is_connected_to_server= False
        self._is_connected_to_db = False
        # object that store the establish connection with the Database
        self._connection_link = None

    @property
    def is_connected_to_server(self)->bool:
        return self._is_connected_to_server
    
    @property
    def is_connected_to_db(self)->bool:
        return self._is_connected_to_db
    
    @property
    def connection_link(self)-> MySQLConnection:
        return self._connection_link
    
    def connect_to_server(self)->None:
        """Connect to the server, linked to this object
        """
        try:
            self._connection_link = mysql.connector.connect(host=self.host_name,password=self.password,port=self.port, user=self.user_name)
            sql_log.info(f"Connection established with server data: username: {self.user_name}, hostname: {self.host_name}, port: {self.port}")
            self._is_connected_to_server = True
        except MySqlError as sql_err:
            sql_log.error(f"could not connect to server {self.user_name}, due to error: {sql_err}")
            self._is_connected_to_server = False
    
    def connect_to_server_and_db(self)->None:
        """Connect to the server and database, linked to this object
        """
        try:
            self._connection_link = mysql.connector.connect(host=self.host_name,password=self.password,port=self.port, user=self.user_name, database=self.db_name)
            sql_log.info(f"Connection established with database using data: username: {self.user_name}, hostname: {self.host_name}, port: {self.port}, database_name: {self.db_name}")
            self._is_connected_to_server = True
            self._is_connected_to_db = True
        except MySqlError as sql_err:
            sql_log.error(f"could not connect to database {self.db_name}, due to error: {sql_err}")
            self._is_connected_to_server = False
            self._is_connected_to_db = False

    @connected
    def connect_to_db(self):
        """Connect to the given database
        As done with sql command: USE <data_base_name>
        """
        cursor = self._connection_link.cursor()
        query_to_use_db = Queries.USE.value + self.db_name
        try:
            cursor.execute(query_to_use_db)
            sql_log.info(f"Successfully connected to database: {self.db_name}")
            self._is_connected_to_db = True
        except MySqlError as sql_err:
            sql_log.error(f"An error occurred during command {query_to_use_db}: {sql_err}")
            self._is_connected_to_db = False

    def check_query(self, query_cmd:str)->Tuple[bool,int]:
        """Check whether the current query is well written.
        The check will only verified if the query end with one delimiter ';'

        :param query_cmd: Sql request to send to server
        :return: True if check passed otherwise False
        """
        # TODO: check typing
        filter_end_comma= ";$"
        filter_comma= ";"
        nb_of_comma_found = 0

        if re.findall(filter_end_comma, query_cmd):
            # check there is only one comma, as we want to do only one and simple query
            nb_of_comma_found = len(re.findall(filter_comma, query_cmd))
            if nb_of_comma_found == 1: # check number of comma found
                return True, 1

        # All roads not True lead to False
        return False, nb_of_comma_found

    @connected(is_connected_db_to_check=True)
    def create_table(self, table:str)->bool:
        """Create a table in the current active database, just as in sql language

        e.g: 
            sql'CREATE TABLE VerbenLernen(...);' is equivalent of the example below:

            >>> table = "VerbenLernen(
                    number INT AUTO_INCREMENT,
                    infinitive VARCHAR(30) NOT NULL,
                    present VARCHAR(30) NOT NULL,
                    PRIMARY KEY(number)
                );"
            >>> create_table(table)

            Also supported:

            >>> table= "CREATE TABLE VerbenLernen(...);"
            >>> create_table(table)

        ..Note: If delimiter is forgotten, it will be added and query executed

        :param table: Table name and data to use as a query create table
        :return: True If query executed successfully otherwise False
        """
        # TODO: check typing
        # get cursor
        cursor = self._connection_link.cursor()
        # check data_to_insert
        result, number_comma_found = self.check_query(table)

        # set query depending of the input and result
        if Queries.CREATE_TABLE.value in table:
            if result:
                query = table
            else:
                # we suppose that ";" was forgotten at the end
                query = table + ";"
        else:
            if result:
                query = Queries.CREATE_TABLE.value + table
            else:
                # we suppose that ";" was forgotten at the end
                query = Queries.CREATE_TABLE.value + table + ";"
        
        
        if number_comma_found > 1: # More than one comma found
            sql_log.exception("We only support ONE query per command, no more or sub queries in query")
            raise ValueError(f"Not supported query: {table}")
        else:
            try:
                cursor.execute(query)
                self._connection_link.commit()
                sql_log.info("Query executed successfully")
            except MySqlError as sql_err:
                sql_log.info(f"Could not execute query due to following error: {sql_err}")
                return False
        return True

    @connected(is_connected_db_to_check=True)
    def insert_into(self, data_to_insert=str)->bool:
        """Execute an insert command just as done in sql language

        :e.g:
            - in sql language: INSERT INTO TableName(...) VALUES('AAA', 'BBB'...);
            this sql command is equivalent of the example below:
            >>> data_to_insert = "VerbenLernen(
                    number INT AUTO_INCREMENT,
                    infinitive VARCHAR(30) NOT NULL,
                    present VARCHAR(30) NOT NULL,
                    PRIMARY KEY(number)
                ) VALUES('beginnen', 'beginnt');"
            >>> insert_into(data_to_insert)

            Also supported:
            
            >>> data_to_insert= "INSERT INTO TableName(...) VALUES('AAA', 'BBB'...);"
            >>> insert_into(data_to_insert)

        ..Note: If delimiter is forgotten, it will be added and query executed

        :param data_to_insert: Give only the data to insert and not the all insert query
        :return: True If query executed successfully otherwise False
        """
        # TODO: check typing
        # get cursor
        cursor = self._connection_link.cursor()
        # check data_to_insert
        result, number_comma_found = self.check_query(data_to_insert)

        # set query depending of the input and result
        if Queries.INSERT_INTO.value in data_to_insert:
            if result:
                query = data_to_insert
            else:
                # we suppose that ";" was forgotten at the end
                query = data_to_insert + ";"
        else:
            if result:
                query = Queries.INSERT_INTO.value + data_to_insert
            else:
                # we suppose that ";" was forgotten at the end
                query = Queries.INSERT_INTO.value + data_to_insert + ";"
        
        
        if number_comma_found > 1: # More than one comma found
            sql_log.exception("We only support ONE query per command, no more or sub queries in query")
            raise ValueError(f"Not supported query: {data_to_insert}")
        else:
            try:
                cursor.execute(query)
                self._connection_link.commit()
                sql_log.info("Query executed successfully")
            except MySqlError as sql_err:
                sql_log.info(f"Could not execute query due to following error: {sql_err}")
                return False
        return True

    @connected(is_connected_db_to_check=True)
    def show_db(self)->Union[List[Any], bool]:
        """Show current existing database in the current connection

        from sql command, e.g:
            > SHOW DATABASES;
            +------------------+
            |  Database        |
            +------------------+
            | database A       |
            | database B       |
            | database C       |
            +------------------+

        :return : list of databases or False if error occurred during command execution"""
        # get cursor
        cursor = self._connection_link.cursor()
        # get query
        query = Queries.SHOW_DB.value + ";"
        
        try:
            cursor.execute(query)
            databases = cursor.fetchall()
            sql_log.info("Query executed successfully")
        except MySqlError as sql_err:
            sql_log.info(f"Could not execute query due to following error: {sql_err}")
            return False
        
        return databases

    @connected(is_connected_db_to_check=True)
    def describe_table(self, table_name: str)->Union[List[Any], bool]:
        """Show the characteristics of each element of the table just as the sql command

        from sql command, e.g:
            > DESCRIBE table_to_describe;
            +-------------------------------------------+
            |  Field     |  Type         |  Null  |  ...
            +-------------------------------------------+
            | student id |  int          |  NO    |  ...
            | name       |  varchar(20)  |  NO    |  ...
            | major      |  varchar(20)  |  NO    |  ...
            +-------------------------------------------+

        :param table_name: Name of the table to describe/display
        :param return: list of characteristics of the given table 
        or False if an error occurred during command execution"""
        # get cursor
        cursor = self._connection_link.cursor()
        # get query
        query = Queries.DESCRIBE.value + table_name + ";"
        
        try:
            cursor.execute(query)
            characteristics = cursor.fetchall()
            sql_log.info("Query executed successfully")
        except MySqlError as sql_err:
            sql_log.info(f"Could not execute query due to following error: {sql_err}")
            return False
        
        return characteristics
    
    def select_any_from_any(self, items_to_select:str, table_of_selection:str, other_cmds_after_from_cmd:str=None)->Union[List[Any],bool]:
        """Select any element/item in the chosen table. Function work as the sql command 'SELECT'

        :e.g:
            - in sql language: 'SELECT * FROM VerbenLernen WHERE infinitive=bleiben;'
            this sql command is equivalent of the example below:

            >>> select_any_from_any('*','VerbenLernen','WHERE infinitive=bleiben')

        :param items_to_select: Give item to select in the table
        :param table_of_selection: Table where to find the item of selection
        :param other_cmds_after_from_cmd: other SQL commands as 'WHERE condition' as should be in the query, defaults to None
        :return: List of element selected in the table or False if an error occurred during command execution
        """

    @connected(is_connected_db_to_check=True)
    def alter_table(
        self, table_name: str, command: str, item_name: str, value: Optional[Any]
    ):
        """Alter item directly in the table"""

    @connected(is_connected_db_to_check=True)
    def drop_table(self, table_name: str):
        """Drop a table from current database on run"""

    @connected
    def use_db(self, db_name: str):
        """Select the database to use during the session"""

    @connected
    def create_db(self, db_name: str):
        """Create a database into server"""

    @connected
    def drop_db(self, db_name: str):
        """Delete a database from server"""
    
    def __enter__(self):
        """..."""
    
    def __exit__(self):
        """..."""
