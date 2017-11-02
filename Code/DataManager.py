#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sqlite3 
from lxml import etree
from Configuration import Paths, SensorsSettings
from Logger import Logger
from FileManager import FileManager



class DataManager(object):
	"""Class responsible for sensors data handling"""

	### Take from path Paths.DirDataSensorsPreprocess all files generated from preprocessData.cxx script
	### and save them(values from files) to database creating time dependence function for every sensor.
	def PrepareSensorData(self):
		FileManager.DeleteNonDataFiles(Paths.DirDataSensorsPreprocess)
		content_list = [file_ for file_ in os.listdir(Paths.DirDataSensorsPreprocess)] #pobranie listy plikow
		content_list = sorted(content_list) # sortowanie po dacie
		sensors = {i:{"mean":[],"rms":[],"skewness":[],"curtosis":[]} for i in range(SensorsSettings.SensorsCount)} # utworzenie slownika. Klucz to numer sensora, zas wartosci to podslowniki z konkretnymi parametrami
		for con in content_list: 
			from_sensors = np.loadtxt(Paths.DirDataSensorsPreprocess + con, delimiter=",") # Pobranie parametrow sensorow z konkretnego dnia
			for i in range(SensorsSettings.SensorsCount): 
				sensors[i]["mean"].append(float(from_sensors[i][0]))
				sensors[i]["rms"].append(float(from_sensors[i][1]))
				sensors[i]["skewness"].append(float(from_sensors[i][2]))
				sensors[i]["curtosis"].append(float(from_sensors[i][3]))
	
		result = [[] for i in range(SensorsSettings.SensorsCount)] # tablica zawierajaca jawna zaleznosc czasowa parametrow kazdego sensora 
		for sensor in sensors:
			for i in range(len(sensors[sensor]["mean"])):
				result[sensor].append([sensors[sensor]["mean"][i],sensors[sensor]["rms"][i],sensors[sensor]["skewness"][i],sensors[sensor]["curtosis"][i]])
	
		time1 = self.GetTimeList(db = False)
		con = sqlite3.connect(Paths.DirDataDB)
		with con:
			cur = con.cursor()
			for i in range(SensorsSettings.SensorsCount):
				numer = str(i) if i > 9 else "0"+str(i)
				for j in range(len(sensors[i]["mean"])):
						try:
							command = "INSERT INTO DATA_SENSOR_{0} VALUES('{1}',{2},{3},{4},{5},{6},{7})".format(numer,str(time1[j]),sensors[i]["mean"][j],sensors[i]["rms"][j],sensors[i]["curtosis"][j],sensors[i]["skewness"][j],1,1)
							cur.execute(command)
						except sqlite3.IntegrityError as ie:
							Logger.ErrorLogMessage(ie,"rekord z daty {0} istnieje już w bazie danych!".format(time1[j]))
						except Exception as ex:
							Logger.ErrorLog(ex)
							Logger.QuitProgram()
	

	### Take from path Paths.DirDataSensorsNewData all new files generated from preprocessData.cxx script
	### and save them(values from files) to database creating time dependence function for every sensor.
	def PrepareSensorNewData(self):
		FileManager.DeleteNonDataFiles(Paths.DirDataSensorsNewData)
		content_list = [file_ for file_ in os.listdir(Paths.DirDataSensorsNewData)] #pobranie listy plikow
		content_list = sorted(content_list) # sortowanie po dacie
		sensors = {i:{"mean":[],"rms":[],"skewness":[],"curtosis":[]} for i in range(SensorsSettings.SensorsCount)} # utworzenie slownika. Klucz to numer sensora, zas wartosci to podslowniki z konkretnymi parametrami
		for con in content_list: 
			from_sensors = np.loadtxt(Paths.DirDataSensorsNewData + con, delimiter=",") # Pobranie parametrow sensorow z konkretnego dnia
			for i in range(SensorsSettings.SensorsCount): 
				sensors[i]["mean"].append(float(from_sensors[i][0]))
				sensors[i]["rms"].append(float(from_sensors[i][1]))
				sensors[i]["skewness"].append(float(from_sensors[i][2]))
				sensors[i]["curtosis"].append(float(from_sensors[i][3]))
	
		result = [[] for i in range(SensorsSettings.SensorsCount)] # tablica zawierajaca jawna zaleznosc czasowa parametrow kazdego sensora 
		for sensor in sensors:
			for i in range(len(sensors[sensor]["mean"])):
				result[sensor].append([sensors[sensor]["mean"][i],sensors[sensor]["rms"][i],sensors[sensor]["skewness"][i],sensors[sensor]["curtosis"][i]])
	
		time1 = self.GetTimeList(db = False,newdata = True)
		con = sqlite3.connect(Paths.DirDataDB)
		with con:
			cur = con.cursor()
			for i in range(SensorsSettings.SensorsCount):
				numer = str(i) if i > 9 else "0"+str(i)
				for j in range(len(sensors[i]["mean"])):
						try:
							command = "INSERT INTO DATA_SENSOR_{0} VALUES('{1}',{2},{3},{4},{5},{6},Null)".format(numer,str(time1[j]),sensors[i]["mean"][j],sensors[i]["rms"][j],sensors[i]["curtosis"][j],sensors[i]["skewness"][j],-1)
							cur.execute(command)
						except sqlite3.IntegrityError as ie:
							Logger.ErrorLogMessage(ie,"rekord z daty {0} dla sensora {1} istnieje już w bazie danych!".format(time1[j],numer))
							FileManager.FindByTimeAndDeleteFile(str(time1[j]),Paths.DirDataSensorsNewData)
						except Exception as ex:
							FileManager.FindByTimeAndDeleteFile(str(time1[j]),Paths.DirDataSensorsNewData)
							Logger.ErrorLog(ex)
							Logger.QuitProgram()
		for filepath in os.listdir(Paths.DirDataSensorsNewData):
			FileManager.MoveFile(Paths.DirDataSensorsNewData+filepath,Paths.DirDataSensorsPreprocess+filepath)
		
	
		
		
	### Create and return variable which keeps information about sensors parameters (time dependent).
	### Data are taken from database, which have to be under Paths.DirDataDB
	### Data are taken in range from "timefrom" to "timeto"
	def GetSensorData(self, alldata = True, timefrom = None, timeto = None):
		acceptedflag1 = "WHERE IS_ACCEPTED_FLAG=1" if (alldata is False) else ""
		acceptedflag2 = "IS_ACCEPTED_FLAG=1 AND" if (alldata is False) else ""
	
		flag = True
		if timefrom is None or timeto is None:
			flag = True
		else:
			flag = False
			try:
				datetime.datetime.strptime(timefrom, '%Y-%m-%d')
				datetime.datetime.strptime(timeto, '%Y-%m-%d')
			except ValueError:
				print "Error occured. Data should be in YYYY-MM-DD format"
				return
	
		conn = sqlite3.connect(Paths.DirDataDB)
		c = conn.cursor()
		sensors = {i:{"mean":[],"rms":[],"skewness":[],"curtosis":[]} for i in range(SensorsSettings.SensorsCount)}
		for i in range(SensorsSettings.SensorsCount):
			numer = str(i) if i > 9 else "0"+str(i)
			command = ""
			if flag:
				command = "SELECT MEAN, RMS, CURTOSIS, SKEWNESS FROM DATA_SENSOR_{0} {1} ORDER BY TIME".format(numer, acceptedflag1)
			else:
				command = "SELECT MEAN, RMS, CURTOSIS, SKEWNESS FROM DATA_SENSOR_{0} WHERE {1} TIME BETWEEN date('{2}') AND date('{3}') ORDER BY TIME".format(numer,acceptedflag2, timefrom, timeto)
			try:
				execute = c.execute(command)
			except Exception as ex:
				Logger.ErrorLog(ex)
				Logger.QuitProgram()
	
			for row in execute:
				sensors[i]["mean"].append(float(row[0]))
				sensors[i]["rms"].append(float(row[1]))
				sensors[i]["curtosis"].append(float(row[2]))	
				sensors[i]["skewness"].append(float(row[3]))
		return sensors			
	


	### Create and return variable which keeps information about sensors parameters(time dependent).
	### Data are taken from database, which have to be under Paths.DirDataDB
	### Data are taken in range from "timefrom" to "timeto"
	def GetNewSensorData(self, timefrom = None, timeto = None):
		flag = True
		if timefrom is None or timeto is None:
			flag = True
		else:
			flag = False
			try:
				datetime.datetime.strptime(timefrom, '%Y-%m-%d')
				datetime.datetime.strptime(timeto, '%Y-%m-%d')
			except ValueError:
				print "Error occured. Data should be in YYYY-MM-DD format"
				return
	
		conn = sqlite3.connect(Paths.DirDataDB)
		c = conn.cursor()
		sensors = {i:{"mean":[],"rms":[],"skewness":[],"curtosis":[]} for i in range(SensorsSettings.SensorsCount)}
		for i in range(SensorsSettings.SensorsCount):
			numer = str(i) if i > 9 else "0"+str(i)
			command = ""
			if flag:
				command = "SELECT MEAN, RMS, CURTOSIS, SKEWNESS FROM DATA_SENSOR_{0} WHERE IS_ACCEPTED_FLAG=-1 ORDER BY TIME".format(numer)
			else:
				command = "SELECT MEAN, RMS, CURTOSIS, SKEWNESS FROM DATA_SENSOR_{0} WHERE IS_ACCEPTED_FLAG=-1 AND TIME BETWEEN date('{1}') AND date('{2}') ORDER BY TIME".format(numer, timefrom, timeto)
			try:
				execute = c.execute(command)
			except Exception as ex:
				Logger.ErrorLog(ex)
				Logger.QuitProgram()
	
			for row in execute:
				sensors[i]["mean"].append(float(row[0]))
				sensors[i]["rms"].append(float(row[1]))
				sensors[i]["curtosis"].append(float(row[2]))	
				sensors[i]["skewness"].append(float(row[3]))
		return sensors		
	
	
	### Create and return variable which keeps information about projected sensors parameters (time dependent).
	### Data are taken from database, which have to be under Paths.DirDataDB
	### Data are taken in range from "timefrom" to "timeto"
	def GetProjectedSensorData(self, timefrom = None, timeto = None):
		flag = True
		if timefrom is None or timeto is None:
			flag = True
		else:
			flag = False
			try:
				datetime.datetime.strptime(timefrom, '%Y-%m-%d')
				datetime.datetime.strptime(timeto, '%Y-%m-%d')
			except ValueError:
				print "Error occured. Data should be in YYYY-MM-DD format"
				return
	
		conn = sqlite3.connect(Paths.DirDataDB)
		c = conn.cursor()
		sensors = {i:{"mean_correct":[],"mean_incorrect":[],"rms_correct":[],"rms_incorrect":[]} for i in range(SensorsSettings.SensorsCount)}
		for i in range(SensorsSettings.SensorsCount):
			numer = str(i) if i > 9 else "0"+str(i)
			command = ""
			if flag:
				command = "SELECT MEAN, MEAN_CORRECTED, RMS, RMS_CORRECTED FROM DATA_SENSOR_PROJECTED_{0} ORDER BY TIME".format(numer)
			else:
				command = "SELECT MEAN, MEAN_CORRECTED, RMS, RMS_CORRECTED FROM DATA_SENSOR_PROJECTED_{0} WHERE TIME BETWEEN date('{1}') AND date('{2}') ORDER BY TIME".format(numer,timefrom, timeto)
			try:
				execute = c.execute(command)
			except Exception as ex:
				Logger.ErrorLog(ex)
				Logger.QuitProgram()
	
			for row in execute:
				sensors[i]["mean_correct"].append(float(row[0]))
				sensors[i]["mean_incorrect"].append(float(row[1]))
				sensors[i]["rms_correct"].append(float(row[2]))	
				sensors[i]["rms_incorrect"].append(float(row[3]))
		return sensors	
	
	
	
	
	### Create and return variable which keeps information abour time of each measurement
	### Data are taken from database, which have to be under Paths.DirDataDB
	###
	def GetTimeList(self, alldata = True, newdata = False, db = True, timefrom = None, timeto = None):
		acceptedflag1 = "WHERE IS_ACCEPTED_FLAG=1" if (alldata is False) else ""
		acceptedflag2 = "IS_ACCEPTED_FLAG=1 AND" if (alldata is False) else ""
		flag = True
		if timefrom is None or timeto is None:
			flag = True
		else:
			flag = False
			try:
				datetime.datetime.strptime(timefrom, '%Y-%m-%d')
				datetime.datetime.strptime(timeto, '%Y-%m-%d')
			except ValueError:
				print "Error occured. Data should be in YYYY-MM-DD format"
				return
	
		if db:
			time1 = []
			conn = sqlite3.connect(Paths.DirDataDB)
			c = conn.cursor()
			if newdata:
				if flag:
					command = "SELECT TIME FROM DATA_SENSOR_00 WHERE IS_ACCEPTED_FLAG=-1 ORDER BY TIME".format(acceptedflag1)
				else:
					command = "SELECT TIME FROM DATA_SENSOR_00 WHERE IS_ACCEPTED_FLAG=-1 AND TIME BETWEEN date('{1}') AND date('{2}') ORDER BY TIME".format(acceptedflag2, timefrom, timeto)
			else:
				if flag:
					command = "SELECT TIME FROM DATA_SENSOR_00 {0} ORDER BY TIME".format(acceptedflag1)
				else:
					command = "SELECT TIME FROM DATA_SENSOR_00 WHERE {0} TIME BETWEEN date('{1}') AND date('{2}') ORDER BY TIME".format(acceptedflag2, timefrom, timeto)
			try:
				execute = c.execute(command)
			except Exception as ex:
				Logger.ErrorLog(ex)
				Logger.QuitProgram()
			for row in execute:
				time1.append(datetime.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S"))
	
			time1 = sorted(time1)
			return time1
		else:
			content_list = []
			if newdata:
				content_list = [file_ for file_ in os.listdir(Paths.DirDataSensorsNewData) if file_.endswith(".dat")] #pobranie listy plikow
			else:
				content_list = [file_ for file_ in os.listdir(Paths.DirDataSensorsPreprocess) if file_.endswith(".dat")] #pobranie listy plikow

			content_list = sorted(content_list) # sortowanie po dacie
			time1 = []
			for line in content_list:
				time1.append(line[-23:-4])
				time1[-1] = datetime.datetime(int(time1[-1][0:4]),int(time1[-1][5:7]),int(time1[-1][8:10]),int(time1[-1][11:13]),int(time1[-1][14:16]),int(time1[-1][17:19]))
			time1 = sorted(time1)
			return time1
	
	
	
	
	### Create charts and histogram for sensors parameters (time dependent)
	### and save them in Paths.DirFigSensors
	def DrawCharts(self, sensorsdata, timelist):
		time1 = timelist
		sensors = sensorsdata
	
		equations = self.__GetTrendLine(sensors, time1)
	
		for sensor in range(SensorsSettings.SensorsCount):
			plt.plot(time1,sensors[sensor]["mean"],"-bo")
			plt.plot(equations[sensor]["mean"][0][0],equations[sensor]["mean"][0][1](equations[sensor]["mean"][0][0]),'g--', label = "First y=%.4fx+(%.f)" % (equations[sensor]["mean"][0][2][0],equations[sensor]["mean"][0][2][1])) # Z BLEDAMI
			plt.legend(loc='best')
			plt.plot(equations[sensor]["mean"][2][0],equations[sensor]["mean"][2][1](equations[sensor]["mean"][2][0]),'r--', label = "Second y=%.4fx+(%.f)" % (equations[sensor]["mean"][2][2][0],equations[sensor]["mean"][2][2][1])) # BEZ BLEDOW
			plt.legend(loc='best')
			plt.gcf().autofmt_xdate()
			plt.savefig(Paths.DirFigSensors +"Sensor_"+str(sensor)+"_"+"mean")
			plt.close()
			plt.hist(sensors[sensor]["mean"],bins = 20)
			plt.savefig(Paths.DirFigSensors + "Histogram_Sensor_"+str(sensor)+"_"+"mean")
			plt.close()
		
			plt.plot(time1,sensors[sensor]["rms"],"-bo")
			plt.plot(equations[sensor]["rms"][0][0],equations[sensor]["rms"][0][1](equations[sensor]["rms"][0][0]),'g--', label = "First y=%.4fx+(%.f)" % (equations[sensor]["rms"][0][2][0],equations[sensor]["rms"][0][2][1])) # Z BLEDAMI
			plt.legend(loc='best')
			plt.plot(equations[sensor]["rms"][2][0],equations[sensor]["rms"][2][1](equations[sensor]["rms"][2][0]),'r--', label = "Second y=%.4fx+(%.f)" % (equations[sensor]["rms"][2][2][0],equations[sensor]["rms"][2][2][1])) # BEZ BLEDOW
			plt.legend(loc='best')
			plt.gcf().autofmt_xdate()
			plt.savefig(Paths.DirFigSensors + "Sensor_" + str(sensor) + "_" + "rms")
			plt.close()
			plt.hist(sensors[sensor]["rms"])
			plt.savefig(Paths.DirFigSensors + "Histogram_Sensor_"+str(sensor)+"_"+"rms")
			plt.close()
			
			plt.plot(time1,sensors[sensor]["skewness"],"-bo")
			plt.gcf().autofmt_xdate()
			plt.savefig(Paths.DirFigSensors + "Sensor_"+str(sensor)+"_"+"skewness")
			plt.close()
			plt.hist(sensors[sensor]["skewness"])
			plt.savefig(Paths.DirFigSensors + "Histogram_Sensor_"+str(sensor)+"_"+"skewness")
			plt.close()
			
			plt.plot(time1,sensors[sensor]["curtosis"],"-bo")
			plt.gcf().autofmt_xdate()
			plt.savefig(Paths.DirFigSensors + "Sensor_"+str(sensor)+"_"+"curtosis")
			plt.close()
			plt.hist(sensors[sensor]["curtosis"])
			plt.savefig(Paths.DirFigSensors + "Histogram_Sensor_"+str(sensor)+"_"+"curtosis")
			plt.close()
	
	
	### Create charts and histogram for sensors projected parameters (time dependent)
	### and save them in Paths.DirFigProejctedSensors	
	def DrawProjectedCharts(self, projectedsensordata):
	
		sensors = projectedsensordata
		for sensor in range(SensorsSettings.SensorsCount):
	
			plt.hist(sensors[sensor]["mean_correct"],bins = 20)
			plt.savefig(Paths.DirFigProjectedSensors + "Histogram_Sensor_"+str(sensor)+"_"+"mean_correct")
			plt.close()
		
			plt.hist(sensors[sensor]["mean_incorrect"])
			plt.savefig(Paths.DirFigProjectedSensors + "Histogram_Sensor_"+str(sensor)+"_"+"mean_incorrect")
			plt.close()
			
			plt.hist(sensors[sensor]["rms_correct"])
			plt.savefig(Paths.DirFigProjectedSensors + "Histogram_Sensor_"+str(sensor)+"_"+"rms_correct")
			plt.close()
		
			plt.hist(sensors[sensor]["rms_incorrect"])
			plt.savefig(Paths.DirFigProjectedSensors + "Histogram_Sensor_"+str(sensor)+"_"+"rms_incorrect")
			plt.close()
	
	
	
	### Funkcja tworzaca projekccje wykresow parametrow wzdluz linii trendu
	### 
	### 
	def SaveProjectedData(self, sensorsdata, timelist):
		time1 = timelist 
		sensors = sensorsdata
	
		equations = self.__GetTrendLine(sensors, time1)
		result = [[] for i in range(SensorsSettings.SensorsCount)] 
		for sensor in range(SensorsSettings.SensorsCount):
			sensor_mean_correct = equations[sensor]["mean"][2][1](mdates.date2num(time1))
			sensor_mean_incorrect = equations[sensor]["mean"][0][1](mdates.date2num(time1))
			sensor_rms_correct = equations[sensor]["rms"][2][1](mdates.date2num(time1))
			sensor_rms_incorrect = equations[sensor]["rms"][0][1](mdates.date2num(time1))
			for i in range(len(sensor_mean_correct)):
				mean_correct = sensors[sensor]["mean"][i]-sensor_mean_correct[i]
				mean_incorrect = sensors[sensor]["mean"][i]-sensor_mean_incorrect[i]
				rms_correct = sensors[sensor]["rms"][i]-sensor_rms_correct[i]
				rms_incorrect = sensors[sensor]["rms"][i]-sensor_rms_incorrect[i]
				result[sensor].append([mean_correct,mean_incorrect,rms_correct,rms_incorrect])
		time1 = timelist
		con = sqlite3.connect(Paths.DirDataDB)
		with con:
			cur = con.cursor()
			for i in range(SensorsSettings.SensorsCount):
				numer = str(i) if i > 9 else "0"+str(i)
				for j in range(len(time1)):
					try:
						command = "INSERT INTO DATA_SENSOR_PROJECTED_{0} VALUES('{1}',{2},{3},{4},{5})".format(numer,str(time1[j]),result[i][j][0],result[i][j][1],result[i][j][2],result[i][j][3])
						cur.execute(command)
					except sqlite3.IntegrityError as ie:
						Logger.ErrorLogMessage(ie,"rekord z daty {0} istnieje już w bazie danych!".format(time1[j]))
					except Exception as ex:
						Logger.ErrorLog(ex)
						Logger.QuitProgram()
	
		# KOLEJNOSC: MEAN_CORRECT, MEAN_INCORRECT, RMS_CORRECT, RMS_INCORRECT
	
	
	
	

	def AnalyzeData(self, sensorsdata, time1):
		sensors = sensorsdata
		equations = self.AnalyzeAndLog(sensors, time1)
		self.SaveEquationsToDb(sensorsdata,equations)
		self.CreateXml(equations)
	
	
	

	def SaveEquationsToDb(self, sensorsdata, equations):
		sensors = sensorsdata
		con = sqlite3.connect(Paths.DirDataDB)
		with con:
			cur = con.cursor()
			for i in range(SensorsSettings.SensorsCount):
				try:
					command = "INSERT INTO EQUATIONS VALUES({0},{1},{2},{3},{4},{5},{6},{7},{8})".format(i,equations[i][0][2][0],equations[i][0][2][1],equations[i][1][2][0],equations[i][1][2][1],equations[i][2][2][0],equations[i][2][2][1],equations[i][3][2][0],equations[i][3][2][1])
					cur.execute(command)
				except sqlite3.IntegrityError as ie:
					Logger.ErrorLogMessage(ie,"rekord dla sensora {0} istnieje już w bazie danych!".format(i))
				except Exception as ex:
					Logger.ErrorLog(ex)
					Logger.QuitProgram()
	
	
	
	def CreateXml(self, equations):
		root = etree.Element('Sensors')
		doc = etree.ElementTree(root)
		for i in equations.keys():
			sensor = etree.SubElement(root, 'Sensor', ID=str(i))
			mean = etree.SubElement(sensor, 'MEAN')
			rms = etree.SubElement(sensor, 'RMS')
			for j in range(4):
				eq_mean = etree.SubElement(mean, "Rownanie"+str(j), A=str(equations[i][j][2][0]), B=str(equations[i][j][2][1])) 
				#eq_mean.text = 'y={0}x+({1})'.format(equations[i][j][2][0],equations[i][j][2][1])
				eq_rms = etree.SubElement(rms, "Rownanie"+str(j), A=str(equations[i][j+4][2][0]), B=str(equations[i][j+4][2][1])) 
				#eq_rms.text = 'y={0}x+({1})'.format(equations[i][j+4][2][0],equations[i][j+4][2][1])
	
		doc.write(Paths.DirDataLogsEquations, xml_declaration=True, encoding='utf-8', pretty_print=True)
	
	
	
	
	def GetEquationsFromXML(self):
		equations = {i:[[],[],[],[],[],[],[],[]] for i in range(SensorsSettings.SensorsCount)}
		sensors = etree.parse(Paths.DirDataLogsEquations)
		root = sensors.getroot()
		for sensor in root.getchildren():
			for sensorchild in sensor.getchildren():
				rownania =  sensorchild.getchildren()
				if(sensorchild.tag == "MEAN"):
					equations[int(sensor.attrib["ID"])][0].extend([rownania[0].attrib["A"],rownania[0].attrib["B"]])
					equations[int(sensor.attrib["ID"])][1].extend([rownania[1].attrib["A"],rownania[1].attrib["B"]])
					equations[int(sensor.attrib["ID"])][2].extend([rownania[2].attrib["A"],rownania[2].attrib["B"]])
					equations[int(sensor.attrib["ID"])][3].extend([rownania[3].attrib["A"],rownania[3].attrib["B"]])
				else:
					equations[int(sensor.attrib["ID"])][4].extend([rownania[0].attrib["A"],rownania[0].attrib["B"]])
					equations[int(sensor.attrib["ID"])][5].extend([rownania[1].attrib["A"],rownania[1].attrib["B"]])
					equations[int(sensor.attrib["ID"])][6].extend([rownania[2].attrib["A"],rownania[2].attrib["B"]])
					equations[int(sensor.attrib["ID"])][7].extend([rownania[3].attrib["A"],rownania[3].attrib["B"]])
	
		return equations
	
	
	
	def AnalyzeAndLog(self, sensors,time_):
		Logger.StartAnalizeLog()
		equations = {i:[[],[],[],[],[],[],[],[]] for i in range(SensorsSettings.SensorsCount)}
		for sensor in sensors:
			########################## OBLICZENIA LINII TRENDU DLA MEAN
			########################## ##########################
			print "SENSOR NUMER " + str(sensor)
			if sensors[sensor]["mean"]:
				number_of_errors = 0
				kopia_sensor_mean = []
				kopia_sensor_rms = []
				kopia_time = []
				std = np.std(sensors[sensor]["mean"])
				meanofmean = np.mean(sensors[sensor]["mean"])
				print "\tPierwsza analiza parametru mean"
				for i in range(len(sensors[sensor]["mean"])):
					if (2 * std < abs(sensors[sensor]["mean"][i] - meanofmean)):
						number_of_errors +=1
						print "\t\tWartosc uznana za bledna: " + str(sensors[sensor]["mean"][i]) + " dla pomiaru o dacie: " + str(time_[i])
					else:
						kopia_sensor_mean.append(sensors[sensor]["mean"][i])
						kopia_time.append(time_[i])
				print "\t\tDla sensora numer " + str(sensor) + " ilosc wykrytych bledow wynosi " + str(number_of_errors)
				equations[sensor][2] = self.__AnalyzeOnceMoreMean(sensor,kopia_sensor_mean,kopia_time)
				
				kopia_time = mdates.date2num(kopia_time)
				
				z = np.polyfit(kopia_time,kopia_sensor_mean,1)
				p = np.poly1d(z)
				equations[sensor][1] = (kopia_time,p,z)
				
				time_mean = mdates.date2num(time_)
				
				z = np.polyfit(time_mean,sensors[sensor]["mean"],1)
				p = np.poly1d(z)
				equations[sensor][0] = (time_mean,p,z)
				
				z = np.polyfit(time_mean[-SensorsSettings.LastMeasurementsNumber:],sensors[sensor]["mean"][-SensorsSettings.LastMeasurementsNumber:],1)
				p = np.poly1d(z)
				equations[sensor][3] = (time_mean,p,z)
				print("\tRownanie linii trendu parematru mean przed analiza: y=%.4fx+(%.f)" % (equations[sensor][0][2][0],equations[sensor][0][2][1]))
				print("\tRownanie linii trendu parematru mean po wstepnej analizie: y=%.4fx+(%.f)" % (equations[sensor][1][2][0],equations[sensor][1][2][1]))
				print("\tRownanie linii trendu parematru mean po koncowej analizie: y=%.4fx+(%.f)" % (equations[sensor][2][2][0],equations[sensor][2][2][1]))
				print("\tRownanie linii trendu parematru mean dla ostatnich 10 wartosci: y=%.4fx+(%.f)" % (equations[sensor][3][2][0],equations[sensor][3][2][1]))
				print ("\n")
			########################## OBLICZENIA LINII TRENDU DLA RMS
			########################## ########################## Nie zmienione nazwy
			########################## zmiennych, porpawic dla lepszej czytelnosc
			if sensors[sensor]["rms"]:
				number_of_errors = 0
				kopia_sensor_mean = []
				kopia_sensor_rms = []
				kopia_time = []
				std = np.std(sensors[sensor]["rms"])
				meanofmean = np.mean(sensors[sensor]["rms"])
				print "\tPierwsza analiza parametru rms"
				for i in range(len(sensors[sensor]["rms"])):
					if (2 * std < abs(sensors[sensor]["rms"][i] - meanofmean)):
						number_of_errors +=1
						print "\t\tWartosc uznana za bledna: " + str(sensors[sensor]["rms"][i]) + " dla pomiaru o dacie: " + str(time_[i])
					else:
						kopia_sensor_mean.append(sensors[sensor]["rms"][i])
						kopia_time.append(time_[i])
				print "\t\tDla sensora numer " + str(sensor) + " ilosc wykrytych bledow wynosi " + str(number_of_errors)
				equations[sensor][6] = self.__AnalyzeOnceMoreRms(sensor,kopia_sensor_mean,kopia_time)
				
				kopia_time = mdates.date2num(kopia_time)
				
				z = np.polyfit(kopia_time,kopia_sensor_mean,1)
				p = np.poly1d(z)
				equations[sensor][5] = (kopia_time,p,z)
				
				time_rms = mdates.date2num(time_)
				
				z = np.polyfit(time_rms,sensors[sensor]["rms"],1)
				p = np.poly1d(z)
				equations[sensor][4] = (time_rms,p,z)
				
				z = np.polyfit(time_mean[-SensorsSettings.LastMeasurementsNumber:],sensors[sensor]["rms"][-SensorsSettings.LastMeasurementsNumber:],1)
				p = np.poly1d(z)
				equations[sensor][7] = (time_mean,p,z)
				print("\tRownanie linii trendu parematru rms przed analiza: y=%.4fx+(%.f)" % (equations[sensor][4][2][0],equations[sensor][4][2][1]))
				print("\tRownanie linii trendu parematru rms po wstepnej analizie: y=%.4fx+(%.f)" % (equations[sensor][5][2][0],equations[sensor][5][2][1]))
				print("\tRownanie linii trendu parematru rms po koncowej analizie: y=%.4fx+(%.f)" % (equations[sensor][6][2][0],equations[sensor][6][2][1]))
				print("\tRownanie linii trendu parematru rms dla ostatnich 10 wartosci: y=%.4fx+(%.f)" % (equations[sensor][7][2][0],equations[sensor][7][2][1]))
				print ("\n")
		Logger.StopAnalizeLog()
		return equations
	
	
	
	def __AnalyzeOnceMoreMean(self, numer_sensora,sensor_mean,time_):
		number_of_errors = 0
		kopia_sensor_mean = []
		kopia_time = []
		rms = np.sqrt(np.mean(np.square(sensor_mean)))
		meanofmean = np.mean(sensor_mean)
		print "\tDruga analiza parametru mean"
		for i in range(len(sensor_mean)):
			if (abs(2 * rms - meanofmean) < abs(sensor_mean[i] - meanofmean)):
				number_of_errors +=1
				print "\t\tWartosc uznana za bledna: " + str(sensor_mean[i]) + " dla pomiaru o dacie: " + str(time_[i])
			else:
				kopia_sensor_mean.append(sensor_mean[i])
				kopia_time.append(time_[i])
		print "\t\tDla sensora numer " + str(numer_sensora) + " ilosc dodatkowych bledow po drugiej analizie wynosi " + str(number_of_errors)
		kopia_time = mdates.date2num(kopia_time)
		z = np.polyfit(kopia_time,kopia_sensor_mean,1)
		p = np.poly1d(z)
		return (kopia_time,p,z)
	
	
	
	def __AnalyzeOnceMoreRms(self, numer_sensora,sensor_rms,time_):
		number_of_errors = 0
		kopia_sensor_rms = []
		kopia_time = []
		rms = np.sqrt(np.mean(np.square(sensor_rms)))
		meanofmean = np.mean(sensor_rms)
		print "\tDruga analiza parametru rms"
		for i in range(len(sensor_rms)):
			if (abs(2 * rms - meanofmean) < abs(sensor_rms[i] - meanofmean)):
				number_of_errors +=1
				print "\t\tWartosc uznana za bledna: " + str(sensor_rms[i]) + " dla pomiaru o dacie: " + str(time_[i])
			else:
				kopia_sensor_rms.append(sensor_rms[i])
				kopia_time.append(time_[i])
		print "\t\tDla sensora numer " + str(numer_sensora) + " ilosc dodatkowych bledow po drugiej analizie wynosi " + str(number_of_errors)
		kopia_time = mdates.date2num(kopia_time)
		z = np.polyfit(kopia_time,kopia_sensor_rms,1)
		p = np.poly1d(z)
		return (kopia_time,p,z)
	
	
	
	def __GetTrendLine(self, sensors,time_):
		equations = {i:{"mean":[[],[],[]] , "rms":[[],[],[]]} for i in range(SensorsSettings.SensorsCount)}
		for sensor in sensors:
			if sensors[sensor]["mean"]:
				number_of_errors = 0
				kopia_sensor_mean = []
				kopia_time = []
				std = np.std(sensors[sensor]["mean"])
				meanofmean = np.mean(sensors[sensor]["mean"])
				for i in range(len(sensors[sensor]["mean"])):
					if (2 * std < abs(sensors[sensor]["mean"][i] - meanofmean)):
						number_of_errors +=1
					else:
						kopia_sensor_mean.append(sensors[sensor]["mean"][i])
						kopia_time.append(time_[i])
				equations[sensor]["mean"][2] = self.__GetSecondTrendLineMean(sensor,kopia_sensor_mean,kopia_time)
				kopia_time = mdates.date2num(kopia_time)
				z = np.polyfit(kopia_time,kopia_sensor_mean,1)
				p = np.poly1d(z)
				equations[sensor]["mean"][1] = (kopia_time,p,z)
				time_mean = mdates.date2num(time_)
				z = np.polyfit(time_mean,sensors[sensor]["mean"],1)
				p = np.poly1d(z)
				equations[sensor]["mean"][0] = (time_mean,p,z)
	
			if sensors[sensor]["rms"]:
				number_of_errors = 0
				kopia_sensor_rms = []
				kopia_time = []
				std = np.std(sensors[sensor]["rms"])
				meanofmean = np.mean(sensors[sensor]["rms"])
				for i in range(len(sensors[sensor]["rms"])):
					if (2 * std < abs(sensors[sensor]["rms"][i] - meanofmean)):
						number_of_errors +=1
					else:
						kopia_sensor_rms.append(sensors[sensor]["rms"][i])
						kopia_time.append(time_[i])
				equations[sensor]["rms"][2] = self.__GetSecondTrendLineRMS(sensor,kopia_sensor_rms,kopia_time)
				kopia_time = mdates.date2num(kopia_time)
				z = np.polyfit(kopia_time,kopia_sensor_rms,1)
				p = np.poly1d(z)
				equations[sensor]["rms"][1] = (kopia_time,p,z)
				time_rms = mdates.date2num(time_)
				z = np.polyfit(time_rms,sensors[sensor]["rms"],1)
				p = np.poly1d(z)
				equations[sensor]["rms"][0] = (time_rms,p,z)
		return equations
	


	def __GetSecondTrendLineMean(self, numer_sensora,sensor_mean,time_):
		number_of_errors = 0
		kopia_sensor_mean = []
		kopia_time = []
		rms = np.sqrt(np.mean(np.square(sensor_mean)))
		meanofmean = np.mean(sensor_mean)
		for i in range(len(sensor_mean)):
			if (abs(2 * rms - meanofmean) < abs(sensor_mean[i] - meanofmean)):
				number_of_errors +=1
			else:
				kopia_sensor_mean.append(sensor_mean[i])
				kopia_time.append(time_[i])
		kopia_time = mdates.date2num(kopia_time)
		z = np.polyfit(kopia_time,kopia_sensor_mean,1)
		p = np.poly1d(z)
		return (kopia_time,p,z)
	


	def __GetSecondTrendLineRMS(self, numer_sensora,sensor_rms,time_):
		number_of_errors = 0
		kopia_sensor_rms = []
		kopia_time = []
		rms = np.sqrt(np.mean(np.square(sensor_rms)))
		meanofmean = np.mean(sensor_rms)
		for i in range(len(sensor_rms)):
			if (abs(2 * rms - meanofmean) < abs(sensor_rms[i] - meanofmean)):
				number_of_errors +=1
			else:
				kopia_sensor_rms.append(sensor_rms[i])
				kopia_time.append(time_[i])
		kopia_time = mdates.date2num(kopia_time)
		z = np.polyfit(kopia_time,kopia_sensor_rms,1)
		p = np.poly1d(z)
		return (kopia_time,p,z)












### Funkcja pobiera ze sciezki "readpath" wszystkie pliki wygenerowane przez skrypt preprocessData.cxx
### oraz zapisuje je do katalogu "savepathtxt" tworzac zaleznosc czasowa dla kazdego sensora.
### Parametr sensors_count mowi o tym ile sensorow chcemy analizowac
###def PrepareSensorData_OBSOLETE(readpath, savepathtxt, sensors_count):
###	content_list = [file_ for file_ in os.listdir(readpath) if file_.endswith(".dat")] #pobranie listy plikow
###	content_list = sorted(content_list) # sortowanie po dacie
###	sensors = {i:{"mean":[],"rms":[],"skewness":[],"curtosis":[]} for i in range(sensors_count)} # utworzenie slownika. Klucz to numer sensora, zas wartosci to podslowniki z konkretnymi parametrami
###	for con in content_list: 
###		from_sensors = np.loadtxt(readpath + con, delimiter=",") # Pobranie parametrow sensorow z konkretnego dnia
###		for i in range(sensors_count): 
###			sensors[i]["mean"].append(float(from_sensors[i][0]))
###			sensors[i]["rms"].append(float(from_sensors[i][1]))
###			sensors[i]["skewness"].append(float(from_sensors[i][2]))
###			sensors[i]["curtosis"].append(float(from_sensors[i][3]))
###
###	result = [[] for i in range(sensors_count)] # tablica zawierajaca jawna zaleznosc czasowa parametrow kazdego sensora 
###	for sensor in sensors:
###		for i in range(len(sensors[sensor]["mean"])):
###			result[sensor].append([sensors[sensor]["mean"][i],sensors[sensor]["rms"][i],sensors[sensor]["skewness"][i],sensors[sensor]["curtosis"][i]])
###
###	for i in range(len(result)):
###		np.savetxt(savepathtxt + "Sensor_" + (str(i) if i <10 else "0"+str(i)) + ".dat", result[i], delimiter=",", fmt='%.7f', newline='\n')
	






### Funkcja tworzy i zwraca zmienna trzymajaca w sobie informaje o parametrach sensorow (zaleznosc czasowa)
### 
### 
###def GetSensorData_OBSOLETE(readpath, sensors_count):
###	
###	content_list = [file_ for file_ in os.listdir(readpath) if (file_.startswith("Sensor") and file_.endswith(".dat"))] #pobranie listy plikow
###	content_list = sorted(content_list) # 
###	sensors = {i:{"mean":[],"rms":[],"skewness":[],"curtosis":[]} for i in range(sensors_count)} # utworzenie slownika. Klucz to numer sensora, zas wartosci to podslowniki z konkretnymi parametrami
###	for i in range(len(content_list)): 
###		from_sensors = np.loadtxt(readpath + content_list[i], delimiter=",") # Pobranie parametrow sensorow z konkretnego dnia
###		for table in from_sensors:
###			sensors[i]["mean"].append(float(table[0]))
###			sensors[i]["rms"].append(float(table[1]))
###			sensors[i]["skewness"].append(float(table[2]))
###			sensors[i]["curtosis"].append(float(table[3]))
###
###	return sensors



### Funkcja pobiera ze sciezki "readpath" wszystkie pliki wygenerowane przez skrypt preprocessData.cxx
### oraz zapisuje je do katalogu "savepathtxt" tworzac zaleznosc czasowa dla kazdego sensora.
### Parametr sensors_count mowi o tym ile sensorow chcemy analizowac
#def DrawCharts_OBSOLETE(savepath, readpathtxt, sensorsdata, sensors_count):
#	time1 = []
#	file1 = open(DIR + "Data\\" + "TIME_LIST.txt", "r")
#	lines = file1.readlines() # Pobiera liste wszystkich plikow, z ktorych wczytywane byly dane. Pliki te maja w nazwie date
#	for line in lines:
#		time1.append(line[-29:-10])
#		time1[-1] = datetime.datetime(int(time1[-1][0:4]),int(time1[-1][5:7]),int(time1[-1][8:10]),int(time1[-1][11:13]),int(time1[-1][14:16]),int(time1[-1][17:19]))
#	file1.close()
#	time1 = sorted(time1)
#
#
#	sensors = sensorsdata
#
#	equations = GetTrendLine(sensors, time1, sensors_count)
#
#	for sensor in range(sensors_count):
#		plt.plot(time1,sensors[sensor]["mean"],"-bo")
#		plt.plot(equations[sensor]["mean"][0][0],equations[sensor]["mean"][0][1](equations[sensor]["mean"][0][0]),'g--', label = "First y=%.4fx+(%.f)" % (equations[sensor]["mean"][0][2][0],equations[sensor]["mean"][0][2][1])) # Z BLEDAMI
#		plt.legend(loc='best')
#		plt.plot(equations[sensor]["mean"][2][0],equations[sensor]["mean"][2][1](equations[sensor]["mean"][2][0]),'r--', label = "Second y=%.4fx+(%.f)" % (equations[sensor]["mean"][2][2][0],equations[sensor]["mean"][2][2][1])) # BEZ BLEDOW
#		plt.legend(loc='best')
#		plt.gcf().autofmt_xdate()
#		plt.savefig(savepath+"Sensor_"+str(sensor)+"_"+"mean")
#		plt.close()
#		plt.hist(sensors[sensor]["mean"],bins = 20)
#		plt.savefig(savepath+"Histogram_Sensor_"+str(sensor)+"_"+"mean")
#		plt.close()
#	
#		plt.plot(time1,sensors[sensor]["rms"],"-bo")
#		plt.plot(equations[sensor]["rms"][0][0],equations[sensor]["rms"][0][1](equations[sensor]["rms"][0][0]),'g--', label = "First y=%.4fx+(%.f)" % (equations[sensor]["rms"][0][2][0],equations[sensor]["rms"][0][2][1])) # Z BLEDAMI
#		plt.legend(loc='best')
#		plt.plot(equations[sensor]["rms"][2][0],equations[sensor]["rms"][2][1](equations[sensor]["rms"][2][0]),'r--', label = "Second y=%.4fx+(%.f)" % (equations[sensor]["rms"][2][2][0],equations[sensor]["rms"][2][2][1])) # BEZ BLEDOW
#		plt.legend(loc='best')
#		plt.gcf().autofmt_xdate()
#		plt.savefig(savepath + "Sensor_" + str(sensor) + "_" + "rms")
#		plt.close()
#		plt.hist(sensors[sensor]["rms"])
#		plt.savefig(savepath+"Histogram_Sensor_"+str(sensor)+"_"+"rms")
#		plt.close()
#		
#		plt.plot(time1,sensors[sensor]["skewness"],"-bo")
#		plt.gcf().autofmt_xdate()
#		plt.savefig(savepath+"Sensor_"+str(sensor)+"_"+"skewness")
#		plt.close()
#		plt.hist(sensors[sensor]["skewness"])
#		plt.savefig(savepath+"Histogram_Sensor_"+str(sensor)+"_"+"skewness")
#		plt.close()
#	
#		plt.plot(time1,sensors[sensor]["curtosis"],"-bo")
#		plt.gcf().autofmt_xdate()
#		plt.savefig(savepath+"Sensor_"+str(sensor)+"_"+"curtosis")
#		plt.close()
#		plt.hist(sensors[sensor]["curtosis"])
#		plt.savefig(savepath+"Histogram_Sensor_"+str(sensor)+"_"+"curtosis")
#		plt.close()






