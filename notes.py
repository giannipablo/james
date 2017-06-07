#!/usr/bin/python

import os
import datetime
import argparse


class Notes():

	def __init__(self,stile, target_path):

		self.__stile        = stile
		self.__target_path = target_path

		npath = './notes_templates/note_template.txt' #'/home/'+os.getlogin()+'/james/notes_templates/note_template.txt'
		if stile.lower()=='meeting':
			npath = './notes_templates/meeting_template.txt' #'/home/'+os.getlogin()+'/james/notes_templates/meeting_template.txt'

		with open(npath,'r') as f:
			self.__template = f.read()

	def new(self, title):
		dtfn  = datetime.datetime.today().strftime('%Y-%m-%d_%H:%M')
		dttxt = datetime.datetime.today().strftime('%d/%m/%Y %H:%M')
		tmp   = self.__template.replace('{TimeStamp}',dttxt)
		tmp   = tmp.replace('{Title}',title.upper())
		
		case_path = '/{0:s}_{1:s}_{2:s}.txt'.format(dtfn,self.__stile,title.lower().replace(' ','_'))
		with open(self.__target_path+case_path,'w') as f:
			f.write(tmp)


nota = Notes('note','./')
nota.new('Me pongo a programar')
