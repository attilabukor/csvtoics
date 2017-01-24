#!/usr/bin/env python2.7

import csv
import sys
from icalendar import Calendar, Event, vDatetime, vText
from pytz import timezone
from datetime import datetime
import pytz


year = datetime.now().year
tz = timezone('Europe/Budapest')
cal = Calendar()

cal.add('prodid', '//Attila Bukor//BCE calendar script//')
cal.add('version', '2.0')

i = 0
with open(sys.argv[1], 'rb') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile)
    for row in reader:
        i += 1
        date = row[0].rsplit('/')
        times = row[1].rsplit('-')
        start = times[0].rsplit(':')
        end = times[1].rsplit(':')
        event = Event()
        event.add('summary', row[4])
        event.add('uid', str(year) + date[0] + date[1] + 'T' + start[0] + start[1] + '/' + str(i) + '@r1pp3rj4ck.eu')
        event.add('dtstart', datetime(year, int(date[0]), int(date[1]), int(start[0]), int(start[1]), 0, tzinfo=tz))
        event.add('dtend', datetime(year, int(date[0]), int(date[1]), int(end[0]), int(end[1]), 0, tzinfo=tz))
        event.add('dtstamp', datetime.now())
        event.add('location', vText('Budapesti Corvinus Egyetem, ' + row[7]))
        event.add('description', vText(row[6]))
        cal.add_component(event)

f = open(sys.argv[2], 'wb')
f.write(cal.to_ical())
f.close()
