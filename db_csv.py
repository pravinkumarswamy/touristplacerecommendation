import pandas as pd
from sqlalchemy import create_engine

# read CSV file
column_names = ['title','ratings', 'distance','category','index','location','image_url']

df = pd.read_csv('C:/Users/Pravin Swamy/Favorites/Desktop/final_year_project/tourist_pura_1000.csv', header = 0)
print(df)

engine = create_engine('mysql://root:@localhost/touristplaces')

with engine.connect() as conn, conn.begin():
    df.to_sql('places', conn, if_exists='append', index=False)

