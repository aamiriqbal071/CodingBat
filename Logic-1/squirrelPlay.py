
# The squirrels in Palo Alto spend most of the day playing. In particular,
# they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean isSummer, return true if the squirrels play and false otherwise.


# squirrelPlay(70, false) → true
# squirrelPlay(95, false) → false
# squirrelPlay(95, true) → true

def squirrelPlay(a,isSummer):
	if isSummer:
		return 60<=a<=100
	else:
		return 60=<a<=90


print(squirrelPlay(70, False))
print(squirrelPlay(95, False))
print(squirrelPlay(95, True))
