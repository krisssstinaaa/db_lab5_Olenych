import psycopg2
import json

params = {
    'user': 'postgres',
    'password': '1111',
    'database': 'labs',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**params)
cur = conn.cursor()


def save_all_tables_to_json(database_connection):
    cursor = database_connection.cursor()
    table_names = ['manga', 'status', 'genre', 'manga_genre']

    data_dict = {}

    for table_name in table_names:
        cursor.execute(f"SELECT * FROM {table_name}")
        table_data = cursor.fetchall()
        all_data = []

        columns = [column[0] for column in cursor.description]
        for row in table_data:
            all_data.append(dict(zip(columns, row)))

        data_dict[table_name] = all_data

    cursor.close()
    database_connection.close()

    with open('output.json', 'w') as json_file:
        json.dump(data_dict, json_file)

save_all_tables_to_json(conn)