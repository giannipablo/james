#!/usr/bin/python

import os
import datetime
import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("-d" , "--descript", dest = "descript", default = "",type = str, help="Note name")
parser.add_argument("-n" , "--note"    , dest = "note"    , action  = "store_true" , help="New note")
parser.add_argument("-m" , "--meeting" , dest = "meeting" , action  = "store_true" , help="New meeting note")
parser.add_argument("-o" , "--open"    , dest = "open"    , action  = "store_true" , help="Open the current note")

args = parser.parse_args()

class Notes():

	def __init__(self,stile, target_path):

		self.__stile       = stile
		self.__target_path = target_path
		self.__case_path   = ''

		npath = '/home/'+os.getlogin()+'/james/notes_templates/note_template.txt'
		if stile.lower()=='meeting':
			npath = '/home/'+os.getlogin()+'/james/notes_templates/meeting_template.txt'

		with open(npath,'r') as f:
			self.__template = f.read()

	def new(self, title):
		dtfn  = datetime.datetime.today().strftime('%Y-%m-%d_%H:%M')
		dttxt = datetime.datetime.today().strftime('%d/%m/%Y %H:%M')
		tmp   = self.__template.replace('{TimeStamp}',dttxt)
		tmp   = tmp.replace('{Title}',title.upper())
		
		self.__case_path = '/{0:s}_{1:s}_{2:s}.txt'.format(dtfn,self.__stile,title.lower().replace(' ','_'))
		with open(self.__target_path+self.__case_path,'w') as f:
			f.write(tmp)

	def gfh(self):
		return self.__target_path+self.__case_path

#nota = Notes('note','./')
#nota.new('Me pongo a programar')

def main():
	
	if args.descript!='':
		if args.note:
			notas = Notes(stile='note', target_path='./')
			notas.new(title=args.descript)
		elif args.meeting:
			notas = Notes(stile='meeting', target_path='./')
			notas.new(title=args.descript)
		else:
			notas = Notes(stile='note', target_path='./')
			notas.new(title=args.descript)
	else:
		if args.note:
			notas = Notes(stile='note', target_path='./')
			notas.new(title='no_named_note')
		elif args.meeting:
			notas = Notes(stile='meeting', target_path='./')
			notas.new(title='no_named_note')
		else:
			notas = Notes(stile='note', target_path='./')
			notas.new(title='no_named_note')

	if args.open:
		tmp = subprocess.Popen(['subl','-n',notas.gfh()])

if __name__ == "__main__":
	main()		