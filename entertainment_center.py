import media
import fresh_tomatoes


def show_movies():

    jungle_book = media.Movie("Jungle Book",
                              "http://cdn.collider.com/wp-content/uploads/2015/08/jungle-book-poster-hi-res.jpeg",  
                              "https://youtu.be/5mkm22yO-bs")  
    minions = media.Movie("Minions",
                         "http://i2.wp.com/bitcast-a-sm.bitgravity.com/slashfilm/wp/wp-content/images/Minions-poster1.jpg",  
                         "https://youtu.be/P9-FCC6I7u0")  

    finding_dory = media.Movie("Finding Dory",
                               "http://www.everythingpixar.com/uploads/3/8/2/4/38249737/9213755_orig.jpg",  
                               "https://www.youtube.com/watch?v=NQu-153MnGQ")  

    zootopia = media.Movie("Zootopia",
                           "http://cdn.collider.com/wp-content/uploads/2015/12/zootopia-movie-poster.jpg",  
                           "https://www.youtube.com/watch?v=WWFB-zrxn7o")  

    frozen = media.Movie("Frozen",
                         "https://walter.trakt.us/images/movies/000/077/349/posters/original/9d1a3cdcf2.jpg",  
                         "https://www.youtube.com/watch?v=R-cdIvgBCWY")  

    lion_king = media.Movie("The Lion King",
                            "http://mpspg.com/images/lion-king-movie-cover-i11.jpg",  
                            "https://www.youtube.com/watch?v=GaJWzJfoXlE")  

    movies = [jungle_book, minions,finding_dory, zootopia, frozen, lion_king]
    fresh_tomatoes.open_movies_page(movies)
    return

show_movies()
