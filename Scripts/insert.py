import psycopg2
from psycopg2 import sql
from faker import Faker
import random

# PostgreSQL connection details
PG_PORT = "5432"                  # Default PostgreSQL port
PG_DB = "postgres"                 # Connect to the default "postgres" database first
PG_USER = "postgres"               # PostgreSQL user
PG_PASSWORD = "4iSt33nTVC"        # PostgreSQL password
PG_HOST = "10.110.125.146"

# Establish connection to PostgreSQL database (connect to 'postgres' database first)
conn = psycopg2.connect(
    port=PG_PORT,
    database=PG_DB,
    user=PG_USER,
    host=PG_HOST,
    password=PG_PASSWORD
)

# Create a cursor
cursor = conn.cursor()

# Check if the database exists, and create it if necessary
cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s;", (PG_DB,))
exists = cursor.fetchone()
if not exists:
    print(f"Database {PG_DB} does not exist. Creating it now.")
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("movies_db")))
    conn.commit()

# Now connect to the newly created or existing 'movies_db' database
conn.close()

# Reconnect to the 'movies_db' database
conn = psycopg2.connect(
    port=PG_PORT,
    database="movies_db",  # Connect to 'movies_db'
    user=PG_USER,
    host=PG_HOST,
    password=PG_PASSWORD
)

cursor = conn.cursor()

# Create the 'actors' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS actors (
        actor_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        birthdate DATE
    );
""")

# Create the 'movies' table with a foreign key to 'actors'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        movie_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        genre VARCHAR(50),
        release_year INT,
        actor_id INT,
        FOREIGN KEY (actor_id)
            REFERENCES actors (actor_id)
            ON DELETE SET NULL
    );
""")

# Commit the changes to the database
conn.commit()

# Initialize Faker to generate random data
faker = Faker()

# Function to generate and insert random actors
def generate_actors(num_records):
    print(f"Inserting {num_records} actors...")
    for _ in range(num_records):
        name = faker.name()
        birthdate = faker.date_of_birth(minimum_age=18, maximum_age=100).isoformat()
        cursor.execute(
            "INSERT INTO actors (name, birthdate) VALUES (%s, %s);",
            (name, birthdate)
        )
    conn.commit()

# Function to generate and insert random movies
def generate_movies(num_records):
    print(f"Inserting {num_records} movies...")
    for _ in range(num_records):
        title = faker.sentence(nb_words=3)
        genre = random.choice(["Action", "Drama", "Comedy", "Romance", "Thriller", "Sci-Fi", "Horror"])
        release_year = random.randint(1900, 2023)
        actor_id = random.randint(1, 100000)  # Assuming there are at least 100,000 actors
        cursor.execute(
            "INSERT INTO movies (title, genre, release_year, actor_id) VALUES (%s, %s, %s, %s);",
            (title, genre, release_year, actor_id)
        )
    conn.commit()

# Number of records to insert into each table
NUM_ACTORS = 100000
NUM_MOVIES = 100000

# Generate and insert data
generate_actors(NUM_ACTORS)
generate_movies(NUM_MOVIES)

# Close the cursor and connection
cursor.close()
conn.close()

print(f"{NUM_ACTORS} actors and {NUM_MOVIES} movies have been successfully inserted into the database.")