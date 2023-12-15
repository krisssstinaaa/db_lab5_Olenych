import psycopg2 
import matplotlib.pyplot as plt
import csv
import pandas as pd

params = {
    'user': 'postgres',
    'password': '7256',
    'database': 'labs',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**params)
cur = conn.cursor()

csv_file = 'lb4\lb5\\top500mangaMAL.csv'

def add_id(input_file, output_file):

    df = pd.read_csv(input_file, on_bad_lines = 'skip')
    status_id_map = {}
    current_id = 1

    for status in df['Status'].unique():
        status_id_map[status] = current_id
        current_id += 1

    df['status_id'] = df['Status'].map(status_id_map)

    genre_id_map = {}
    current_id = 1

    for genre in df['Genres'].unique():
        genre_id_map[genre] = current_id
        current_id += 1

    df['genre_id'] = df['Genres'].map(genre_id_map)

    df['manga_id'] = df['Manga ID']
    df['manga_url'] = df['Manga URL']
    df['english_title'] = df['English Title']
    df['synonim_title'] = df['Synonims Titles']
    df.to_csv(output_file, index=False)

add_id(csv_file, 'manga_i.csv')

query_del_s = 'DELETE FROM status'
query_del_g = 'DELETE FROM genre'
query_del_m = 'DELETE FROM manga'
query_del_mg = 'DELETE FROM manga_genre'

query_status = 'INSERT INTO status (status_id, status) VALUES (%s, %s)'
query_genre = 'INSERT INTO genre (genre_id, genre) VALUES (%s, %s);'
query_manga = 'INSERT INTO manga (manga_id, manga_url, english_title, synonim_title, chapters, status_id) VALUES (%s, %s, %s, %s, %s, %s);'
query_mg = 'INSERT INTO manga_genre (manga_id, genre_id) VALUES (%s, %s) '

queries = (query_status, query_genre, query_manga, query_mg)

with open('manga_i.csv', 'r') as file:

    cur.execute(query_del_mg)
    cur.execute(query_del_g)
    cur.execute(query_del_m)   
    cur.execute(query_del_s)  
    reader = csv.DictReader(file)

    status, genre = [], []
    for idx, row in enumerate(reader):
        if idx < 5:
            if row['status_id'] not in status:
                values = (row['status_id'], row['Status']) 
                cur.execute(query_status, values)
                status.append(row['status_id'])

                
            if row['genre_id'] not in genre:
                values = (row['genre_id'], row['Genres']) 
                cur.execute(query_genre, values)
                genre.append(row['genre_id'])

            values = (row['manga_id'], row['manga_url'], row['english_title'], row['synonim_title'], row['Chapters'], row['status_id']) 
            cur.execute(query_manga, values)

            values = (row['manga_id'], row['genre_id']) 
            cur.execute(query_mg, values) 
        else:
            break

    conn.commit()