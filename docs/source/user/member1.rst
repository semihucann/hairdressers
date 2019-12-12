Parts Implemented by Ahmet Semih Uçan
================================

:My Tables:
.. csv-table:: People Table
   :header: "id", "username", "name_surname", "mail", "password_hash", "gender", "age", "role"
   :widths: 10, 10, 30,10,10,10,10,10

   "5", berber_efendi, "Hasan Berber", "hasan@berber.com", "hashed", "m", "21", "berber"

.. csv-table:: Berber Table
   :header: "id", "people_id", "berbershop_id", "gender_choice", "experience_year", "start_time", "finish_time", "rates"
   :widths: 10, 10, 30,10,10,10,10,10

   "1", #5, "#3", "unisex", "5", "8", "17", "3"

.. csv-table:: Owner Table
   :header: "id", "people_id", "tc_number", "serial_number", "vol_number", "family_order_no", "order_no"
   :widths: 10, 10, 30,10,10,10,10

   "1", #5, "31245654612", "423", "123", "345", "245"
