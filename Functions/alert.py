from .getIds import getIds
from Database.db import DB
from .searchSlots import searchSlots
from .send import send

def alert():
    ids= getIds()
    for id in ids:
        data= searchSlots(id)
        for user in DB['Users']:
            for center in data:
                for session in center['sessions']:
                    # First Dose
                    if user['dose'] == 'first' and user['districtCode'] == id and session['available_capacity_dose1'] > 0:
                        
                        if session['allow_all_age'] == True:
                            msg = "š¤ <b><u>Co-Win Slot Alerts</u></b>\n\nSlot Available for <b>{}</b>".format(user['name'])+"\n\nš  Venue: {}\n\n".format(center['name'])+"šļø Date: <b>{}</b>\n\n".format(session['date'])+"š¢ Available Doses: {}\n\n".format(
                            session['available_capacity_dose1'])+"š Vaccine: {}\n\n".format(session['vaccine'])+"š Dose: First\n\n"+"ā° Slots: {}\n\n".format(session['slots'])+"š Address: {}".format(center['address'])
                            send(user['chatId'], msg)
                        else:
                            if user['ageGroup'] == 18 and session['min_age_limit'] == 18:
                                msg = "š¤ <b><u>Co-Win Slot Alerts</u></b>\n\nSlot Available for <b>{}</b>".format(user['name'])+"\n\nš  Venue: {}\n\n".format(center['name'])+"šļø Date: <b>{}</b>\n\n".format(session['date'])+"š¢ Available Doses: {}\n\n".format(
                                session['available_capacity_dose1'])+"š Vaccine: {}\n\n".format(session['vaccine'])+"š Dose: First\n\n"+"ā° Slots: {}\n\n".format(session['slots'])+"š Address: {}".format(center['address'])
                                send(user['chatId'], msg)
                            
                            if user['ageGroup'] == 40 and session['max_age_limit'] == 44:
                                msg = "š¤ <b><u>Co-Win Slot Alerts</u></b>\n\nSlot Available for <b>{}</b>".format(user['name'])+"\n\nš  Venue: {}\n\n".format(center['name'])+"šļø Date: <b>{}</b>\n\n".format(session['date'])+"š¢ Available Doses: {}\n\n".format(
                                session['available_capacity_dose1'])+"š Vaccine: {}\n\n".format(session['vaccine'])+"š Dose: First\n\n"+"ā° Slots: {}\n\n".format(session['slots'])+"š Address: {}".format(center['address'])
                                send(user['chatId'], msg)

                            if user['ageGroup'] == 45 and session['min_age_limit'] == 45:
                                msg = "š¤ <b><u>Co-Win Slot Alerts</u></b>\n\nSlot Available for <b>{}</b>".format(user['name'])+"\n\nš  Venue: {}\n\n".format(center['name'])+"šļø Date: <b>{}</b>\n\n".format(session['date'])+"š¢ Available Doses: {}\n\n".format(
                                session['available_capacity_dose1'])+"š Vaccine: {}\n\n".format(session['vaccine'])+"š Dose: First\n\n"+"ā° Slots: {}\n\n".format(session['slots'])+"š Address: {}".format(center['address'])
                                send(user['chatId'], msg)

                    # Second Dose
                    if user['dose'] == 'second' and user['vaccine'] == session['vaccine'] and user['districtCode'] == id and session['available_capacity_dose2'] > 0:
                        if session['allow_all_age'] == True:
                            msg = "š¤ <b><u>Co-Win Slot Alerts</u></b>\n\nSlot Available for <b>{}</b>".format(user['name'])+"\n\nš  Venue: {}\n\n".format(center['name'])+"šļø Date: <b>{}</b>\n\n".format(session['date'])+"š¢ Available Doses: {}\n\n".format(
                            session['available_capacity_dose2'])+"š Vaccine: {}\n\n".format(session['vaccine'])+"š Dose: Second\n\n"+"ā° Slots: {}\n\n".format(session['slots'])+"š Address: {}".format(center['address'])
                            send(user['chatId'], msg)
                        else:
                            if user['ageGroup'] == 18 and session['min_age_limit'] == 18:
                                msg = "š¤ <b><u>Co-Win Slot Alerts</u></b>\n\nSlot Available for <b>{}</b>".format(user['name'])+"\n\nš  Venue: {}\n\n".format(center['name'])+"šļø Date: <b>{}</b>\n\n".format(session['date'])+"š¢ Available Doses: {}\n\n".format(
                                session['available_capacity_dose2'])+"š Vaccine: {}\n\n".format(session['vaccine'])+"š Dose: Second\n\n"+"ā° Slots: {}\n\n".format(session['slots'])+"š Address: {}".format(center['address'])
                                send(user['chatId'], msg)
                            
                            if user['ageGroup'] == 40 and session['max_age_limit'] == 44:
                                msg = "š¤ <b><u>Co-Win Slot Alerts</u></b>\n\nSlot Available for <b>{}</b>".format(user['name'])+"\n\nš  Venue: {}\n\n".format(center['name'])+"šļø Date: <b>{}</b>\n\n".format(session['date'])+"š¢ Available Doses: {}\n\n".format(
                                session['available_capacity_dose2'])+"š Vaccine: {}\n\n".format(session['vaccine'])+"š Dose: Second\n\n"+"ā° Slots: {}\n\n".format(session['slots'])+"š Address: {}".format(center['address'])
                                send(user['chatId'], msg)

                            if user['ageGroup'] == 45 and session['min_age_limit'] == 45:
                                msg = "š¤ <b><u>Co-Win Slot Alerts</u></b>\n\nSlot Available for <b>{}</b>".format(user['name'])+"\n\nš  Venue: {}\n\n".format(center['name'])+"šļø Date: <b>{}</b>\n\n".format(session['date'])+"š¢ Available Doses: {}\n\n".format(
                                session['available_capacity_dose2'])+"š Vaccine: {}\n\n".format(session['vaccine'])+"š Dose: Second\n\n"+"ā° Slots: {}\n\n".format(session['slots'])+"š Address: {}".format(center['address'])
                                send(user['chatId'], msg)

                    
