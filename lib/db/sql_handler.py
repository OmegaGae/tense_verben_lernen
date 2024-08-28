import mysql.connector
import logging
import functools
import re

from mysql.connector import MySQLConnection, Error as MySqlError
from typing import Optional, Tuple, Union, List, Any, Callable

from lib.constant_values import Queries


sql_log = logging.getLogger(__file__)


# this library will use pydantic to make sure that typing are respected
class SqlHandler:
    """Object that help to interact directly with SQL database by doing
    different type of Queries."""

    # decorator to make sure connection already created before any queries, if not 
    # it will create the connection
    @staticmethod
    def _connected(func:Callable, is_connected_db_to_check:bool=False)->Union[List[Any], bool, None]:
        """Decorator to check whether before any SQL query on database,
         a connection to the server exist

        ..Note: If connection to server or database does not exist but is needed, it will be created automatically using default value
            given at the initialization of this class object.

        :param is_connected_db_to_check: Enable flag if connection to database need to be checked, defaults to False
        :return: Wrap function result, as link to this class, should be True if everything went well otherwise False or None
        """
        # To not loose documentation, module name and annotation information of func through is_connected
        @functools.wraps(func)
        def is_connected(self, *args, **kwargs)-> Union[List[Any], bool, None]:
            """Decorator to check whether before any SQL query on database, a connection to the server exist

            ..Note: If connection to server or database does not exist but is needed, it will be created automatically using default value
                given at the initialization of this class object.

            :return: Wrap function result, as link to this class, should be True if everything went well otherwise False or None
            :raises AssertionError: Error raised when we could not connect to server or database
            """
            # check server open
            if not self._is_connected_to_server:
                result_conn_server = self.connect_to_server()
                assert result_conn_server, "Failed to connect to server"
            
            # check database open if requested
            if is_connected_db_to_check:
                if not self._is_connected_to_db:
                    result_conn_db = self.connect_to_db()
                    assert result_conn_db, "Failed to connect to server"
            # execute function
            results = func(self, *args, **kwargs)

            return results
    
        return is_connected

    def __init__(
        self, host_name:Optional[str]="localhost", user_name: Optional[str]="root", password: Optional[str]="",port:Optional[int]=3306, db_name: Optional[str] = "VerbenLernen"
    ) -> None:
        """Initialization of the SqlHandler. One instance can only be connected at one database
        at a time.

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
    
    def connect_to_server(self)->bool:
        """Connect to the server, linked to this object (see in initialization server data)

        :return: True if the command was successfully executed otherwise False
        """
        try:
            self._connection_link = mysql.connector.connect(host=self.host_name,password=self.password,port=self.port, user=self.user_name)
            sql_log.info(f"Connection established with server data: username: {self.user_name}, hostname: {self.host_name}, port: {self.port}")
            self._is_connected_to_server = True
        except MySqlError as sql_err:
            sql_log.error(f"could not connect to server {self.user_name}, due to error: {sql_err}")
            self._is_connected_to_server = False
            return False
        return True
    
    def connect_to_server_and_db(self)->bool:
        """Connect to the server and database, linked to this object
        
        :return: True if the command was successfully executed otherwise False
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
            return False
        return True

    @_connected
    def connect_to_db(self)->bool:
        """Connect to the given database
        As done with sql command: USE <database_name>

        :return: True if the command was successfully executed otherwise False
        """
        cursor = self._connection_link.cursor()
        query = Queries.USE.value + self.db_name + ";"
        try:
            cursor.execute(query)
            sql_log.info(f"Successfully connected to database: {self.db_name}")
            self._is_connected_to_db = True
        except MySqlError as sql_err:
            sql_log.error(f"An error occurred during command {query}: {sql_err}")
            self._is_connected_to_db = False
            return False
        return True

    def check_query(self, query_cmd:str)->Tuple[bool,int]:
        """Check whether the current query is well written.
        The check will only verified that the query end with one delimiter ';'

        :param query_cmd: Sql request to send to server
        :return: True if check passed otherwise False, and number of semicolon found
        """
        # TODO: check typing
        filter_end_semicolon= ";$"
        filter_semicolon= ";"
        nb_of_semicolon_found = 0
    
        if re.findall(filter_end_semicolon, query_cmd):
            # check there is only one comma, as we want to do only one and simple query
            nb_of_semicolon_found = len(re.findall(filter_semicolon, query_cmd))
            if nb_of_semicolon_found == 1: # check number of comma found
                return True, 1

        # All roads not True lead to False
        return False, nb_of_semicolon_found

    @_connected(is_connected_db_to_check=True)
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

            >>> table= "CREATE TABLE VerbenLernen(                    
                    number INT AUTO_INCREMENT,
                    infinitive VARCHAR(30) NOT NULL,
                    present VARCHAR(30) NOT NULL,
                    PRIMARY KEY(number)
                );"
            >>> create_table(table)

        ..Note: If delimiter is forgotten, it will be added and query executed

        :param table: Table name and data to use as a query create table
        :return: True If query executed successfully otherwise False
        :raises ValueError: Error raised when there is more than 1 query in a query as
            multi-queries/sub-queries in a query, are not supported
        """
        # TODO: check typing
        # get cursor
        cursor = self._connection_link.cursor()
        # check data_to_insert
        result, number_semicolon_found = self.check_query(table)

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
        
        
        if number_semicolon_found > 1: # More than one semicolon found
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

    @_connected(is_connected_db_to_check=True)
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
            
            >>> data_to_insert= "INSERT INTO VerbenLernen(                    
                    number INT AUTO_INCREMENT,
                    infinitive VARCHAR(30) NOT NULL,
                    present VARCHAR(30) NOT NULL,
                    PRIMARY KEY(number)
                ) VALUES('beginnen', 'beginnt');"
            >>> insert_into(data_to_insert)

        ..Note: If delimiter is forgotten, it will be added and query executed

        :param data_to_insert: Give only the data to insert and not the all insert query
        :return: True If query executed successfully otherwise False
        :raises ValueError: Error raised when there is more than 1 query in a query as
            multi-queries/sub-queries in a query, are not supported
        """
        # TODO: check typing
        # get cursor
        cursor = self._connection_link.cursor()
        # check data_to_insert
        result, number_semicolon_found = self.check_query(data_to_insert)

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
        
        
        if number_semicolon_found > 1: # More than one comma found
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

    @_connected
    def show_db(self)->Union[List[Any], bool]:
        """Show current existing database from the current connection

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

    @_connected(is_connected_db_to_check=True)
    def describe_table(self, table_name: str)->Union[List[Any], bool]:
        """Show the characteristics of each element of the table just as in the SQL language

        From sql command, e.g:
            > DESCRIBE VerbenLernen;
            +-------------------------------------------+
            |  Field     |  Type         |  Null  |  ...
            +-------------------------------------------+
            | student id |  int          |  NO    |  ...
            | name       |  varchar(20)  |  NO    |  ...
            | major      |  varchar(20)  |  NO    |  ...
            +-------------------------------------------+

        This is equivalent of the example below:

        e.g:
            >>> describe_table('VerbenLernen')

            Also supported:

            >>> describe_table('DESCRIBE VerbenLernen;')

        :param table_name: Name of the table to describe/display
        :param return: list of characteristics of the given table 
        or False if an error occurred during command execution"""
        #TODO:pydantic
        # get cursor
        cursor = self._connection_link.cursor()
        
        # check query
        result, number_semicolon_found = self.check_query(table_name)

        # set query depending of the input and result
        if Queries.DESCRIBE.value in table_name:
            if result:
                query = table_name
            else:
                # we suppose that ";" was forgotten at the end
                query = table_name + ";"
        else:
            if result:
                query = Queries.DESCRIBE.value + table_name
            else:
                # we suppose that ";" was forgotten at the end
                query = Queries.DESCRIBE.value + table_name + ";"
        

        if number_semicolon_found > 1: # More than one comma found
            sql_log.exception("We only support ONE query per command, no more or sub queries in query")
            raise ValueError(f"Not supported query: {table_name}")
        else:
            try:
                cursor.execute(query)
                characteristics = cursor.fetchall()
                sql_log.info("Query executed successfully")
                assert cursor.close(), f"Cursor could not be closed successfully"
            except MySqlError as sql_err:
                sql_log.info(f"Could not execute query due to following error: {sql_err}")
                return False
        
        return characteristics
    
    @_connected(is_connected_db_to_check=True)
    def select_any_from_any(self, items_to_select:str, table_of_selection:str, other_cmds_after_from_cmd:str=None)->Union[List[Any],bool]:
        """Select any element/item in the chosen table. Function works as the sql command 'SELECT'

        :e.g:
            - in sql language: 'SELECT * FROM VerbenLernen WHERE infinitive=bleiben;'
            this sql command is equivalent of the example below:

            >>> select_any_from_any('*','VerbenLernen','WHERE infinitive=bleiben')

        :param items_to_select: Give item to select in the table
        :param table_of_selection: Table where to find the item of selection
        :param other_cmds_after_from_cmd: other SQL commands as 'WHERE condition' as should be in the query, defaults to None
        :return: List of element selected in the table or False if an error occurred during command execution
        """
        #TODO:pydantic
        # get cursor
        cursor = self._connection_link.cursor()
        # get query
        query = Queries.SELECT.value + items_to_select + Queries.FROM.value + table_of_selection + other_cmds_after_from_cmd + ";"
        
        try:
            cursor.execute(query)
            selection = cursor.fetchall()
            sql_log.info("Query executed successfully")
            assert cursor.close(), f"Cursor could not be closed successfully"
        except MySqlError as sql_err:
            sql_log.info(f"Could not execute query due to following error: {sql_err}")
            return False
        
        return selection

    @_connected(is_connected_db_to_check=True)
    def drop_table(self, table_name: str)->bool:
        """Drop a table from current database on run, just as SQL command 'DROP TABLE'
        
        From sql command, e.g:
            > DROP TABLE VerbenLernen;

        This is equivalent of the example below:

        e.g:
            >>> drop_table('VerbenLernen')

            Also supported:

            >>> drop_table('DROP TABLE VerbenLernen;')

        :param table_name: Table in the current database in run, to drop
        :return: True if command executed successfully otherwise False
        """
        # TODO:pydantic
        # get cursor
        cursor = self._connection_link.cursor()

        # check query
        result, number_semicolon_found = self.check_query(table_name)

        # set query depending of the input and result
        if Queries.DROP_TABLE.value in table_name:
            if result:
                query = table_name
            else:
                # we suppose that ";" was forgotten at the end
                query = table_name + ";"
        else:
            if result:
                query = Queries.DROP_TABLE.value + table_name
            else:
                # we suppose that ";" was forgotten at the end
                query = Queries.DROP_TABLE.value + table_name + ";"
        

        if number_semicolon_found > 1: # More than one comma found
            sql_log.exception("We only support ONE query per command, no more or sub queries in query")
            raise ValueError(f"Not supported query: {table_name}")
        else:
            try:
                cursor.execute(query)
                self._connection_link.commit()
                sql_log.info("Query executed successfully")
            except MySqlError as sql_err:
                sql_log.info(f"Could not execute query due to following error: {sql_err}")
                return False
        
        return True

    @_connected
    def use_db(self, db_name: str)->bool:
        """Select the database to use during the session, just as the SQL command 'USE database_name'
        e.g: 
            sql'USE VerbenLernen;' is equivalent of the example below:

            >>> use_db('VerbenLernen')

            Also supported:

            >>> use_db('USE VerbenLernen;')

        :param db_name: Name of the database to switch to
        :return: True if the command was successfully executed otherwise False
        """
        # TODO:pydantic
        cursor = self._connection_link.cursor()

        # check query
        result, number_semicolon_found = self.check_query(db_name)

        # set query depending of the input and result
        if Queries.USE.value in db_name:
            if result:
                query = db_name
            else:
                # we suppose that ";" was forgotten at the end
                query = db_name + ";"
        else:
            if result:
                query = Queries.USE.value + db_name
            else:
                # we suppose that ";" was forgotten at the end
                query = Queries.USE.value+ db_name + ";"
        

        if number_semicolon_found > 1: # More than one comma found
            sql_log.exception("We only support ONE query per command, no more or sub queries in query")
            raise ValueError(f"Not supported query: {db_name}")
        else:
            try:
                cursor.execute(query)
                sql_log.info(f"Successfully connected to database: {self.db_name}")
                self._is_connected_to_db = True
            except MySqlError as sql_err:
                sql_log.error(f"An error occurred during command {query}: {sql_err}")
                self._is_connected_to_db = False
                return False
        return True

    @_connected
    def create_db(self, db_name: str)->bool:
        """Create a database into server, just as in sql language

        e.g: 
            sql'CREATE DATABASE VerbenLernen;' is equivalent of the example below:

            >>> create_db('VerbenLernen')

            Also supported:

            >>> create_db('CREATE DATABASE VerbenLernen;')

        ..Note: If delimiter is forgotten, it will be added and query executed

        :param db_name: Database name to use as a query
        :return: True If query executed successfully otherwise False
        """
        # TODO: check typing
        # get cursor
        cursor = self._connection_link.cursor()
        # check query
        result, number_semicolon_found = self.check_query(db_name)

        # set query depending of the input and result
        if Queries.CREATE_DATABASE.value in db_name:
            if result:
                query = db_name
            else:
                # we suppose that ";" was forgotten at the end
                query = db_name + ";"
        else:
            if result:
                query = Queries.CREATE_DATABASE.value + db_name
            else:
                # we suppose that ";" was forgotten at the end
                query = Queries.CREATE_DATABASE.value + db_name + ";"
        

        if number_semicolon_found > 1: # More than one comma found
            sql_log.exception("We only support ONE query per command, no more or sub queries in query")
            raise ValueError(f"Not supported query: {db_name}")
        else:
            try:
                cursor.execute(query)
                self._connection_link.commit()
                sql_log.info("Query executed successfully")
            except MySqlError as sql_err:
                sql_log.info(f"Could not execute query due to following error: {sql_err}")
                return False
        return True        

    @_connected
    def drop_db(self, db_name: str)->bool:
        """Drop a database from the server, just as SQL command 'DROP DATABASE'
        
        from sql command, e.g:
            > DROP DATABASE db_name;

        :param db_name: Database name to delete
        :return: True if command executed successfully otherwise False
        """
        # TODO:pydantic
        # get cursor
        cursor = self._connection_link.cursor()
        # get query
        query = Queries.DROP_DB.value + db_name + ";"
        
        try:
            cursor.execute(query)
            self._connection_link.commit()
            sql_log.info("Query executed successfully")
        except MySqlError as sql_err:
            sql_log.info(f"Could not execute query due to following error: {sql_err}")
            return False
        
        return True
    
    @_connected(is_connected_db_to_check=True)
    def create_view(self, view_name:str, characteristics_to_select:str, ref_table_name:str, any_others_cmd:str)->bool:
        """Create a view in the current active database, just as in sql language 'CREATE VIEW'

        e.g: 
            sql'CREATE VIEW A1_Verben AS SELECT * FROM VerbenLernen WHERE level='A1';' is equivalent of the example below:

            >>> create_view("A1_Verben","*","VerbenLernen", "WHERE level=A1")

        :param view_name: Name of the view to create
        :param characteristics_to_select: Characteristics to select from the table that view should show
        :param ref_table_name: Reference table that view should take to create the view to show
        :param any_others_cmd: Any other command as example a condition for view to take items, such as 'WHERE condition=a'
        :return: True if command was successfully executed otherwise False
        """
        # TODO: check typing
        # get cursor
        cursor = self._connection_link.cursor()
        # get query
        query = Queries.CREATE_VIEW.value + view_name + Queries.AS_SELECT.value + characteristics_to_select + Queries.FROM.value + ref_table_name + any_others_cmd + ";"
        
        try:
            cursor.execute(query)
            self._connection_link.commit()
            sql_log.info("Query executed successfully")
        except MySqlError as sql_err:
            sql_log.info(f"Could not execute query due to following error: {sql_err}")
            return False
        return True
    
    def disconnect_server(self)->bool:
        """Disconnect current connection to the server

        :return: True if command was successfully executed otherwise False
        """
        if not self._is_connected_to_server:
            return True
        
        cursor = self._connection_link.cursor()
        try:
            cursor.close()
            sql_log.info(f"Connection closed with server data: username: {self.user_name}, hostname: {self.host_name}, port: {self.port}")
            self._is_connected_to_server = False
            self._is_connected_to_db = False
        except MySqlError as sql_err:
            sql_log.error(f"could not disconnect to server {self.user_name}, due to error: {sql_err}")
            self._is_connected_to_server = True
            return False
        return True
          
    @_connected
    def execute_any_query(self, query:str)->bool:
        """Use this method to execute any SQL query not supported by this class

        ..Note: Please make sure to be connected to the wanted server before using this method otherwise default server 
        information may be used to connect into.
        
        :param query: Any SQL query 
        :return: True if command was executed successfully otherwise False
        """
        # TODO: check typing
        # get cursor
        cursor = self._connection_link.cursor()
        try:
            cursor.execute(query)
            self._connection_link.commit()
            sql_log.info("Query executed successfully")
        except MySqlError as sql_err:
            sql_log.info(f"Could not execute query due to following error: {sql_err}")
        return False     
        
    def __enter__(self):
        """Open automatically using context manager command 'with',
        a new connection to the server and connect to default database given
        """        
        self.connect_to_server_and_db()

    def __exit__(self):
        """Close connection to the server automatically using context manager command 'with'"""
        self.disconnect_server()
