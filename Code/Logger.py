# -*- coding: utf-8 -*-

import sys
import datetime
from Configuration import Paths, ProjectSettings





class Logger(object):
	"""Collect error and logs in specific files"""
	OldClassifierStdout = ""
	OldAnalizeStdout = ""
	ClassifierLogHandler = ""
	AnalizeLogHandler = ""
	@staticmethod
	def ErrorLog(ex):
		old_stdout = sys.stdout
		today = "{0}{1}.log".format(Paths.DirDataLogsErrors,datetime.datetime.now().strftime("%Y-%m-%d"))

		log_file = open(today,"a+")
		if ProjectSettings.DebugMode == True:
			sys.stdout = sys.__stdout__
		else:
			print "Critical error uccured. Detailed information can be found in log file"
			sys.stdout = log_file
		print "=============================================================="
		print "Log started at {0}".format(datetime.datetime.now())
		print "=============================================================="
		print ex
		print "=============================================================="
		print "Log stopped at {0}".format(datetime.datetime.now())
		print "=============================================================="

		print "\n\n"
		sys.stdout = old_stdout
		log_file.close()

	@staticmethod
	def ErrorLogMessage(ex,message):
		old_stdout = sys.stdout
		today = "{0}{1}.log".format(Paths.DirDataLogsErrors,datetime.datetime.now().strftime("%Y-%m-%d"))

		log_file = open(today,"a+")
		if ProjectSettings.DebugMode == True:
			sys.stdout = sys.__stdout__
		else:
			print message
			print "Detailed information can be found in log file"
			sys.stdout = log_file
		print "=============================================================="
		print "Log started at {0}".format(datetime.datetime.now())
		print "=============================================================="
		print ex
		print "=============================================================="
		print "Log stopped at {0}".format(datetime.datetime.now())
		print "=============================================================="

		print "\n\n"
		sys.stdout = old_stdout
		log_file.close()

	@staticmethod
	def InfoLog(infomessage):
		old_stdout = sys.stdout
		today = "{0}{1}.log".format(Paths.DirDataLogsErrors,datetime.datetime.now().strftime("%Y-%m-%d"))

		log_file = open(today,"a+")
		if ProjectSettings.DebugMode == True:
			sys.stdout = sys.__stdout__
		else:
			sys.stdout = log_file
		print "=============================================================="
		print "Log started at {0}".format(datetime.datetime.now())
		print "=============================================================="
		print infomessage
		print "=============================================================="
		print "Log stopped at {0}".format(datetime.datetime.now())
		print "=============================================================="

		print "\n\n"
		sys.stdout = old_stdout
		log_file.close()

	@staticmethod
	def QuitProgram():
		raw_input("Due to some critical error program will quit after you press any button.")
		sys.exit(0)


	@staticmethod
	def StartClassifierLog():
		print "Result od classification can be found in folder: {0}".format(Paths.DirDataLogsClassifier)
		Logger.OldClassifierStdout = sys.stdout
		today = "{0}{1}.log".format(Paths.DirDataLogsClassifier,datetime.datetime.now().strftime("%Y-%m-%d"))

		Logger.ClassifierLogHandler = open(today,"a+")
		if ProjectSettings.DebugMode == True:
			sys.stdout = sys.__stdout__
		else:
			sys.stdout = Logger.ClassifierLogHandler
		
		print "=============================================================="
		print "Log started at {0}".format(datetime.datetime.now())
		print "=============================================================="
	@staticmethod
	def StopClassifierLog():
		print "=============================================================="
		print "Log stopped at {0}".format(datetime.datetime.now())
		print "=============================================================="
		print "\n\n"
		sys.stdout = Logger.OldClassifierStdout
		Logger.ClassifierLogHandler.close()


	@staticmethod
	def StartAnalizeLog():
		print "Result od analyze can be found in folder {0}".format(Paths.DirDataLogsAnalize)
		Logger.OldAnalizeStdout = sys.stdout
		today = "{0}{1}.log".format(Paths.DirDataLogsAnalize,datetime.datetime.now().strftime("%Y-%m-%d"))

		Logger.AnalizeLogHandler = open(today,"a+")
		if ProjectSettings.DebugMode == True:
			sys.stdout = sys.__stdout__
		else:
			sys.stdout = Logger.AnalizeLogHandler
		print "=============================================================="
		print "Log started at {0}".format(datetime.datetime.now())
		print "=============================================================="

	@staticmethod
	def StopAnalizeLog():
		print "=============================================================="
		print "Log stopped at {0}".format(datetime.datetime.now())
		print "=============================================================="
		print "\n\n"
		sys.stdout = Logger.OldAnalizeStdout
		Logger.AnalizeLogHandler.close()






