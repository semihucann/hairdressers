import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    "CREATE TABLE IF NOT EXISTS DUMMY (NUM INTEGER)",
    "INSERT INTO DUMMY VALUES (42)",

    """
    CREATE TABLE IF NOT EXISTS Comments(
        id SERIAL PRIMARY KEY, 
        people_id integer,
        berber integer,
        comment_title VARCHAR (100),
        comment_content VARCHAR (500),
        rate integer NOT NULL,
        date_time TIMESTAMP, 
        comment_like integer NOT NULL, 
        comment_dislike integer NOT NULL 
    )""",
    #  CREATE TYPE IF NOT EXISTS type AS ENUM ('company', 'personal');
    """
  
    CREATE TABLE IF NOT EXISTS Contact_info(
        id SERIAL PRIMARY KEY, 
        berber_id integer,
        berbershop_id integer,
        type type,
        telephone_number VARCHAR (12),
        facebook VARCHAR (500),
        twitter VARCHAR (500),
        instagram VARCHAR (500)
    )""",

    """
    
       CREATE TABLE IF NOT EXISTS Rezervation(
           id SERIAL PRIMARY KEY,
           people_id integer, 
           berber_id integer,
           datetime_registration TIMESTAMP,
           datetime_rezervation TIMESTAMP,
           status VARCHAR (100),
           note VARCHAR (100),
           price_type VARCHAR (100)
       )""",

    # SEMİH TABLE ######################################################################
    # "CREATE TYPE IF NOT EXISTS GENDER_TYPE AS ENUM ('male', 'female', 'unisex'); ",
    # "CREATE TYPE IF NOT EXISTS ROLE AS ENUM ('berber','owner','user', 'admin' ); ",
    # One char is used
    """
    CREATE TABLE IF NOT EXISTS People(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        name_surname VARCHAR(50),
        mail VARCHAR(300) UNIQUE,
        password_hash VARCHAR(300),
        gender VARCHAR(1),
        age integer,
        role VARCHAR(1)    
    )""",
    """
    CREATE TABLE IF NOT EXISTS Berber(
        id SERIAL PRIMARY KEY,
        people_id INTEGER REFERENCES People(id),
        berbershop_id INTEGER DEFAULT 0, 
        gender_choice VARCHAR(1),
        experience_year INTEGER,
        start_time INTEGER,
        finish_time INTEGER,
        rates INTEGER DEFAULT 0 
    )
    """
    #################################################################################
]

def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
