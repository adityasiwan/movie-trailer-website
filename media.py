import webbrowser


class Movie:
    def __init__(self, title, movie_poster, movie_trailer):
        self.title = title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
