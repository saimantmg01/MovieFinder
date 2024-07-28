import streamlit as st

from movie_finder import MovieFinder

# recommender = MovieFinder()

# text = st.text_area("Type the description of movie: \n")

# if text:
#     result = recommender.find_similar_movies(text)
#     for movie, percentage in result:
#         # print(f"The most similar movie with percent similarity of {percentage:.2f} is:\n{ movie}\n ")
#         st.write(movie)
#         st.write(percentage)
#     # st.write(1234)


# in order to run type: 
#   streamlit run app.py

# Initialize the MovieFinder
recommender = MovieFinder()

# Streamlit UI
st.title("Movie Recommendation System")

# Text area for user to input movie description
user_input = st.text_area('Type the description of movie:')

# Input for number of similar movies
number_of_similar_movie = st.number_input('Type the number of similar movies:', min_value=1, step=1)

# Button to trigger the recommendation
if st.button('Find Similar Movies'):
    if user_input and number_of_similar_movie:
        number = int(number_of_similar_movie)

        # Find similar movies
        results = recommender.find_similar_movies(user_input, number)

# Display the results
    st.write("Similar Movies:")
    for movie, percentage in results:
#         # print(f"The most similar movie with percent similarity of {percentage:.2f} is:\n{ movie}\n ")
        st.write(movie)
        st.write(percentage)