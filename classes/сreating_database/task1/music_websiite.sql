CREATE TABLE IF NOT EXISTS genre (
	genre_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS artist (
	artist_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
	album_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	release_year INT NOT NULL
);

CREATE TABLE IF NOT EXISTS song (
	song_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	duration INT NOT NULL,
	album_id INT REFERENCES album(album_id) NOT NULL
);

CREATE TABLE IF NOT EXISTS collection (
	collection_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	year_release INT NOT NULL
);

CREATE TABLE IF NOT EXISTS artist_genre (
	artist_id INT REFERENCES artist(artist_id),
	genre_id INT REFERENCES genre(genre_id),
	CONSTRAINT pk_artist_genre PRIMARY KEY (artist_id, genre_id)
);

CREATE TABLE IF NOT EXISTS artist_album (
	artist_id INT REFERENCES artist(artist_id),
	album_id INT REFERENCES album(album_id),
	CONSTRAINT pk_artist_album PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS track_collection (
	track_id INT REFERENCES track(track_id),
	collection_id INT REFERENCES collection(collection_id),
	CONSTRAINT pk_song_collection PRIMARY KEY (song_id, collection_id)
);