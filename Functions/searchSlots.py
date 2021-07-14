import requests

from .makeDate import makeDate

cowinEndpoint = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'

def searchSlots(id):
    date= makeDate()
    url = cowinEndpoint+"?district_id={}".format(id)+"&date={}".format(date)
    try:
        res = requests.get(url)
        return res.json()['centers']
    except requests.exceptions.RequestException as e:
        print('Error getting data', e)