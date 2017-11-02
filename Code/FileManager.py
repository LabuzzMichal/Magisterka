# -*- coding: utf-8 -*-


import shutil
import os
import ntpath

class FileManager(object):
	"""Allow user to find specific file and implement basic files managament functionalities"""
	@staticmethod
	def FindByTimeAndMoveFile(timesring,source,dest):
		timesring.replace("_"," ")
		timesring.replace(".",":")
		content_list = [file_ for file_ in os.listdir(source) if timesring in file_]
		if len(content_list) > 0:
			shutil.move(source,dest+FileManager.BaseName(source))

	@staticmethod
	def FindByTimeAndDeleteFile(timesring,source):
		timesring = timesring.replace(" ","_")
		timesring = timesring.replace(":",".")
		content_list = [file_ for file_ in os.listdir(source) if timesring in file_]
		if len(content_list) > 0:
			os.remove(source+content_list[0])

	@staticmethod
	def MoveFile(source,dest):
		shutil.move(source,dest)

	@staticmethod
	def DeleteFile(source):
		os.remove(source)

	@staticmethod
	def DeleteNonDataFiles(source):
		content_list = [file_ for file_ in os.listdir(source) if not file_.endswith(".dat")]
		for content in content_list:
			os.remove(source+content)

	@staticmethod
	def BaseName(path):
		head, tail = ntpath.split(path)
		return tail or ntpath.basename(head)