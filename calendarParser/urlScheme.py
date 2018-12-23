#End point schemas
baseUrl = 'https://www.nasa.gov'
api = '/api/'
apiVersion = '2'
calendarPath = 'calendar-event'
searchAction = '_search?'
sizeCluster = 'size='


def UrlForItems(items):
	url = "/".join([(u.strip("/") if index + 1 < len(items) else u.lstrip("/")) for index, u in enumerate(items)])
	return url	


def searchRequest(size):
	"""
    Summary line.

    Using the base url and the paramters defined for the api Performs
    a request with the max items passed.

    Parameters
    ----------
    size : int
        number of items max to be retrieved from the API call


    Returns
    -------
    Url
        complete URL to request calendar

	"""
	items = [baseUrl, api, apiVersion, calendarPath, searchAction]
	return UrlForItems(items) + sizeCluster + str(size)







