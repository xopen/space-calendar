import requests
from ics import Calendar,Event
import numpy as np
import urlScheme
import  writeFile as wf

""" URL Definition """
url = urlScheme.searchRequest(1000)

""" Get Json """ 
try:
	resp = requests.get(url)
	resp.raise_for_status()		
	
	json_data = resp.json()
	""" Json normalization parsing """
	resutlHits = np.asarray(json_data["hits"]["hits"])
	""" Calendar creation """
	calendarObject = Calendar()

	# node keys
	sourceNodeKey = "_source"
	dateKey 			= "event-date"
	titleKey 			= "title"
	uuidKey 			= "nid"
	startDateKey 	= "value"
	endDateKey 		= "value2"
	dateNodeLevel = 0

	for eventNasa in resutlHits:

		eventTitle = eventNasa[sourceNodeKey][titleKey]
		eventDateBegin = eventNasa[sourceNodeKey][dateKey][dateNodeLevel][startDateKey]
		eventDateEnd = eventNasa[sourceNodeKey][dateKey][dateNodeLevel][endDateKey]
		eventUuid = eventNasa[sourceNodeKey][uuidKey]

		""" Event creation """
		event = Event()
	
		""" Event data """
		event.name = eventTitle
		event.begin = eventDateBegin
		event.end = eventDateEnd
		event.uid = eventUuid #unique to event

		#Add event to calendar	
		calendarObject.events.add(event)


	""" write calendar file """
	wf.writeFile('space-calendar_spaceA.ics',calendarObject)

except requests.RequestException as err:
	print(err)
