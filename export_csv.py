import psycopg2
import csv
import pandas as pd

params = {
    'user': 'postgres',
    'password': '1111',
    'database': 'labs',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**params)

table_names = ['manga', 'status', 'genre', 'manga_genre']

def save_tables_to_csv(conn, tables):
    for table in tables:
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + table)
            column_names = [x[0] for x in cur.description]
            output = pd.DataFrame(columns = column_names)
            rows = cur.fetchall()  
            output = pd.DataFrame(rows, columns=column_names)
    

            output.to_csv(f'{table}.csv', index=False)


save_tables_to_csv(conn, table_names)