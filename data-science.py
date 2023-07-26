from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://unicorn_user:magical_password@localhost:5432/rainbow_database')
df = pd.read_sql_query('select * from "anime"',con=engine)
