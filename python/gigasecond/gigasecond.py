from datetime import datetime, timedelta


def add_gigasecond(birth_date) : 
	"""
	Calculate the moment when someone has lived for 109 seconds
	"""
	return birth_date + timedelta(seconds=1000000000)

	

# t=time.mktime(x.timetuple()) # Datetime to timestamp
# t+=1000000000
# return datetime.fromtimestamp(t) : # From timestamp to datetime