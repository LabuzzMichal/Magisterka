# -*- coding: utf-8 -*-

import numpy as np
import random
import sqlite3 
from Configuration import Paths
from Logger import Logger

class FakeData(object):
	"""Generates simulated bad-quality sensor data"""

	def GenerateFakeData(self,sensorid,p_value_list, samples, append=False):
		"""
		Generates simulated bad-quality sensor data (parameters in feature space) based on good-quality real sensor data.
		It is done by departing from good-quality sensor params TO SOME EXTENT
	
		=======
		params:
		sourcepath - points to the file with feature-space parameters and class; one row per sensor
		fake_data_path - output path for the fake data
		samples - number of fake samples to be created
		append - whether to append or overwrite the output file with fake data
		p_value_list - ??
		"""
	
		# load original (real) sensor data (42 samples)
		from_sensors = self.__GetSensorData(sensorid)
		# TU POPRAWIC
		# calculate mean and std. dev. among all rows for each parameter
		average_list = from_sensors["mean"]
		average_par = (np.average(average_list),np.std(average_list))
		rms_list = from_sensors["rms"]
		rms_par = (np.average(rms_list),np.std(rms_list))
		skewness_list = from_sensors["skewness"]
		skewness_par = (np.average(skewness_list),np.std(skewness_list))
		kurtosis_list = from_sensors["curtosis"]
		kurtosis_par = (np.average(kurtosis_list),np.std(kurtosis_list)) 
	
		# simulate bad quality sensors by randomly departing from good quality sensor parameters
		# each parameter x gets mean_x +/- p * stddev_x, where p is from (p_value_list[i][0], p_value_list[i][1]) range
		result = []
		for i in range(samples):
			random_data = [average_par[0] + random.choice([1,-1]) * random.uniform(p_value_list[0][0] * average_par[1], p_value_list[0][1] * average_par[1]),
						   rms_par[0] + random.choice([1,-1]) * random.uniform(p_value_list[1][0]*rms_par[1],p_value_list[1][1]*rms_par[1]),
						   skewness_par[0] + random.choice([1,-1]) * random.uniform(p_value_list[2][0]*skewness_par[1],p_value_list[2][1]*skewness_par[1]),
						   kurtosis_par[0] + random.choice([1,-1]) * random.uniform(p_value_list[3][0]*kurtosis_par[1],p_value_list[3][1]*kurtosis_par[1]),
						   0]
			result.append(random_data)
	
		# save result to output file (either append or overwrite)
		# write mode
		if append:
			self.__SaveFakedData(result,sensorid)
		else:
			self.__DeletePreviousFakeData(sensorid)
			self.__SaveFakedData(result,sensorid)
	
	
	
	def __DeletePreviousFakeData(self,sensorid):
		try:
			conn = sqlite3.connect(Paths.DirDataDB)
			c = conn.cursor()
			command = "DELETE FROM FAKE_DATA WHERE SENSORID={0}".format(int(sensorid))
			c.execute(command)
			conn.commit() 
			c.close()
		except Exception as ex:
			Logger.ErrorLog(ex)
	
	
	def __GetSensorData(self,sensorid):
		conn = sqlite3.connect(Paths.DirDataDB)
		c = conn.cursor()
		sensor = {"mean":[],"rms":[],"skewness":[],"curtosis":[]} 
		sensornumer = str(sensorid) if sensorid > 9 else "0"+str(sensorid)
		command = "SELECT MEAN, RMS, CURTOSIS, SKEWNESS FROM DATA_SENSOR_{0} WHERE IS_ACCEPTED_FLAG=1 ORDER BY TIME".format(sensornumer)
		for row in c.execute(command):
			sensor["mean"].append(float(row[0]))
			sensor["rms"].append(float(row[1]))
			sensor["curtosis"].append(float(row[2]))	
			sensor["skewness"].append(float(row[3]))
		return sensor	
	
	
	def __SaveFakedData(self,sensorsfakedata,sensorid):
		fakedata = sensorsfakedata
	
		con = sqlite3.connect(Paths.DirDataDB)
		with con:
			cur = con.cursor()
			for i in range(len(fakedata)):
				command = "INSERT INTO FAKE_DATA VALUES({0},'0',{1},{2},{3},{4},0)".format(sensorid,fakedata[i][0],fakedata[i][1],fakedata[i][2],fakedata[i][3])
				cur.execute(command)
	# ORDER: MEAN_CORRECT, MEAN_INCORRECT, RMS_CORRECT, RMS_INCORRECT