from configparser import ConfigParser
import psycopg2


def config(filename='once_upon_a_project/database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def return_database_connection():
    # Read connection parameters.
    params = config()

    # Connect to the PostgreSQL server.
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)

    # Create a cursor.
    cur = conn.cursor()
    return conn, cur


def fetchall_examples(cur):
    cur.execute("SELECT * FROM examples")
    rows = cur.fetchall()
    return rows


def add_example(conn, cur, title, text):
    command = """INSERT INTO examples VALUES(%s, %s)"""
    cur.execute(command, (title, text))
    conn.commit()


def execute_one_time_command(command):
    conn, cur = return_database_connection()
    cur.execute(command)
    conn.commit()


def drop_table(table_name):
    """
    Only run this during initial project setup. Whether that means on your local machine is tbd.

    Function usage example: drop_table('examples')
    Call function: $ python3 once_upon_a_project/config.py
    """
    command = 'DROP TABLE public.{}'.format(table_name)
    execute_one_time_command(command)


def create_table(table_name):
    """
    Only run this during initial project setup. Whether that means on your local machine is tbd.
    Function usage example: create_table('examples')
    Call function: $ python3 once_upon_a_project/config.py

    """
    command = 'CREATE TABLE public.{} ();'.format(table_name)
    execute_one_time_command(command)


def alter_table(table_name, column_name_and_definition):
    """
    Function usage example: alter_table('examples', 'ADD COLUMN row_0 VARCHAR')
    Call function: $ python3 once_upon_a_project/config.py
    See latest version of https://www.postgresql.org/docs/9.2/sql-altertable.html for more info.
    """
    command = 'ALTER TABLE public.{} {};'.format(table_name, column_name_and_definition)
    execute_one_time_command(command)
