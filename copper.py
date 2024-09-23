import pandas as pd
from decorator import db_conn


def read_and_clean_copper_data():
    df = pd.read_csv('copper1.csv')
    df_final = df.dropna()

    # Convert df ti list of dict to save in sql
    df_final = df_final.to_dict(orient='records')
    return df_final

# To store data in sql


@db_conn
def store_copper_data(cursor, data):
    for row in data:
        query = "INSERT INTO copper_data (prd_id,prd_name,prd_price,prd_qty,prd_weight) VALUES (%s,%s,%s,%s,%s)"
        values = (row['prd_id'],
                  row['prd_name'],
                  row['prd_price'],
                  row['prd_qty'],
                  row['prd_weight'],)
        cursor.execute(query,values)
        print("Copper Data Inserted Successfully in SQL")

def process_copper():
    data = read_and_clean_copper_data()
    store_copper_data(data)

