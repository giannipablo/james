#!/usr/bin/python

import os
import json 
import argparse
import webbrowser

parser = argparse.ArgumentParser()

parser.add_argument("-o" , "--open", dest = "alias"    , default = "",type = str, help="It opens my web pages")
parser.add_argument("-a" , "--add" , dest = "new_alias", default = "",type = str, help="It adds an alias and url. Pass it in the form  'alias|url'")
parser.add_argument("-l" , "--list", dest = "list"     , action  = "store_true" , help="It list the table alias vs. urls")

args = parser.parse_args()


class Webs():

	def __init__(self):
		with open('/home/'+os.getlogin()+'/james/webs/websdb.json') as data_file:
			self.__websdb = json.load(data_file)

	def __get_url(self, alias):
		if alias in self.__websdb:
			return self.__websdb[alias]
		return ''

	def list_urls(self):
		#print ''
		for key in self.__websdb.keys():
			print key + '     \t' + self.__websdb[key]
		print ''

	def add_url(self, alias, url):
		self.__websdb[alias] = url
		with open('/home/'+os.getlogin()+'/james/webs/websdb.json', 'w') as outfile:
			json.dump(self.__websdb, outfile)

	def open_url(self, alias):
		webbrowser.open(self.__get_url(alias))


def main():
	webs = Webs()

	if args.alias!='':
		webs.open_url(alias=args.alias)
		
	if args.list:
		webs.list_urls()

	if args.new_alias!='':
		tmp = args.new_alias.split('|')
		webs.add_url(alias=tmp[0], url=tmp[1])


if __name__ == "__main__":
	main()