# Environment Setup

    $ conda create -n condavenv
    
The environment locatoin will show up in the output, I'd recommend keeping that around

    $ source activate condavenv
    $ conda install openssl psycopg2 flask flask-wtf
    $ python3 -m pip install flask-migrate flask_script
    
 # Table Setup
 ## create a table
 - open up `once_upon_a_prject/config.py`
 - scroll to the bottom of the file and on a new line write `create_table('examples')`. `examples` is what I want my table named.
 
    $ source activate condavenv
    $ python3 once_upon_a_project/config.py
    
- go back to `once_upon_a_prject/config.py` and delete the `create_table('examples')` you added.

the process for deleting a table is pretty similar, just be extra careful when using that one. You delete all your table's data.


# Run app
    $ source activate condavenv
    $ flask run

# Older instructions
## sqlalchemy attempt
- find hackernoon's flask-web-programming-from-scratch article
- when you get to `$ pythonapp.py db init` try this instead

  - edit app.py's  app.config[''SQLALCHEMY_DATABASE_URI] property so the value looks like mine. 
  - then run:
     
      $ source activate condavenv
      $ python3 src/app.py db init
      $ python3 src/app.py db migrate
      $ python3 src/app.py db upgrade
