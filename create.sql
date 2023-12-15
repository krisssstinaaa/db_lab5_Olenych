CREATE TABLE Genre
(
  genre_id INT NOT NULL,
  genre CHAR(20) NOT NULL,
  PRIMARY KEY (genre_id)
);

CREATE TABLE Status
(
  status_id INT NOT NULL,
  status CHAR(20) NOT NULL,
  PRIMARY KEY (status_id)
);

CREATE TABLE Manga
(
  manga_id INT NOT NULL,
  manga_url CHAR(200) NOT NULL,
  english_title CHAR(40) NOT NULL,
  synonim_title CHAR(100) NOT NULL,
  chapters INT NOT NULL,
  status_id INT NOT NULL,
  PRIMARY KEY (manga_id),
  FOREIGN KEY (status_id) REFERENCES Status(status_id)
);

CREATE TABLE Manga_genre
(
  manga_id INT NOT NULL,
  genre_id INT NOT NULL,
  PRIMARY KEY (manga_id, genre_id),
  FOREIGN KEY (manga_id) REFERENCES Manga(manga_id),
  FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);