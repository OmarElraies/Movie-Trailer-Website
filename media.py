class Movie(object):
    """A movie which contains alot of info that users interested in it

    Attributes:
            movie_title: the title of the movie.
            movie_storyLine: a short breif for the movie.
            poster_image: the url of poter of the movie.
            trailer_youtube: the url youtube link  trailer of the movie.

    """

    def __init__(self, movie_title, movie_storyLine,
                 poster_image, trailer_youtube):
        """Return a new Movie object."""
        self.title = movie_title
        self.storyLine = movie_storyLine
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
