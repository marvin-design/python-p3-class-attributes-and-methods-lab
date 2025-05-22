class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Track total number of Song instances
        Song.count += 1

        # Track genres
        Song.genres.append(genre)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        # Track artists
        Song.artists.append(artist)
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
