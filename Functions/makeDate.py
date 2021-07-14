import datetime

def makeDate():
    d = str(datetime.datetime.today())
    d1 = d.split()[0].split('-')[::-1]
    d2 = str(d1[0]+"-"+d1[1]+'-'+d1[2])
    return d2