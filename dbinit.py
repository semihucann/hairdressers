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
    #SEMİH TABLE ######################################################################
    #"CREATE TYPE IF NOT EXISTS GENDER_TYPE AS ENUM ('male', 'female', 'unisex'); ",
    #"CREATE TYPE IF NOT EXISTS ROLE AS ENUM ('berber','owner','user', 'admin' ); ",
    #One char is used
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
    INSERT INTO People(username,name_surname,mail,password_hash,gender,age,role) VALUES('firstuser','first user','first@user.com', '1a2b','m',22,'u');
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
    url=os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
