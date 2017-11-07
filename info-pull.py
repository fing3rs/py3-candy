#!/usr/bin/python

"""Script to pull geo information from free online providers"""
import sys
import requests
import json

url = 'https://ipinfo.io/'

class ipinfo():
	ip = ""
	hostname = ""
	city = ""
	region = ""
	country = ""
	loc = ""
	org = ""
	conn = ""
	subver = ""

	def display(self):
		print ''
		print 'Connection Information:'
		print 'IP:\t\t', self.ip
		print 'City:\t\t', self.city
		print 'Region:\t\t', self.region
		print 'Country:\t', self.country
		print 'Location:\t', self.loc
		print 'Organisation:\t', self.org
		print 'Conn Type:\t', self.conn
		print 'Client Subver:\t', self.subver

	def load_api(self, node):
		r = requests.get(url + node)
		data = r.json()
		p = json.loads(json.dumps(data))

		self.ip = p["ip"]
		self.city = p["city"]
		self.region = p["region"]
		self.country = p["country"]
		self.loc = p["loc"]
		self.org = p["org"]

	def load_cli(self):
		pass

def main():
	"""Main entry point for the script."""
	with open('data.txt') as f:			# open file as f
		for line in f:					# read each IP
			ip = line					
			if ip != '127.0.0.1\n':		# check for loopback
				node = ipinfo()
				node.load_cli()
				node.load_api(ip)
				node.display()
	pass

if __name__ == '__main__':
	sys.exit(main())