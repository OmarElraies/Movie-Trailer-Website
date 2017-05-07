import media
import fresh_tomatoes


# The Godfather movie object
the_godfather = media.Movie(
    "The Godfather",
    "The aging patriarch of an organized crime dynasty transfers control +\
            of his clandestine empire to his reluctant son.",
    "http://fontmeme.com/images/The-Godfather-Poster.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA")

# Interstellar movie object
interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to\
            ensure humanity's survival.",
    "http://imgc.allpostersimages.com/images/P-473-488-90/87/8706/YGFN300Z/\
            posters/interstellar.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

# The Pursuit of Happyness movie object
the_pursuit_of_happyness = media.Movie(
    "The Pursuit of Happyness ",
    "A struggling salesman takes custody of his son as he's poised to \
    begin a life-changing professional endeavor.",
    "http://www.impawards.com/2006/posters/pursuit_of_happyness.jpg",
    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

# The Departed movie object
the_departed = media.Movie(
    "The Departed",
    "An undercover cop and a mole in the police attempt to identify each \
            other while infiltrating an Irish gang in South Boston",
    "http://www.impawards.com/2006/posters/departed_ver9.jpg",
    "https://www.youtube.com/watch?v=auYbpnEwBBg")

# Avatar movie object
avatar = media.Movie(
    "Avatar",
    "Avatar (marketed as James Cameron's Avatar) is a 2009 American",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Toy Story movie object
toy_story = media.Movie(
    "Toy Story",
    "Toy Story is a 1995 American computer-animated buddy comedy",
    "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# CreateING a list of these movie objects
movies = [the_godfather, interstellar, the_pursuit_of_happyness, the_departed,
          avatar, toy_story]

# Passing movies input in order to build the HTML file
fresh_tomatoes.open_movies_page(movies)
