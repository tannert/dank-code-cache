import googlemaps
gm = googlemaps.Client(key='AIzaSyAmGy4lOEqnGnvwfzYfqbfznZstgverBwY')
	
parks = ['arches','canyonlands','capitol reef','bryce canyon','zion']
parks = [park + ' national park' for park in parks]


	
# coords = map(geocode, parks)

matrix = gm.distance_matrix(parks, parks, mode='driving')

def drive_time(index1, index2):
	"returns the drive time in seconds between the parks at index1 and index2 in the list of parks"
	
	return matrix['rows'][index1]['elements'][index2]['duration']['value']

def route_time(permutation):
	"returns the drive time in seconds, given an index permutation of the same length as parks"
	
	total = 0
	for i in range(len(parks)-1):
		total += drive_time(permutation[i],permutation[i-1])
		
	return total
		

#traveling salesman algorithm - yields an ordered list of coordinates


#reorder the list of parks to give the optimal trip
#???
#profit



def salesman_sort():
	pass