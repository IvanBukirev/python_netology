CREATE TABLE  IF NOT EXISTS genres(
    genre_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS artists (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    bio TEXT
);

CREATE TABLE IF NOT EXISTS artist_genres (
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id) ON DELETE CASCADE,
    genre_id INTEGER NOT NULL REFERENCES genres(genre_id) ON DELETE CASCADE,
    PRIMARY KEY (artist_id, genre_id)
);


CREATE TABLE IF NOT EXISTS albums (
    album_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    release_year INTEGER NOT NULL,
    cover_url VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS  album_artists (
    album_id INTEGER NOT NULL REFERENCES albums(album_id) ON DELETE CASCADE,
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id) ON DELETE CASCADE,
    PRIMARY KEY (album_id, artist_id)

);

CREATE TABLE IF NOT EXISTS tracks (
    track_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    duration INTEGER NOT NULL, -- в секундах
    album_id INTEGER NOT NULL REFERENCES albums(album_id) ON DELETE CASCADE,
    track_number INTEGER
);

CREATE TABLE compilations (
    compilation_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    release_year INTEGER NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS compilation_tracks (
    compilation_id INTEGER NOT NULL REFERENCES compilations(compilation_id) ON DELETE CASCADE,
    track_id INTEGER NOT NULL REFERENCES tracks(track_id) ON DELETE CASCADE,
    PRIMARY KEY (compilation_id, track_id)
);



