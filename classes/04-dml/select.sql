--2
--Название и продолжительность самого длительного трека.
SELECT title название , duration продолжительность
FROM tracks
ORDER BY duration DESC
LIMIT 1;

--Название треков, продолжительность которых не менее 3,5 минут.
SELECT title название , duration продолжительность
FROM tracks
WHERE duration >=210;

--Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT title название , release_year год_выпуска
FROM compilations
WHERE  release_year  BETWEEN 2018 AND 2020;

--Исполнители, чьё имя состоит из одного слова.
SELECT name AS исполнитель
FROM artists
WHERE name NOT LIKE '% %';


--Название треков, которые содержат слово «мой» или «my».
  --С применением ILIKE
SELECT title AS название_трека
FROM tracks
WHERE title ILIKE 'my %'    -- слово в начале
   OR title ILIKE '% my %'  -- слово в середине
   OR title ILIKE '% my'    -- слово в конце
   OR title ILIKE 'my'      -- только слово
   OR title ILIKE 'мой %'   -- слово в начале (рус)
   OR title ILIKE '% мой %' -- слово в середине (рус)
   OR title ILIKE '% мой'   -- слово в конце (рус)
   OR title ILIKE 'мой';    -- только слово (рус)

  --с использованием string_to_array и массивов
SELECT title AS название_трека
FROM tracks
WHERE string_to_array(lower(title), ' ') && ARRAY['my', 'мой'];

  --с регулярными выражениями
SELECT title AS название_трека
FROM tracks
WHERE title ~* '\y(my|мой)\y';

--3
--Количество исполнителей в каждом жанре.
SELECT g.name AS жанр, COUNT(DISTINCT ag.artist_id) AS количество_исполнителей
FROM genres g
LEFT JOIN artist_genres ag ON g.genre_id = ag.genre_id
GROUP BY g.name
ORDER BY количество_исполнителей DESC;

--Количество треков, вошедших в альбомы 2019-2020 годов.
SELECT COUNT(t.track_id) AS количество_треков
FROM tracks t
JOIN albums a ON t.album_id = a.album_id
WHERE a.release_year BETWEEN 2019 AND 2020;

--Средняя продолжительность треков по каждому альбому.
SELECT a.title AS альбом, AVG(t.duration) AS средняя_длительность
FROM tracks t
JOIN albums a ON t.album_id = a.album_id
GROUP BY a.title;

--Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT ar.name AS исполнитель
FROM artists ar
LEFT JOIN album_artists aa ON ar.artist_id = aa.artist_id
LEFT JOIN albums a ON aa.album_id = a.album_id
WHERE a.release_year != 2020
GROUP BY ar.name;

--Названия сборников, в которых присутствует конкретный исполнитель (ТОКИО)
SELECT DISTINCT c.title AS сборник
FROM compilations c
JOIN compilation_tracks ct ON c.compilation_id = ct.compilation_id
JOIN tracks t ON ct.track_id = t.track_id
JOIN albums a ON t.album_id = a.album_id
JOIN album_artists aa ON a.album_id = aa.album_id
JOIN artists ar ON aa.artist_id = ar.artist_id
WHERE ar.name = 'ТОКИО';


--4
--Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT DISTINCT a.title AS альбом
FROM albums a
JOIN album_artists aa ON a.album_id = aa.album_id
JOIN artists ar ON aa.artist_id = ar.artist_id
WHERE ar.artist_id IN (
    SELECT artist_id
    FROM artist_genres
    GROUP BY artist_id
    HAVING COUNT(genre_id) > 1
);

--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек
SELECT ar.name AS исполнитель, title AS название, duration AS продолжительность
FROM artists ar
JOIN album_artists aa ON ar.artist_id = aa.artist_id
JOIN tracks t ON aa.album_id = t.album_id
WHERE t.duration = (SELECT MIN(duration) FROM tracks);

--Названия альбомов, содержащих наименьшее количество треков
SELECT a.title AS альбом, COUNT(t.track_id) AS количество_треков
FROM albums a
JOIN tracks t ON a.album_id = t.album_id
GROUP BY a.album_id, a.title
HAVING COUNT(t.track_id) = (
    SELECT COUNT(track_id)
    FROM tracks
    GROUP BY album_id
    ORDER BY 1
    LIMIT 1
);