INSERT INTO Genre (genre_id, genre)
VALUES
(1, 'Action'),
(2, 'Adventure'),
(3, 'Drama'),
(4, 'Comedy'),
(5, 'Mystery'),
(6, 'Fantasy');

INSERT INTO Status (status_id, status)
VALUES
(1, 'Publishing'),
(2, 'Finished');

INSERT INTO Manga (manga_id, manga_url, english_title, synonim_title, chapters, status_id)
VALUES
(1, 'https://myanimelist.net/manga/2/Berserk', 'Berserk', 'Berserk: The Prototype', 242, 1),
(2, 'https://myanimelist.net/manga/1706/JoJo_no_Kimyou_na_Bouken_Part_7__Steel_Ball_Run', 'Jojo', 'JoJos Bizarre Adventure Part 7: Steel Ball Run, SBR', 96, 2),
(3, 'https://myanimelist.net/manga/25/Fullmetal_Alchemist', 'Fullmetal Alchemist', 'Full Metal Alchemist, Hagane no Renkinjutsushi, FMA, HagaRen, Fullmetal Alchemist Gaiden', 116, 2),
(4, 'https://myanimelist.net/manga/13/One_Piece', 'One Piece', 'One Piece', 1052, 1),
(5, 'https://myanimelist.net/manga/1/Monster', 'Monster', 'Monster', 162, 2);

INSERT INTO manga_genre (manga_id, genre_id)
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 6),
(2, 1),
(2, 2),
(2, 5),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(4, 1),
(4, 2),
(4, 4),
(4, 6),
(5, 5),
(5, 3);

