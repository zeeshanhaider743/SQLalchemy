import sqlalchemy
import pandas as pd
from sqlalchemy import  create_engine
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean
from datetime import datetime

class SQL:
    def __init__(self,address):
        self.address = address
        self.engine = create_engine(self.address)
        self.connection = self.engine.connect()

    def read_sql(self):
        self.x = pd.DataFrame(pd.read_sql("SELECT * FROM user_details Limit 10000",self.engine))
        return self.x

    def get_duplicates(self):
        y = self.x
        z = y.copy()
        user_credentials = pd.concat([y,z], ignore_index=True)
        user_credentials.to_sql('user_credentials', con=self.engine)
        return user_credentials

    def add_key(self, query):
        self.engine.execute(query)
obj = SQL('mysql+pymysql://root:12345678@localhost/sql')

obj.read_sql()

d = obj.get_duplicates()
#print(d)

query2 = """ALTER TABLE user_credentials
ADD FOREIGN KEY (index) REFERENCES user_details(user_id);"""

query1 = """ALTER TABLE user_credentials
ADD PRIMARY KEY (index);"""

obj.add_key(query1)
obj.add_key(query2)