from SortFunctions import quick_sort
import random
import csv


def main():

    movies_by_genre = []
    with open('movies.csv', encoding='utf-8', newline = '\n') as csvfile:
        movie_reader = csv.reader(csvfile, delimiter=',')
        for row in (movie_reader):
            movies_by_genre.append((row[2].split('|')[0], row[1]))

    choice = input("Should I sort the movies? (y/n)")
    print('\n')
    if choice == 'y':
        quick_sort(movies_by_genre, 0, int(len(movies_by_genre)/2))

        genre = input('What genre of movie would you like to watch?')
        print('\n')
        movies_in_category = []
        for movie in movies_by_genre:
            if movie[0] == genre:
               movies_in_category.append(movie[1])

        index = input(f'Give me a random Index between 0 and {len(movies_in_category)}: ')
        print('\n')
        index = int(index)
        if index > len(movies_in_category):
            index = 3
        
        if index < -1 * (len(movies_in_category)):
            index = 3

        num_movies = input('And how many recommendations would you like?')
        print('\n')
        num_movies = int(num_movies)

        a = num_movies//2
        if num_movies % 2 == 0:
            recs = movies_in_category[index - a : index + a]
            for mov in recs:
                print(mov)

        else:
            recs = movies_in_category[index - (a + 1) : index + a]
            for mov in recs:
                print(mov)   

       
    else:
        print(movies_by_genre)
      
   
if __name__ == "__main__":
    main()