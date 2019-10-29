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



    berberShopList=[berbershop1,berbershop2,berbershop3,berbershop4]
    return berberShopList