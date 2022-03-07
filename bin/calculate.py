#!python3

from geopy.distance import geodesic
import json
import sys

def main():
	print(sys.argv)
	source_file = sys.argv[1]
	dest_file = sys.argv[2]

	f = open(source_file, 'r')
	data = json.load(f)	
	f.close()

	origin = ( data['origin']['coordinates']['lat'], data['origin']['coordinates']['long']) 

	f = open(dest_file, 'w')
	for x in data['destinations']:
		destination = ( x['coordinates']['lat'], x['coordinates']['long']) 
		d = geodesic(origin, destination).miles
		f.write('<li>The distance from ' + data['origin']['name'] + ' to ' + x['name'] + " is " + str(d) + ' miles</li>\n')
	f.close()


main()