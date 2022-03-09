#!python3

from geopy.distance import geodesic
import json
import sys
from pprint import pprint

class Location:
	def __init__(self, name, latitude, longitude):
		self.Name = name
		self.Coordinates = (latitude, longitude);

	def __repr__(self):
		return self.Name + " at (" + str(self.Coordinates[0]) + "," + str(self.Coordinates[1]) + ")"

	def __str__(self):
		return self.Name + " at (" + str(self.Coordinates[0]) + "," + str(self.Coordinates[1]) + ")"

	def milesFrom(self, location):
		return round(geodesic(self.Coordinates, location.Coordinates).miles, 2)

def locationsDataFromFile(path):
	f = open(path, 'r')
	data = json.load(f)	
	f.close()
	return list(map(lambda x: Location(x['name'], x['coordinates']['lat'], x['coordinates']['long']), data['locations']))

def main():
	origin_input_path = sys.argv[1]
	city_input_path = sys.argv[2]
	dest_file = sys.argv[3]

	origins = locationsDataFromFile(origin_input_path)
	origin = origins[0]

	cities = locationsDataFromFile(city_input_path)

	f = open(dest_file, 'w')
	f.write('---\n')
	f.write('Title: Distances from ' + origin.Name + '\n')
	f.write('---\n')
	f.write('\n')

	for c in cities:
		f.write('- The distance from ' + origin.Name + ' to ' + c.Name + " is " + str(origin.milesFrom(c)) + ' miles.\n')
	f.close()


main()