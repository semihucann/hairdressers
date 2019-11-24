from Entities import Berbershop
#trivial function to provide list of berbers, normally supposed to be retrieved from model through database
def listOfBerbers():
    berbershop1=Berbershop()
    berbershop1.shopname="Semih Berber"
    berbershop1.id=1
    berbershop1.closingtime="20.00"
    berbershop1.tradenumber=235
    berbershop1.location="Istanbul"
    berbershop1.openingtime="12.00"
    berbershop1.ownerpeople_id=255
    berbershop1.campaigns = ["c1","c2"]

    berbershop10 = Berbershop()
    berbershop10.shopname = "Semih Berber"
    berbershop10.id = 1
    berbershop10.closingtime = "20.00"
    berbershop10.tradenumber = 235
    berbershop10.location = "Istanbul"
    berbershop10.openingtime = "12.00"
    berbershop10.ownerpeople_id = 255
    berbershop10.campaigns = ["c10,c12"]

    berbershop11 = Berbershop()
    berbershop11.shopname = "Xemih Berber"
    berbershop11.id = 1
    berbershop11.closingtime = "20.00"
    berbershop11.tradenumber = 235
    berbershop11.location = "Istanbul"
    berbershop11.openingtime = "12.00"
    berbershop11.ownerpeople_id = 255
    berbershop11.campaigns = ["c77"]

    berbershop12 = Berbershop()
    berbershop12.shopname = "Temih Berber"
    berbershop12.id = 1
    berbershop12.closingtime = "20.00"
    berbershop12.tradenumber = 235
    berbershop12.location = "Istanbul"
    berbershop12.openingtime = "12.00"
    berbershop12.ownerpeople_id = 255

    berbershop2 = Berbershop()
    berbershop2.shopname="Kuaför Fatih"
    berbershop2.id = 2
    berbershop2.closingtime = "22.00"
    berbershop2.tradenumber = 236
    berbershop2.location = "Ankara"
    berbershop2.openingtime = "12.00"
    berbershop2.ownerpeople_id = 255

    berbershop3 = Berbershop()
    berbershop3.shopname = "Halis Kuaför"
    berbershop3.id = 3
    berbershop3.closingtime = "23.00"
    berbershop3.tradenumber = 2355
    berbershop3.location = "Izmir"
    berbershop3.openingtime = "12.00"
    berbershop3.ownerpeople_id = 258

    berbershop4 = Berbershop()
    berbershop4.shopname = "Ağdacı Ertuğrul"
    berbershop4.id = 4
    berbershop4.closingtime = "23.00"
    berbershop4.tradenumber = 2355
    berbershop4.location = "Diyarbakır"
    berbershop4.openingtime = "12.00"
    berbershop4.ownerpeople_id = 258

    berbershop5 = Berbershop()
    berbershop5.shopname = "Ağdacı Ertuğrul"
    berbershop5.id = 4
    berbershop5.closingtime = "23.00"
    berbershop5.tradenumber = 2355
    berbershop5.location = "Diyarbakır"
    berbershop5.openingtime = "12.00"
    berbershop5.ownerpeople_id = 258

    berbershop6 = Berbershop()
    berbershop6.shopname = "Ağdacı Ertuğrul"
    berbershop6.id = 4
    berbershop6.closingtime = "23.00"
    berbershop6.tradenumber = 2355
    berbershop6.location = "Diyarbakır"
    berbershop6.openingtime = "12.00"
    berbershop6.ownerpeople_id = 258

    berbershop7 = Berbershop()
    berbershop7.shopname = "Ağdacı Ertuğrul"
    berbershop7.id = 4
    berbershop7.closingtime = "23.00"
    berbershop7.tradenumber = 2355
    berbershop7.location = "Diyarbakır"
    berbershop7.openingtime = "12.00"
    berbershop7.ownerpeople_id = 258

    berbershop8 = Berbershop()
    berbershop8.shopname = "Ağdacı Ertuğrul"
    berbershop8.id = 4
    berbershop8.closingtime = "23.00"
    berbershop8.tradenumber = 2355
    berbershop8.location = "Diyarbakır"
    berbershop8.openingtime = "12.00"
    berbershop8.ownerpeople_id = 258


    berbershop9 = Berbershop()
    berbershop9.shopname = "Ağdacı Ertuğrul"
    berbershop9.id = 4
    berbershop9.closingtime = "23.00"
    berbershop9.tradenumber = 2355
    berbershop9.location = "Diyarbakır"
    berbershop9.openingtime = "12.00"
    berbershop9.ownerpeople_id = 258





    berberShopList=[berbershop1,berbershop2,berbershop3,berbershop4,berbershop5
    ,berbershop6,berbershop7,berbershop8,berbershop9,berbershop10,berbershop11,berbershop12]
    return berberShopList