from flask_sqlalchemy import SQLAlchemy

# Create a DB object

DB = SQLAlchemy()

# Create a table with a specific schmea
# we will do that creating a python class

class User(DB.Model):
    #Two columns inside of our user table
    #ID Column Schema
    id = DB.Column(DB.BigInteger)
    # username Column schema