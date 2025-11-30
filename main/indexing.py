from pymongo import MongoClient


client = MongoClient("mongodb+srv://Apratim:AapraUchiha@datacluster.gv3cli6.mongodb.net/?appName=datacluster")

# Use your database name — MongoDB creates it automatically if it doesn’t exist
db = client["mm_database"]

db.top_10s.create_index(
    [("username",1),("movies.id",1)],
    unique=True,
    sparse=True,
)

