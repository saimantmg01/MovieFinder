from movie_finder import MovieFinder

if __name__ == "__main__":
    # Create an instance of MovieRecommender
    recommender = MovieFinder()
    
    while True:

        print("*" * 15, "\n")
        # Get user input and find similar movies
            # eg: "A boy learns he is a wizard and attends a magical school."
        user_input = input("Type the description of movie: \n")
        number_of_similar_movie = input("Type the number of similar movie: ") 

        number = int(number_of_similar_movie)


        # edge case tests 
        # results = recommender.find_similar_movies(user_input, 100000000)
        # results = recommender.find_similar_movies(user_input)
        
        results = recommender.find_similar_movies(user_input, number)
      
        print("\n")

        # Display the results
        recommender.display_results(results)

        print("*" * 15, "\n")