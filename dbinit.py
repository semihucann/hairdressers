import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [

    #ERTUGRUL's tables
    #ALTER TABLE Comments
    #ADD COLUMN keywords varchar(100);
    """
    
    CREATE TABLE IF NOT EXISTS Comments(
        id SERIAL PRIMARY KEY, 
        people_id integer NOT NULL REFERENCES People(id) ON DELETE CASCADE,
        berber integer  REFERENCES Berber(id) ON DELETE CASCADE,
        berbershop integer  REFERENCES Berbershop(id) ON DELETE CASCADE,
        title VARCHAR (100),
        content VARCHAR (500),
        rate integer  NOT NULL,
        date_time TIMESTAMP, 
        comment_like integer DEFAULT 0 NOT NULL, 
        comment_dislike  integer DEFAULT 0 NOT NULL,
        CHECK (rate > 0), CHECK (rate < 6) 
    )""",
    #  CREATE TYPE IF NOT EXISTS type AS ENUM ('company', 'personal');
    """
    
    CREATE TABLE IF NOT EXISTS Contact_info(
        id SERIAL PRIMARY KEY, 
        berbershop_id integer  REFERENCES Berbershop(id) ON DELETE CASCADE,
        type type,
        telephone_number VARCHAR (15) NOT NULL,
        facebook VARCHAR (500),
        twitter VARCHAR (500),
        instagram VARCHAR (500)
    )""",
    # CREATE TYPE status AS ENUM ('okey','notokey');
    #Create type method as enum ('creditcard','cash');
    """
      
      
       CREATE TABLE IF NOT EXISTS Rezervation(
           id SERIAL PRIMARY KEY,
           people_id integer NOT NULL REFERENCES People(id) ON DELETE CASCADE,
           berbershop_id integer NOT NULL REFERENCES Berbershop(id) ON DELETE CASCADE,
           datetime_registration TIMESTAMP,
           datetime_rezervation TIMESTAMP,
           status status,
           note VARCHAR (100),
           price_type integer REFERENCES ServicePrices(id) ON DELETE CASCADE,
           payment_method method
       )""",

    """ 
         
       CREATE TABLE IF NOT EXISTS CommentLikeDislike(
           id SERIAL PRIMARY KEY,
           comment_id integer NOT NULL REFERENCES Comments(id) ON DELETE CASCADE,
           people_id integer NOT NULL REFERENCES People(id) ON DELETE CASCADE,
           ifliked  integer NOT NULL,
           ifdisliked integer NOT NULL,
           CHECK (ifliked <2), CHECK (ifliked >-2), CHECK (ifdisliked <2), CHECK (ifdisliked >-2) 
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
        gender VARCHAR(10),
        age integer,
        role VARCHAR(10)    
    )""",
    """
    CREATE TABLE IF NOT EXISTS Berber(
        id SERIAL PRIMARY KEY,
        people_id INTEGER REFERENCES People(id) ON DELETE CASCADE,
        berbershop_id INTEGER DEFAULT NULL REFERENCES Berbershop(id) ON DELETE SET NULL,
        gender_choice VARCHAR(10),
        experience_year INTEGER DEFAULT 0,
        start_time INTEGER,
        finish_time INTEGER,
        rates INTEGER DEFAULT 0 
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Owner(
        id SERIAL PRIMARY KEY,
        people_id INTEGER REFERENCES People(id) ON DELETE CASCADE,
        tc_number NUMERIC(11) UNIQUE NOT NULL,
        serial_number NUMERIC(5) NOT NULL,
        vol_number NUMERIC(5),
        family_order_no NUMERIC(5),
        order_no NUMERIC(5)
    )   
    """,

    #"""DROP TABLE People, Berber, Owner;""",
    #################################################################################

    #FATIH'S TABLES
    """
    CREATE TABLE IF NOT EXISTS Berbershop(
        id SERIAL PRIMARY KEY,
        owner_people_id INTEGER REFERENCES People(id) ON DELETE CASCADE,
        shopname VARCHAR(50),
        location VARCHAR(300),
        city VARCHAR(50),
        opening_time TIME,
        closing_time TIME,
        trade_number NUMERIC(10) NOT NULL,
        shop_logo bytea 
    )   
    """,
    # blob data type for postgresql is bytea
    """
    CREATE TABLE IF NOT EXISTS Serviceprices(
        id SERIAL PRIMARY KEY,
        shop_id INTEGER REFERENCES Berbershop(id) ON DELETE CASCADE,
        service_name VARCHAR(50),
        definition VARCHAR(300),
        gender VARCHAR(10),
        price DECIMAL(6,2),
        duration INTEGER
    )   
    """,
    """
    CREATE TABLE IF NOT EXISTS Creditcards(
        id SERIAL PRIMARY KEY,
        people_id INTEGER REFERENCES People(id) ON DELETE CASCADE,
        name VARCHAR(50),
        card_number NUMERIC(16) NOT NULL,
        cvv_number NUMERIC(4) NOT NULL,
        last_month NUMERIC(2) NOT NULL,
        last_year NUMERIC(2) NOT NULL
    )   
    """,
    #FATIH'S TABLES
    
    #HALIS'S TABLES
    """
    CREATE TABLE IF NOT EXISTS Posts(
        id SERIAL PRIMARY KEY,
        people_id INTEGER REFERENCES People(id) ON DELETE CASCADE,
        post_title VARCHAR(50),
        post_content VARCHAR(500),
        like_number INTEGER,
        dislike_number INTEGER,
        subject VARCHAR(20),
        date_time TIMESTAMP
    )
    """

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
