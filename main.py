import psycopg2 
import matplotlib.pyplot as plt

params = {
    'user': 'postgres',
    'password': '7256',
    'database': 'labs',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**params)
cur = conn.cursor()

create_manga_genre_view = """
    CREATE OR REPLACE VIEW manga_genre_view AS
    SELECT g.genre, COUNT(mg.manga_id) AS manga_count
    FROM genre g
    JOIN manga_genre mg ON g.genre_id = mg.genre_id
    GROUP BY g.genre;
"""
cur.execute(create_manga_genre_view)


create_manga_status_view = """
    CREATE OR REPLACE VIEW manga_status_view AS
    SELECT s.status, COUNT(m.manga_id) AS manga_count
    FROM status s
    JOIN manga m ON s.status_id = m.status_id
    GROUP BY s.status;
"""
cur.execute(create_manga_status_view)


create_chapters_status_view = """
    CREATE OR REPLACE VIEW chapters_status_view AS
    SELECT s.status, AVG(m.chapters) AS avg_chapters
    FROM manga m
    JOIN status s ON m.status_id = s.status_id
    GROUP BY s.status;
"""
cur.execute(create_chapters_status_view)
cur.close()

query_manga_genre = "select * from manga_genre_view;"
query_manga_status = "select * from manga_status_view;"
query_chapters_status = "select * from chapters_status_view;"

with conn:
    cur = conn.cursor()

    cur.execute(query_manga_genre)
    manga_genre = cur.fetchall()

    cur.execute(query_manga_status)
    manga_status = cur.fetchall()

    cur.execute(query_chapters_status)
    chapters_status = cur.fetchall()


    labels_a, values_a = zip(*manga_genre)
    labels_b, values_b = zip(*manga_status)
    labels_c, values_c = zip(*chapters_status)


    fig, ax = plt.subplots(1, 3, figsize = (15, 5))
    ax[0].bar(labels_a, values_a, color = 'green')
    ax[0].set_title('Кількість манги для кожного жанру')
    ax[0].set_xlabel('Жанр')
    ax[0].set_ylabel('Кількість')

    ax[1].pie(values_b, labels=labels_b)
    ax[1].set_title('Кількість манги за кожним статусом')

    ax[2].bar(labels_c, values_c, color = 'red')
    ax[2].set_xlabel('Статус')
    ax[2].set_ylabel('Кількість розділів')
    ax[2].set_title('Залежність кількості розділів від завершеності манги')

    plt.tight_layout()
    plt.show()