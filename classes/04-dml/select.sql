
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
SELECT title AS название_трека
FROM tracks
WHERE title LIKE '%мой%' OR title LIKE '%Мой%' OR title LIKE '%my%' OR title LIKE '%My%';


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