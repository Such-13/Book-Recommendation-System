from flask import Flask, request, render_template
import pandas as pd
import joblib

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model
cosine_sim = joblib.load('model.pkl')

# Load the dataset
df = pd.read_csv('books.csv')

# Preprocess data
def preprocess_data(df):
    df.fillna('', inplace=True)
    df['combined_features'] = df['Title'] + ' ' + df['Author'] + ' ' + df['Genre'] + ' ' + df['Publisher']
    return df

df = preprocess_data(df)

# Recommendation function
def get_recommendations(title, df, cosine_sim):
    if title not in df['Title'].values:
        return ["Book not found"]
    
    idx = df[df['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Skip the first item as it is the same book
    
    valid_indices = [i[0] for i in sim_scores if i[0] < len(df)]
    
    return df['Title'].iloc[valid_indices].tolist()
    # Collect unique book indices
    unique_book_indices = []
    seen_titles = set()
    for i, score in sim_scores:
        if len(unique_book_indices) == 10:
            break
        book_title = df['Title'].iloc[i]
        if book_title != title and book_title not in seen_titles:
            unique_book_indices.append(i)
            seen_titles.add(book_title)

    # Return the top 10 most similar book titles as a list
    return df['Title'].iloc[unique_book_indices].tolist()

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        title = request.form['title']
        recommendations = get_recommendations(title, df, cosine_sim)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)