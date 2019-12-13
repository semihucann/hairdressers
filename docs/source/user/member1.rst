Parts Implemented by Ahmet Semih Uçan
=====================================
:Author:
    Ahmet Semih Uçan

My Tables in Database
---------------------


.. figure:: pictures/register_type.jpg
   :scale: 50 %
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).

=====  ========  ============   ======   ==============   ======   ======
id     username  name_surname	mail	 password_hash	  gender   age
=====  ========  ============   ======   ==============   ======   ======
False  False  	 False          False    False            False    False
=====  ========  ============   ======   ==============   ======   ======


.. csv-table:: People Table
   :header: "id", "username", "name_surname", "mail", "password_hash", "gender", "age", "role"
   :widths: 10, 10, 10,10,10,10,10,10

   "5", berberr, "Hasan Berber", "a@g.com", "hashed", "m", "21", "berber"

.. csv-table:: Berber Table
   :header: "id", "people_id", "berbershop_id", "gender_choice", "experience_year", "start_time", "finish_time", "rates"
   :widths: 10, 10, 10,10,10,10,10,10

   "1", #5, "#3", "unisex", "5", "8", "17", "3"

.. csv-table:: Owner Table
   :header: "id", "people_id", "tc_number", "serial_number", "vol_number", "family_order_no", "order_no"
   :widths: 10, 10, 10,10,10,10,10

   "1", #5, "31245654612", "423", "123", "345", "245"
