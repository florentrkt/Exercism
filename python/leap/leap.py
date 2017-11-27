def is_leap_year(x):
    if x%4==0 and x%100!=0:
    	return True
    if x%400==0:
    	return True
    else:
    	return False
