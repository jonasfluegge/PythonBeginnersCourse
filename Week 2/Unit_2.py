star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

trilogy_input = int(input("Trilogy: "))
number_film_input = int(input("Number of film: "))
movie = ""

if trilogy_input == 1:
    if number_film_input == 1:
        movie = star_wars_movies[0][0]
    if number_film_input == 2:
        movie = star_wars_movies[0][1]
    if number_film_input == 3:
        movie = star_wars_movies[0][2]
elif trilogy_input == 2:
    if number_film_input == 1:
        movie = star_wars_movies[1][0]
    if number_film_input == 2:
        movie = star_wars_movies[1][1]
    if number_film_input == 3:
        movie = star_wars_movies[1][2]
elif trilogy_input == 3:
    if number_film_input == 1:
        movie = star_wars_movies[2][0]
    if number_film_input == 2:
        movie = star_wars_movies[2][1]
    if number_film_input == 3:
        movie = star_wars_movies[2][2]
else:
    exit()

    print(movie)
