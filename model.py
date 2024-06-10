import pandas as pd
import joblib 

# # Load your CSV data
# df = pd.read_csv('books.csv')

# # Display the first few rows to verify the data
# print(df.head())

#!pip install --upgrade astrapy

from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("AstraCS:THPHfGlAfYkSrRdBBLJOOAWE:7d4f9929a8333acda2525be9b904f339065f8a7d8b62ea65e4b4ba1b85ffee93")
db = client.get_database_by_api_endpoint(
  "https://eef27c48-d40e-4643-9629-6c0ac4131b86-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")

# Data is already loded in the database
collection_name = "books"

# Load and Explore the Dataset:

cursor = db.get_collection("books").find()

import pandas as pd
df = pd.DataFrame(list(cursor))

print("Dataset Information:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst Few Rows of the Dataset:")
print(df.head())


# Perform exploratory data analysis

# Display basic statistics of numerical features
print("Summary Statistics:")
print(df.describe())

# Display the number of unique values in each column
print("\nNumber of Unique Values:")
print(df.nunique())



# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)


def preprocess_data(df):
    # Fill missing values
    df.fillna('', inplace=True)

    # Combine text features
    df['combined_features'] = df['Title'] + ' ' + df['Author'] + ' ' + df['Genre'] + ' ' + df['Publisher']

    return df
df = preprocess_data(df)

df.head()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Build the recommendation model
def build_model(df):
    # Vectorize the combined text features
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_features'])

    # Compute the cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    return cosine_sim

cosine_sim = build_model(df)

joblib.dump(cosine_sim, 'model.pkl')

# Function to get book recommendations
def get_recommendations(title, df, cosine_sim):
    # Get the index of the book that matches the title
    idx = df[df['Title'] == title].index[0]

    # Get the pairwise similarity scores of all books with that book
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the books based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar books
    sim_scores = sim_scores[1:11]

    # Get the book indices
    book_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar books
    return df['Title'].iloc[book_indices]

# Test the recommendation system
username = input("Enter book:")
print(get_recommendations(username, df, cosine_sim))



