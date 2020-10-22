from configparser import ConfigParser
import psycopg2


def config(filename='once_upon_a_project/database.ini', section='postgresql'):
  parser = ConfigParser()
  parser.read(filename)
  db = {}
  if parser.has_section(section):
    params = parser.items(section)
    for param in params:
      db[param[0]] = param[1]
  else:
    raise Exception('Section {0} not found in the {1} file'.format(section, filename))
  return db
  
 
def return_database_connection():
  params = config()
  print('Connecting to the PostgreSQL database...')
  conn = psycopg2.connect(**params) 
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
  

def drop_table():
"""*Careful with this one."""
  command = (
  """
  DROP TABLE public.exmaples
  """
  )
  execute_one_time_command(command)
  

def create_table():
  command = (
  """
  CREATE TABLE public.examples (
    example_title VARCHAR(255) NOT NULL,
    example_text VARCHAR NOT NULL
  )
  """
  )
  execute_one_time_command(command)

  
