import sqlalchemy
import pandas as pd
from sqlalchemy import  create_engine
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean
from datetime import datetime

class SQL:
    def run_engine(self, address):
        self.engine = create_engine(address)
        return self.engine

    def connect_engine(self):
        self.connection = self.engine.connect()

    def read_sql(self):
        x = pd.read_sql("SELECT * FROM user_details Limit 10",self.engine)
        return x

    def 

