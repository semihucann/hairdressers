import datetime

now = datetime.datetime.now()
print(now)
print(now.hour)

t = now.hour
print(t)

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)


