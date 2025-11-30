# MovieMatch

MovieMatch is a web application that allows users to log in, create a list of their top 10 favorite movies, and discover their personality traits based on their movie preferences. The platform also provides a matching system that suggests other users with similar tastes, with a match_score indicating compatibility.

Built for movie lovers who want to connect with like-minded people and explore their cinematic personalities!


# Features

- User Authentication
- Users can create and manage their personalized top 10 movies
- Analyze users’ movie preferences to infer personality traits or nature
- Discover other users with similar tastes in movies/genres, ranked by match_score
- Interactive Dashboard to V=view your movie list, matches, and personality insights

# Tech_Stack

- Python 3
- Django
- HTML
- CSS
- Bulma
- MongoDB
- The Movie Database (TMDb) API

# Setup_instructions

1. **Clone the repository**

    ```bash
    git clone https://github.com/Apratimmm/movie_match.git
    cd moviematching
    
2. **Create and activate a virtual environment**

    ```bash
    python -m venv virenv
    source virenv/bin/activate

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    
4. **Create your .env file**

    Create a .env file in the root folder and add your credentials:
    ```bash
    - MONGO_URI=your_mongodb_URI
    - API_Read_Access_Token=your_TMDB_read_access_token

5. **Run the server**

    ```bash
    python manage.py runserver
