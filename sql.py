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
        self.engine.execute("""ALTER TABLE `sql`.`user_credentials` 
CHANGE COLUMN `index` `index` INT NOT NULL ,
CHANGE COLUMN `user_id` `user_id` INT NOT NULL ;
""")
        return user_credentials

    def run_query(self, query):
        self.engine.execute(query)

obj = SQL('mysql+pymysql://root:12345678@localhost/sql')

obj.read_sql()


print(obj.get_duplicates())

query2 = """ALTER TABLE `sql`.`user_credentials` 
ADD CONSTRAINT `fk`
  FOREIGN KEY (`user_id`)
  REFERENCES `sql`.`user_details` (`user_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;"""


obj.run_query(query2)

