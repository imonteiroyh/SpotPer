-- Gravadora
INSERT INTO record_label(code, name, address, homepage_address)
VALUES 
    (1, 'Ultra', 'Londres, Inglaterra', 'https://www.ultra.com/'),
    (2, 'Sony', 'São Paulo, São Paulo', 'https://www.sonymusic.com.br'),
    (3, 'Spinnin', 'Berlim, Alemanha', 'https://www.spinnin.com'),
	(4, 'Estúdio 100', 'R. Cel. Ferraz - Centro, Fortaleza - CE', NULL),
	(5, 'Pro Áudio', 'R. Mariana Pinto Bandeira, Fortaleza - CE', 'https://www.proaudio.com.br'),
    (6, 'Sucesso', 'Av. Novo Horizonte, 488, Caucaia - CE', NULL),
    (7, 'Produções', 'Av. Novo Horizonte, 488, Caucaia - CE', NULL),
    (8, 'Gravadora Barroca', 'Rua da Alegria - França', NULL),
    (9, 'MK Music', 'R. Cel. Ferraz - Centro, Fortaleza - CE', 'https://www.mkmusic.com.br');

-- Telefones da gravadora 
INSERT INTO record_label_phones(phone, record_label_code)
VALUES	
	('1111-1111', 1),
	('1111-1112', 1),
	('1111-1113', 2),
	('1111-1114', 3),
	('1111-1115', 4),
	('1111-1116', 4),
	('1111-1117', 5),
	('1111-1118', 6),
	('1111-1119', 7),
	('1111-1110', 8),
	('1111-1121', 9);

-- Album 
INSERT INTO album (code, media_number, description, record_label_code, record_date, purchase_date, purchase_price, purchase_type, physical_media)
VALUES
    (1, 1, 'Favorite Hits', 3, FORMAT(CONVERT(DATETIME, '2000-12-01', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2008-02-02', 120), 'dd-MM-yyyy'), 30.50, 'Pessoal', 'cd'),
    (2, 1, 'Christmas', 2, FORMAT(CONVERT(DATETIME, '2000-12-15', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2008-02-04', 120), 'dd-MM-yyyy'), 45.50, 'Pessoal', 'vinyl'),
    (2, 2, 'Christmas side B', 2, FORMAT(CONVERT(DATETIME, '2000-12-15', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2008-02-04', 120), 'dd-MM-yyyy'), 45.50, 'Pessoal', 'vinyl'),
    (3, 1, 'GUTS', 2, FORMAT(CONVERT(DATETIME, '2023-12-09', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2023-10-04', 120), 'dd-MM-yyyy'), 50.00, 'Presente', 'cd'),
    (4, 1, 'Happier than ever', 1, FORMAT(CONVERT(DATETIME, '2021-10-15', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2023-11-02', 120), 'dd-MM-yyyy'), 75.75, 'Presente', 'download'),
    (5, 1, 'Confetti', 4, FORMAT(CONVERT(DATETIME, '2022-10-15', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2023-11-10', 120), 'dd-MM-yyyy'), 60.43, 'Pessoal', 'cd'),
    (5, 2, 'Confetti DELUXE', 4, FORMAT(CONVERT(DATETIME, '2022-10-15', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2023-11-10', 120), 'dd-MM-yyyy'), 60.43, 'Pessoal', 'cd'),
    (6, 1, 'Melhores Hits do Verão', 5, FORMAT(CONVERT(DATETIME, '2021-10-16', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2022-12-10', 120), 'dd-MM-yyyy'), 60.00, 'Pessoal', 'cd'),
    (7, 1, '21', 6, FORMAT(CONVERT(DATETIME, '2019-10-16', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2023-12-10', 120), 'dd-MM-yyyy'), 75.00, 'Presente', 'vinyl'),
    (8, 1, 'Four', 5, FORMAT(CONVERT(DATETIME, '2015-12-16', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2020-12-08', 120), 'dd-MM-yyyy'), 80.99, 'Pessoal', 'download'),
    (9, 1, 'Midnight Memories', 7, FORMAT(CONVERT(DATETIME, '2014-12-10', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2022-12-18', 120), 'dd-MM-yyyy'), 35.67, 'Presente', 'cd'),
    (9, 2, 'Midnight Memories for fans', 7, FORMAT(CONVERT(DATETIME, '2014-12-10', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2022-12-18', 120), 'dd-MM-yyyy'), 35.67, 'Presente', 'cd'),
    (10, 1, 'Lover', 8, FORMAT(CONVERT(DATETIME, '2019-12-11', 120), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '2023-11-18', 120), 'dd-MM-yyyy'), 45.45, 'Pessoal', 'cd');

-- Período Musical 
INSERT INTO musical_period(code, description, active_start, active_end)
VALUES
	(1, 'Idade Média', '1300', '1400'),
	(2, 'Renascença', '1400', '1500'),
	(3, 'Barroco', '1600', '1700'),
	(4, 'Clássico', '1700', '1800'),
	(5, 'Romântico', '1800', '1900'),
	(6, 'Moderno', '1900', '2000');

-- Compositor
INSERT INTO songwriter(code, name, birth_city, birth_country, birth_date, death_date, musical_period_code)
VALUES
    (1, 'Jack Antonoff', 'Washington DC', 'USA', FORMAT(CONVERT(DATETIME, '23-12-1992', 105), 'dd-MM-yyyy'), NULL, 6),
    (2, 'Adele', 'London', 'England', FORMAT(CONVERT(DATETIME, '01-03-2000', 105), 'dd-MM-yyyy'), NULL, 6),
    (3, 'Michael Buble', 'New York', 'New York', FORMAT(CONVERT(DATETIME, '30-03-1983', 105), 'dd-MM-yyyy'), NULL, 5),
    (4, 'Johann Sebastian Bach', NULL, 'Italia', FORMAT(CONVERT(DATETIME, '01-01-1910', 105), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '20-10-1950', 105), 'dd-MM-yyyy'), 3),
	(5, 'Georg Friedrich Händel', 'Halle', 'Alemanha', FORMAT(CONVERT(DATETIME, '03-05-1800', 105), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '12-03-1859', 105), 'dd-MM-yyyy'), 3),
    (6, 'Jean-Philippe Rameau', 'Nice', 'França', FORMAT(CONVERT(DATETIME, '15-07-1800', 105), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '28-02-1864', 105), 'dd-MM-yyyy'), 4),
    (7, 'Antonio Vivaldi', 'Sicilia', 'Itália', FORMAT(CONVERT(DATETIME, '12-01-1800', 105), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '28-10-1841', 105), 'dd-MM-yyyy'), 2),
    (8, 'Harry Styles', 'Redditch', 'Reino Unido', FORMAT(CONVERT(DATETIME, '01-02-1994', 105), 'dd-MM-yyyy'), NULL, 5),
    (9, 'Finneas', 'San Francisco', 'California', FORMAT(CONVERT(DATETIME, '01-07-1996', 105), 'dd-MM-yyyy'), NULL, 6),
    (10, 'Ludwig von Beethoven', 'Bonn', 'Alemanha', FORMAT(CONVERT(DATETIME, '12-12-1770', 105), 'dd-MM-yyyy'), FORMAT(CONVERT(DATETIME, '26-03-1827', 105), 'dd-MM-yyyy'), 3);

-- Tipo de Composição 
INSERT INTO composition_type(code,description)
VALUES
	(1, 'Sinfonia'),
	(2, 'Ópera'),
	(3, 'Sonata'),
	(4, 'Concerto');

-- Intérprete
INSERT INTO interpreter(code, name, type)
VALUES
	(1, 'Billie Eilish', 'Soprano'),
	(2, 'Maneskin', 'Quarteto'),
	(3, 'Little Mix', 'Trio'),
	(4, 'Olivia Rodrigo', 'Soprano'),
	(5, 'Mariah Carey', 'Ensemble'),
	(6, 'Michael Bublé', 'Tenor'),
	(7, 'ExaltaSamba', 'Ensemble'),
	(8, 'One Direction', 'Quarteto'), 
	(9, 'Taylor Swift', 'Tenor'),
	(10, 'Linkin Park', 'Soprano');

-- Faixas 
INSERT INTO track(album_code, album_media_number, number, description, composition_type_code, execution_time, recording_type)
VALUES 
	(1, 1, 1, 'favorite 1', 1, 3, 'DDD'),
	(1, 1, 2, 'favorite 2', 2, 3, 'DDD'),
	(2, 1, 1, 'its beginning to look a lot like christmas', 1, 4, null),
	(2, 2, 1, 'all i want for christmas is you', 2, 3, null),
	(3, 1, 1, 'all american bitch', 3, 2, 'ADD'),
	(3, 1, 2, 'bad idea right?', 2, 2, 'ADD'),
	(3, 1, 3, 'vampire', 3, 2, 'ADD'),
	(4, 1, 1, 'I didnt change my number', 3, 2, null),
	(4, 1, 3, 'billie bossa nova', 3, 3, null),
	(5, 1, 1, 'sweet melody', 4, 2, 'DDD'),
	(5, 1, 2, 'for the fans', 1, 4, 'DDD'),
	(5, 2, 1, 'hair (remastered)', 2, 3, 'ADD'),
	(7, 1, 1, 'mundo ideal', 4, 4, null),
	(7, 1, 3, 'rolling in the deep', 2, 5, null),
	(7, 1, 2, 'skyfall', 1, 4, null),
	(8, 1, 1, 'steal my girl', 4, 4, null),
	(8, 1, 5, 'girl almighty', 2, 5, null),
	(9, 1, 1, 'best song ever', 1, 4, 'ADD'),
	(9, 1, 3, 'midnight memories', 1, 3, 'ADD'),
	(9, 2, 18, 'half a heart', 2, 4, 'DDD'),
	(10, 1, 1, 'i forgot that you existed', 4, 3, 'ADD'),
	(10, 1, 2, 'lover', 2, 4, 'ADD'),
	(10, 1, 3, 'daylight', 3, 3, 'DDD');

-- Faixa - Intérprete
INSERT INTO track_interpreter(album_code,album_media_number,track_number,interpreter_code)
VALUES
	(1, 1, 1, 2),
	(1, 1, 2, 2),
	(2, 1, 1, 6),
	(2, 2, 1, 5),
	(3, 1, 1, 4),
	(3, 1, 2, 4),
	(3, 1, 3, 4),
	(4, 1, 1, 1),
	(4, 1, 3, 1),
	(5, 1, 1, 3),
	(5, 1, 2, 3),
	(5, 1, 2, 3),
	(7, 1, 2, 10),
	(7, 1, 3, 10),
	(8, 1, 1, 8),
	(8, 1, 5, 10),
	(9, 1, 3, 10),
	(9, 1, 1, 10),
	(9, 2, 18, 10),
	(10, 1, 1, 9),
	(10, 1, 2, 9),
	(10, 1, 3, 9);

-- Faixa - Compositor
INSERT INTO track_songwriter(album_code, album_media_number, track_number, songwriter_code)
VALUES
	(1, 1, 1, 4),
	(1, 1, 2, 6),
	(2, 1, 1, 3),
	(2, 2, 1, 10),
	(3, 1, 1, 1),
	(3, 1, 2, 2),
	(3, 1, 3, 6),
	(4, 1, 1, 9),
	(4, 1, 3, 9),
	(5, 1, 1, 8),
	(5, 1, 2, 1),
	(5, 1, 2, 4),
	(7, 1, 1, 10),
	(7, 1, 2, 2),
	(7, 1, 3, 2),
	(8, 1, 1, 8),
	(8, 1, 5, 8),
	(9, 1, 3, 7),
	(9, 1, 1, 3),
	(9, 2, 18, 8),
	(10, 1, 1, 1),
	(10, 1, 2, 1),
	(10, 1, 3, 10);

-- Playlist 
INSERT INTO playlist(code, name, creation_date) 
VALUES
	--(1, 'playlist_1', '11-11-2011'),
	--(2, 'playlist_2', '10-01-2012'),
	--(3, 'playlist_rock', '19-01-2019'),
	--(4, 'playlist_internacional', '30-08-2017'),
	--(5, 'playlist_test', '30-08-2018'),
	--(6, 'playlist_diferentes', '30-09-2021')

	(1, 1, '11-11-2011'),
	(2, 2, '10-01-2012'),
	(3, 3, '19-01-2019'),
	(4, 4, '30-08-2017'),
	(5, 5, '30-08-2018'),
	(6, 6, '30-09-2021'),
	(20, 'essa passa no 7d', '05-11-2023')

-- Faixa - Playlist
INSERT INTO track_playlist(album_code, album_media_number, track_number, playlist_code, last_played, times_played)
VALUES
	(1, 1, 1, 1, '30-09-2021', 2),
	(2, 1, 1, 1, '30-09-2021', 2),
	(3, 1, 1, 1, '30-10-2021', 1),
	(2, 2, 1, 1, '30-10-2021', 1),
	(3, 1, 2, 1, '30-08-2022', 2),
	(4, 1, 1, 1, '30-09-2022', 3),
    (5, 1, 1, 2, '30-09-2022', 3),
	(7, 1, 1, 20, '05-11-2023', 7)