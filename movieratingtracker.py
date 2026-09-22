print("============================================")
print("           MOVIE RATING TRACKER        ")
print("============================================")

movies = ["Avatar", "Frozen", "Inception"]
ratings = [8.2, 7.5, 3.0]
movie_database = {
    movie: rating
    for movie, rating in zip(movies, ratings)
}

top_movies = [
    movie
    for movie, rating in movie_database.items()
    if rating > 8
]
uppercase_movies = list(map(str.upper, movies))
while True:
    print("\n-----MENU-----")
    print("1. View Movie Database")
    print("2. View Top Rated Movies")
    print("3. View Movie names in uppercase")
    print("4. Exit")

    choice = int(input("Enter your Choice :"))

    if choice == 1:
        print("Movie Database:")
        print(movie_database)
    elif choice == 2:
        print("Top Rated Moviess :")
        print(top_movies)

    elif choice == 3:
        print("movie names in uppercase:")
        print(uppercase_movies)

    elif choice == 4:
        print("\n Thank you for using Movie rating Tracker")
        exit()

    else:
        print("invalid choice. enter a number from 1 to 4 ")
        
