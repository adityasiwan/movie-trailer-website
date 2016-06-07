import webbrowser


class Movie:
    # the class Movie provides a way tos tore movie data
    def __init__(self, title, movie_poster, movie_trailer):
        self.title = title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
