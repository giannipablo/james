#!/usr/bin/python

import os
import argparse


class Notes(type):

	def __init__(self,type):

		npath = '/home/'+os.getlogin()+'/james/notes_templates/note_template.txt'
		if type.lower()=='meeting':
			npath = '/home/'+os.getlogin()+'/james/notes_templates/meeting_template.txt'

		with open(npath) as f:
			self.__template = f.load(data_file)

	
