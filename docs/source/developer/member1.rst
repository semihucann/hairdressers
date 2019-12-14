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


