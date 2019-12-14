Parts Implemented by Ahmet Semih Uçan
=====================================

In this project, I created 3 classes to send and receive data as object. My fundamental classes' name are People, Berber and Owner.
In these classes, I write constructors to assign initial values to the object. These classes' codes are below.


.. code-block:: python

   class People:
    def __init__(self):
        self.id = None
        self.username = None
        self.name_surname = None
        self.mail = None
        self.password_hash = None
        self.gender = None
        self.age = None
        self.role = None
        self.active = True

    def get_id(self):
        return self.username

    @property
    def is_active(self):
        return self.active


.. code-block:: python

    class Berber:
        def __init__(self):
            self.id = None
            self.people_id = None
            self.berber_shop_id = None
            self.gender_choice = None
            self.experience_year = None
            self.start_time = None
            self.finish_time = None
            self.rates = None
            self.people = None #will be used for reaching berber's people attributes for berbershop_view page


.. code-block:: python

    class Owner:
        def __init__(self):
            self.id = None
            self.people_id = None
            self.tc_number = None
            self.serial_number = None
            self.vol_number = None
            self.family_order_no = None
            self.order_no = None

The following initialize function in dbinit.py was running when the site was opened. This function was running to create tables with SQL codes that I kept in the variable INIT_STATEMENT in the database.


.. code-block:: python

    def initialize(url):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            for statement in INIT_STATEMENTS:
                cursor.execute(statement)
            cursor.close()

INIT_STATEMENT is below.

.. code-block:: python

    INIT_STATEMENTS = [
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
        """
    ]