Parts Implemented by Ahmet Semih Uçan
=====================================

In this project, I created 3 classes to send and receive data as object. My fundamental classes' name are People, Berber and Owner.
In these classes, I write constructors to assign initial values to the object. These classes' codes are below.

Classes
-------

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

INIT_STATEMENT
--------------

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


In this project, I have written and used sql codes for each table separately, such as deleting updates. I have created 3 different classes named x_model for each table. I wrote the queries I used in the table in these classes. I have completed the necessary actions by calling the functions I prepared in views.py.

People Model
------------

Here are some examples of functions that I use in the model

.. code-block:: python

    class Peoplemodel:

        # Insert Function
         def insert(self, people):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("""INSERT INTO People (username, name_surname, mail, password_hash, gender, age,role)
                               VALUES (%s , %s , %s , %s , %s , %s,  %s )""", (
                people.username, people.name_surname, people.mail, people.password_hash, people.gender, people.age,
                people.role))

        # Read Function
        def get_all_list(self):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute(""" SELECT * from people""")
                people_list = []
                rows = cursor.fetchall()
                for i in rows:
                    person = People()
                    person.id = i[0]
                    person.username = i[1]
                    person.name_surname = i[2]
                    person.mail = i[3]
                    person.password_hash = i[4]
                    person.gender = i[5]
                    person.age = i[6]
                    person.role = i[7]
                    person.active = True
                    people_list.append(person)
                return people_list

        # Delete Id
        def delete_id(self, id):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM People where id = %s", (id,))

        # Delete Update
        def update(self, people):
            if self.control_exist_to_update(people) == False:
                with dbapi2.connect(url) as connection:
                    cursor = connection.cursor()
                    cursor.execute("""UPDATE People SET username = %s, name_surname = %s, mail = %s, password_hash = %s, gender = %s, age = %s where id = %s""",
                                   (people.username, people.name_surname, people.mail, people.password_hash, people.gender, people.age, people.id))
                return True
            else:
                return False

Berber Model
------------

.. code-block:: python

    class Berbermodel:

        # Read function
        def get_id(self, username):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                                SELECT id FROM PEOPLE WHERE username = %s
                                """, (username, ))
            row = cursor.fetchone()
            return row

        # Insert function
        def insert(self, berber):
                with dbapi2.connect(url) as connection:
                    cursor = connection.cursor()
                    cursor.execute("""INSERT INTO Berber (people_id, gender_choice, experience_year, start_time, finish_time, rates)
                                     VALUES (%s , %s , %s , %s , %s , %s )""", (berber.people_id, berber.gender_choice, berber.experience_year,
                                                                                     berber.start_time, berber.finish_time, berber.rates))
        # Delete function
        def delete_with_people_id(self, id):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Berber where people_id = %s", (id,))

        # Update function
        def update_berber(self, berber):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """UPDATE Berber SET gender_choice = %s, experience_year = %s, start_time = %s, finish_time = %s  where people_id = %s""",
                    (berber.gender_choice, berber.experience_year, berber.start_time, berber.finish_time, berber.people_id))
            return True

        # Read function
        def get_all_list(self):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute(""" SELECT * from berber""")
                berber_list = []
                rows = cursor.fetchall()
                for i in rows:
                    berber = Berber()
                    berber.id = i[0]
                    berber.people_id = i[1]
                    berber.berber_shop_id = i[2]
                    berber.gender_choice = i[3]
                    berber.experience_year = i[4]
                    berber.start_time = i[5]
                    berber.finish_time = i[6]
                    berber.rates = i[7]
                    berber_list.append(berber)
                return berber_list

Owner Model
-----------

.. code-block:: python

    class Ownermodel:
        #Read function to get id with username
        def get_id(self, username):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                                SELECT id FROM PEOPLE WHERE username = %s
                                """, (username,))
            row = cursor.fetchone()
            return row

        #Insert function with owner object
        def insert(self, owner):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("""INSERT INTO Owner (people_id, tc_number, serial_number, vol_number, family_order_no, order_no)
                                VALUES (%s , %s , %s , %s , %s , %s )""", (owner.people_id, owner.tc_number, owner.serial_number, owner.vol_number, owner.family_order_no, owner.order_no))

        #Delete function with id
        def delete_with_people_id(self, id):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Owner where people_id = %s", (id,))

        #Update function with owner object
        def update_owner(self, owner):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """UPDATE Owner SET tc_number = %s, serial_number = %s, vol_number = %s, family_order_no = %s, order_no = %s  where people_id = %s""",
                    (owner.tc_number, owner.serial_number, owner.vol_number, owner.family_order_no, owner.order_no, owner.people_id))
            return True

        #Control function the duplicate tc_number for validation
        def control_exist_tc(self, tc):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Owner where tc_number = %s ", (tc, ))
            row = cursor.fetchone()
            if (row == None):
                return False
            return True

        #Read function all owners
        def get_all_list(self):
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute(""" SELECT * from owner""")
                owner_list = []
                rows = cursor.fetchall()
                for i in rows:
                    owner = Owner()
                    owner.id = i[0]
                    owner.people_id = i[1]
                    owner.tc_number = i[2]
                    owner.serial_number = i[3]
                    owner.vol_number = i[4]
                    owner.family_order_no = i[5]
                    owner.order_no = i[6]
                    owner_list.append(owner)
                return owner_list
