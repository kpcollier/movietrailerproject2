import fresh_tomatoes
import media

#Info on movies (title, storyline, poster, trailer.)
#Instance variable refrence
rocky_2 = media.Movie("Rocky 2",
                      "Rocky Balboa fights Apollo Creed in a rematch",
                      "http://bit.ly/2stfFtY",
                      "https://www.youtube.com/watch?v=6PSSxAGSiCY")

dark_knight = media.Movie("The Dark Knight",
                          "The Joker is Batman's new rival.",
                          "http://bit.ly/1MOw97w",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

despicable_me = media.Movie("Despicable Me",
                            "A crook and his minions try to steal the moon.",
                            "http://bit.ly/2tqZIsQ",
                            "https://www.youtube.com/watch?v=sUkZFetWYY0")

breakfast_club = media.Movie("The Breakfast Club",
                             "Five students reflect on their differences.",
                             "http://bit.ly/2twbO4r",
                             "https://www.youtube.com/watch?v=ZXzlCpHK3-I")

the_warriors = media.Movie("The Warriors",
                           "A New York street gang fights to stay alive.",
                           "http://bit.ly/2upQ3PS",
                           "https://www.youtube.com/watch?v=4GxSwUcm_XE")

gladiator = media.Movie("Gladiator",
                        "A man's will to get revenge after being betrayed.",
                        "http://bit.ly/2tqMzjp",
                        "https://www.youtube.com/watch?v=owK1qxDselE")
                                                      
movies = [rocky_2, dark_knight, despicable_me, breakfast_club, the_warriors, gladiator]
fresh_tomatoes.open_movies_page(movies)


