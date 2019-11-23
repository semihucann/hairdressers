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


]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = "postgres://lltjryrurbhacv:4ed89e50a1718d204c9ac3cee26560e3874bf47bd7ce47e12f0c4f81611954f6@ec2-107-22-236-52.compute-1.amazonaws.com:5432/d2lpnjbrjgerqm"
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
