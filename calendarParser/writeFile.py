def writeFile(fileName,calendarObject):
	"""
    Summary line.

    saves in disc the given file with the name passed.

    Parameters
    ----------
    fileName : str
        name for the file

    calendarObject
    		object to save, expected a ics file
   """
	
	with open(fileName, 'w', encoding='utf-8-sig') as my_calendar_file:
		try:
			my_calendar_file.writelines(calendarObject)
		except :
			raise TypeError("Could not save file")
