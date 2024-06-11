# Vervebridge-Book-Recommendation-System
# Book Recommender System
https://vervebridge-book-recommendation-system-1.onrender.com

## Overview
The Book Recommender System (https://vervebridge-book-recommendation-system-1.onrender.com) is a web application that allows users to input a book title and receive a list of recommended books based on cosine similarity of combined textual features. The system is built using Flask for the backend and leverages machine learning for generating recommendations.

## System Architecture
The system follows a client-server architecture with the following major components:
- **User Interface**: A web interface for entering book titles and displaying recommendations.
- **Backend Server**: A Flask application that handles user requests and interacts with the recommendation engine.
- **Recommendation Engine**: A module that preprocesses data, trains the machine learning model, and provides book recommendations.
- **Data Storage**: Stores book data and pre-trained model files.

## Technology Stack
- **Frontend**: HTML, CSS (for styling)
- **Backend**: Python (Flask framework)
- **Machine Learning**: Scikit-learn (for cosine similarity), Pandas (for data handling)
- **Storage**: CSV (for book data), Joblib (for model storage)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/book-recommender-system.git
    cd book-recommender-system
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the dataset and model:**
    - Ensure `books.csv` is in the project directory.
    - Ensure `model.pkl` (the pre-trained model) is in the project directory.

## Project Structure

book-recommender-system/ <br>
├── templates/<br>
│   └── index.html<br>
├── static/<br>
│   └── style.css<br>
├── app.py<br>
├── preprocess.py<br>
├── recommend.py<br>
├── train_model.py<br>
├── books.csv<br>
├── model.pkl<br>
├── requirements.txt<br>
├── logging_config.py<br>
├── app.log<br>
└── README.md<br>


## Execution

### 1. Train the Model
If you need to retrain the model or preprocess the data, run the `model.py` script:
```bash
python model.py
```
This script will preprocess the data, train the model, and save the cosine similarity matrix to model.pkl.

### 2. Run the Flask Application
Start the Flask server by running the following command:

``` bash 

python app.py
```
The application will be available at http://127.0.0.1:5000/.

### 3. Use the Application
Open a web browser and navigate to http://127.0.0.1:5000/.
Enter a book title in the input form and click "Get Recommendations".
The system will display a list of recommended books along with the response time.
 ### Measuring Response Time
The application measures and displays the response time for generating recommendations. This is useful for performance analysis and optimization.

### Contributing
Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Create a new Pull Request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**: Credits the libraries and frameworks used in the project.
