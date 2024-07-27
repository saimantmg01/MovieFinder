from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class MovieFinder:

    def __init__(self, model_name='all-MiniLM-L6-v2', dataset_path="./dataset/imdb-movies-dataset.csv"):
        # Initialize the model and dataset
        
        # Load the pre-trained model from hugging face
            #helps with description comparison
        self.model = SentenceTransformer(model_name)
        self.dataset_path = dataset_path

        #load the dataset using pandas
        self.df = pd.read_csv(self.dataset_path)
        #replaces empty description field with empty string values
        self.df["Description"] = self.df["Description"].fillna("")
        #create embeddings from user descriptions to compare against user inputted description  
        self.embeddings = self._encode_descriptions()

    def _encode_descriptions(self):
        # Encode movie descriptions into embeddings
        return self.model.encode(self.df["Description"])

    def find_similar_movies(self, user_input, num_similar_movie = 3):
         # check if number of similar movie inputted is within range of dataset
        if num_similar_movie > len(self.df):
            print(f"Requested number of similar movies exceeds the number of available movies.")
            return []
        
        # Create embedding from the user input
        user_embedding = self.model.encode([user_input])
        
        # Calculate similarity between user description and movie descriptions
        similarities = cosine_similarity(user_embedding, self.embeddings)
        
        #flattened the similarity array into 1d array
        flattened_similarities = similarities.flatten()

        # Flatten the similarity array and get top 3 indices
        top_indices = self.get_top_indices(flattened_similarities, num_similar_movie)
        
        # Prepare results with movie and corresponding percentages
        result = []
        for idx in top_indices:
            similarity_percentage = similarities[0][idx]
            movie = self.df.iloc[idx]
            result.append([movie, similarity_percentage])
        return result

    def get_top_indices(self, array, num_similar_movie):
        # Get the indices of the top number of specified movies
        top_indices = np.argpartition(array, -num_similar_movie)[-num_similar_movie:]
        top_indices = top_indices[np.argsort(-array[top_indices])]
        return top_indices

    def display_results(self, results):
        if len(results) < 1:
            print("No similar movie found")
        # Print the similar movies and their similarity percentages
        for movie, percentage in results:
            print(f"The most similar movie with percent similarity of {percentage:.2f} is:\n{ movie}\n ")


    
