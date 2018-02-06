from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from django.utils import timezone

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

TIMEZONE = 'America/New_York'      # PDT/MST/GMT-7
EVENT = {
    'summary': 'Dinner with friends',
    'start':  {'dateTime': '2018-02-10T12:00:00', 'timeZone': TIMEZONE},
    'end':    {'dateTime': '2018-02-10T22:00:00', 'timeZone': TIMEZONE},
    # 'attendees': [
    #     {'email': 'seanesmyth@yahoo.com'},
    # ],
    'location': 'Pizzeria Uno',
    'recurrence': [ 'RRULE:FREQ=WEEKLY;UNTIL=20180224']
}

e = GCAL.events().insert(calendarId='primary',
        sendNotifications=True, body=EVENT).execute()

print('''*** %r event added:
    Start: %s
    End:   %s
    location: %s
    organizer: %s ''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime'], e['location'], e['organizer']))
# Python 3.6 string interpolation style print
print(f"My name is {e['summary']}, my age next year is {age+1}.")
