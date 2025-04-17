-- Вставляем жанры
INSERT INTO genres (name) VALUES
('Инди-рок'), ('Лоу-фай'), ('Альтернативный рэп'), ('Этно-электроника'), ('Пост-панк');

-- Вставляем исполнителей
INSERT INTO artists (name, bio) VALUES
('Перемотка', 'Московская инди-рок группа с меланхоличным звучанием'),
('Луна', 'Санкт-Петербургский лоу-фай проект'),
('ТОКИО', 'Экспериментальный рэп из Екатеринбурга'),
('Увула', 'Этно-электронный дуэт из Казани'),
('Порядок слов', 'Пост-панк группа из Новосибирска'),
('Марсианские Будни', 'Арт-рок коллектив из Архангельска');

-- Связываем исполнителей с жанрами
INSERT INTO artist_genres (artist_id, genre_id) VALUES
(1, 1), -- Перемотка - Инди-рок
(2, 2), -- Луна - Лоу-фай
(3, 3), -- ТОКИО - Альтернативный рэп
(4, 4), -- Увула - Этно-электроника
(5, 5), -- Порядок слов - Пост-панк
(6, 1), -- Марсианские Будни - Инди-рок
(6, 4); -- Марсианские Будни - Этно-электроника

-- Вставляем альбомы
INSERT INTO albums (title, release_year, cover_url) VALUES
('Снег в апреле', 2018, 'https://example.com/peremotka_snow.jpg'),
('Фаза луны', 2020, 'https://example.com/luna_phase.jpg'),
('Отель "Токио"', 2019, 'https://example.com/tokyo_hotel.jpg'),
('Зов предков', 2021, 'https://example.com/uvula_call.jpg'),
('Тихие дома', 2017, 'https://example.com/words_order.jpg'),
('Северный ветер', 2022, 'https://example.com/mars_days.jpg');

-- Связываем альбомы с исполнителями
INSERT INTO album_artists (album_id, artist_id) VALUES
(1, 1), -- Снег в апреле - Перемотка
(2, 2), -- Фаза луны - Луна
(3, 3), -- Отель "Токио" - ТОКИО
(4, 4), -- Зов предков - Увула
(5, 5), -- Тихие дома - Порядок слов
(6, 6), -- Северный ветер - Марсианские Будни
(4, 6); -- Зов предков - Марсианские Будни (коллаборация)

-- Вставляем треки
INSERT INTO tracks (title, duration, album_id, track_number) VALUES
-- Перемотка - Снег в апреле
('Снег в апреле', 203, 1, 1),
('Окна', 187, 1, 2),
-- Луна - Фаза луны
('Море в стакане', 156, 2, 1),
('Фаза луны', 198, 2, 2),
-- ТОКИО - Отель "Токио"
('Лифт на крышу', 213, 3, 1),
('Отель "Токио"', 231, 3, 2),
-- Увула - Зов предков
('Зов предков', 245, 4, 1),
('Танец огня', 192, 4, 2),
-- Порядок слов - Тихие дома
('Тихие дома', 207, 5, 1),
('Город спит', 223, 5, 2),
-- Марсианские Будни - Северный ветер
('Северный ветер', 198, 6, 1),
('Белые ночи', 214, 6, 2);

-- Вставляем сборники
INSERT INTO compilations (title, release_year, description) VALUES
('Андеграунд 2018', 2019, 'Лучшее из русского андеграунда 2018 года'),
('Экспериментальный звук', 2020, 'Современные экспериментальные проекты'),
('Новая волна', 2021, 'Молодые перспективные исполнители'),
('Этно-микс', 2022, 'Современная этническая музыка'),
('Инди-сцена', 2023, 'Актуальная инди-музыка России');

-- Связываем сборники с треками
INSERT INTO compilation_tracks (compilation_id, track_id) VALUES
-- Андеграунд 2018
(1, 1), -- Снег в апреле
(1, 9), -- Тихие дома
-- Экспериментальный звук
(2, 5), -- Лифт на крышу
(2, 7), -- Зов предков
-- Новая волна
(3, 3), -- Море в стакане
(3, 11), -- Северный ветер
-- Этно-микс
(4, 7), -- Зов предков
(4, 8), -- Танец огня
-- Инди-сцена
(5, 1), -- Снег в апреле
(5, 2), -- Окна
(5, 11); -- Северный ветер


-- Добавляем треки с словами "мой" или "my"
UPDATE tracks SET title = 'Мой город' WHERE track_id = 2;  -- Окна → Мой город (Перемотка)
UPDATE tracks SET title = 'My Darkest Night' WHERE track_id = 6;  -- Отель "Токио" → My Darkest Night (ТОКИО)
INSERT INTO tracks (title, duration, album_id, track_number) VALUES
('Твой мой дым', 215, 3, 3);  -- Новый трек для ТОКИО

-- Добавляем данные для обеспечения непустого результата
INSERT INTO artist_genres (artist_id, genre_id) VALUES
(6, 3); -- Добавляем Марсианским Будням ещё один жанр (Альтернативный рэп)


-- Добавляем трек без сборника
INSERT INTO tracks (title, duration, album_id, track_number) VALUES
('Одинокий трек', 180, 1, 4);

-- Добавляем очень короткий трек
INSERT INTO tracks (title, duration, album_id, track_number) VALUES
('Мини-трек', 30, 2, 5);


-- Добавляем альбом с 1 треком
INSERT INTO albums (title, release_year, cover_url) VALUES
('Сольный проект', 2023, 'https://example.com/solo.jpg');
INSERT INTO tracks (title, duration, album_id, track_number) VALUES
('Единственный трек', 210, 7, 1);



