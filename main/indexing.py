from main.db import db

# Uses the same client/connection string as the rest of the app (MONGO_URI in .env).
# MongoDB creates the database/collection automatically if it doesn't exist yet.

db.top_10s.create_index(
    [("username", 1), ("movies.id", 1)],
    unique=True,
    sparse=True,
)

