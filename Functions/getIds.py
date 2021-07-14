from Database.db import DB
def getIds():
    res = []
    for id in DB['Users']:
        if id['districtCode'] not in res:
            res.append(id['districtCode'])
    return res