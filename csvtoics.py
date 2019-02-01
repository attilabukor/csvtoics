#!/usr/bin/env python

import csv
import sys
from icalendar import Calendar, Event, vDatetime, vText
from pytz import timezone
from datetime import datetime
import pytz


tz = timezone('Europe/Budapest')
cal = Calendar()

cal.add('prodid', '//Attila Bukor//BCE calendar script//')
cal.add('version', '2.0')

i = 0
with open(sys.argv[1], 'rb') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        i += 1
        if row[0] == '':
            continue
        date = row[0].rsplit('.')
        times = row[2].rsplit('-')
        start = times[0].rsplit(':')
        end = times[1].rsplit(':')
        event = Event()
        event.add('summary', row[4])
        event.add('uid', date[0] + date[1] + date[2] + 'T' + start[0] + start[1] + '/' + str(i) + '@bukor.me')
        event.add('dtstart', datetime(int(date[0]), int(date[1]), int(date[2]), int(start[0]), int(start[1]), 0, tzinfo=tz))
        event.add('dtend', datetime(int(date[0]), int(date[1]), int(date[2]), int(end[0]), int(end[1]), 0, tzinfo=tz))
        event.add('dtstamp', datetime.now())
        event.add('location', vText('Budapesti Corvinus Egyetem, ' + row[6]))
        event.add('description', vText(row[5]))
        cal.add_component(event)

f = open(sys.argv[2], 'wb')
f.write(cal.to_ical())
f.close()
