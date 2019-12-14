Parts Implemented by Ertugrul Semiz
=====================================

My Tables in Database
---------------------
Comment  Table

=====  =========  ==============  ==========  ================  ==============  ======  ==========================  ============  ===============  ===========================
id     people_id  berber          berbershop  title	        content         rate    date_time                   comment_like  comment_dislike  keywords
=====  =========  ==============  ==========  ================  ==============  ======  ==========================  ============  ===============  ===========================
25     87	  NULL            13          izmirin en iyisi  gayet begendik  4       2019-12-14 21:02:56.554483  0             0                Expensive,Talentless,Dirty
=====  =========  ==============  ==========  ================  ==============  ======  ==========================  ============  ===============  ===========================

Contact_info Table

===  =============  ========   ================   ===========     ==========  ===========
id   berbershop_id  type       telephone_number   facebook        twitter     instagram
===  =============  ========   ================   ===========     ==========  ===========
5    11             company    5359266963         ertugrulsm      ertugrulsm  ertugrulsmz
===  =============  ========   ================   ===========     ==========  ===========

Rezervation Table

=====  =========    =============   ==========================   ====================  =============== =========  ==========  ==============
id     people_id    berbershop_id   datetime_registration        datetime_rezervation  status          note       price_type  payment_method
=====  =========    =============   ==========================   ====================  =============== =========  ==========  ==============
1      78           11              2019-12-14 15:36:52.266049   2019-12-15 09:00:00   notokey         ordayimmm  1           creditcard
=====  =========    =============   ==========================   ====================  =============== =========  ==========  ==============

Commentlikedislike Table

===  =============  =========   ========   ==========
id   comment_id     people_id   ifliked    ifdisliked
===  =============  =========   ========   ==========
1    1              79          1          0
===  =============  =========   ========   ==========



In this project I was in charge of  4 tables. Even though database rules does permit different length of phone numbers, i have done
validation for it to be 10 digits exactly. Also, comment title, content can not be null so it is covered also form validation.



Main Page
-----------

I've created main page of website (except navigation bar which is common for all page). In the first part of main page there is
bootstrap carausel which has 3 navigators : who are we , main bar, all barbershops which direct to the corresponding area in the
same page through buttons on them.



.. figure:: pictures/bigcarousel.png
   :scale: 50 %
   :alt: main carousel directing

Who are we  :
Information about our system.
Main Bar :
General links exists here. Visitors directly reach most of the features from this  sliding carousel.


.. figure:: pictures/whoarewe.png
   :scale: 50 %
   :alt: who are we

.. figure:: pictures/mainbar.png
   :scale: 50 %
   :alt: mainbar

All Barbershops :
İt is the table having list of all the barbershops in the systems. Name of the shop, City, Address etc. There is also link which
users can access berbershopview page which includes info about barbershops, comments made by customers also direct links to the
take rezervation.

.. figure:: pictures/allberbershops.png
   :scale: 50 %
   :alt: mainbar




   Signup Page

Signin Flow
-----------
In signin page, I get username and password from client. After this operation, I hash the password with passlib.hash library and check.

.. figure:: pictures/signin.jpg
   :scale: 90 %
   :alt: map to buried treasure

   Signin Page

- If written username and password is correct, "You have successfully logged in <TYPE>" message is shown.
- If written username and password is wrong, error message is shown.

.. figure:: pictures/signin2.jpg
   :scale: 90 %
   :alt: map to buried treasure

   Signin Page Respond


Admin Panel
-----------

If person signin to web site as admin, admin panel can be used.
In admin panel, people berber and owner tables are shown.
The panel provides update and delete facilities on 3 tables.

.. figure:: pictures/admin_panel.jpg
   :scale: 50 %
   :alt: map to buried treasure

   Admin Panel

Admin Panel Operations
----------------------

- To delete any user, mark the check_box in the first column of people table and click the "delete selected" button.
- To order table, select order type from select_box and click the order button
- To edit any person, click the rightmost button on that person's row and



    3 different update operation by person type for tables(people, berber, owner)


- If person doesn't login, navbar is shown like that first part of picture.
- If person login and person isn't admin, navbar is shown like that second part of picture.
- If person login and person is admin, Admin Panel url will be added to navbar and navbar is shown like that third part of picture.

Navbar Edition
--------------

    Navbar links changing according to the type of person logging in
