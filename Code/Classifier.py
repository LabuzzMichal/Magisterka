# -*- coding: utf-8 -*-



import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
import sqlite3
from Configuration import Paths, SensorsSettings
from Logger import Logger





class KNN():
	def __init__(self, sensorstringid, timefrom = None, timeto = None):
		"""
		Read the data used for training algorithm and for prediction
		=======
		params:
		sensorstringid
		
		"""

		self.predict_data = self.__GetPredictSensorData(sensorstringid)
		good_data = self.__GetTrainSensorData(sensorstringid, timefrom, timeto) 
		fake_data = self.__GetFakeSensorData(sensorstringid)


		self.train_data = good_data + fake_data 
		
		self.predict_data = np.array(self.predict_data)
		self.train_data = np.array(self.train_data)

	def ChooseParameters(self,timestep = True, mean = True, rms = True, skewness = True, curtosis = True):
		counter = 0
		
		if timestep is True:
			#newcol = np.array([i for i in range(len(self.train_data))])
			#self.train_data = np.insert(self.train_data,0,newcol, axis=1).
			pass
		else:
			pass

		if mean is True:
			pass
		else:		
			self.train_data = np.delete(self.train_data,0+counter, axis=1)
			counter+=1

		if rms is True:
			pass
		else:
			self.train_data = np.delete(self.train_data,1-counter, axis=1)
			counter+=1

		if skewness is True:
			pass
		else:
			self.train_data = np.delete(self.train_data,2-counter, axis=1)
			counter+=1

		if curtosis is True:
			pass
		else:
			self.train_data = np.delete(self.train_data,3-counter, axis=1)
			counter+=1

		return

	def TrainAndPredict(self, k=4, weights='distance', metric='minkowski', algorithm='auto'):
		"""
		Trains k-nearest neighbours classifier with sensor and simulated (fake) data and checks accuracy of the classifier
		by comparing its predictions with test samples in two ways: directly and using cross-validation
		
		=======
		params:
		k - number of neighbours
		train_test_ratio - specifies how many samples use for training the algorithm and how many for testing its accuracy
		weights - pertains to data points (NOT to the attributes!); the closer ones may be regarded as more important (weights='distance');
				  possible weights: 'uniform', 'distance', [callable].
				  The [callable] is a user-defined function
		algorithm - 'auto'; shan't be changed in this little project
		metric - e.g. 'minkowski' or 'euclidean' or 'mahalanobis' tells the algorithm how to measure the distance
		"""
		
		
		traindata = self.train_data[:, :-1]
		targetvalues = [self.train_data[i][-1] for i in range(len(self.train_data))] # array of 0/1

		
		# build a classifier and teach it
		self.neigh = KNeighborsClassifier(n_neighbors=k, weights=weights, algorithm=algorithm, metric=metric)
		self.neigh.fit(traindata, targetvalues)
		
		# check accuracy with cross-validation
		cv = cross_validation.ShuffleSplit(len(targetvalues), n_iter=10, test_size=10, random_state=0)
		self.knn_score = cross_validation.cross_val_score(self.neigh, traindata, targetvalues, cv=cv)
		
		# summarise all test data (predictions)
		Logger.StartClassifierLog()
		print "------All params @: {"
		print "n_neighbors: " + str(k) + "  weights: " + str(weights) + "  metric: "+str(metric) + "  algorithm: "+str(algorithm) + " }"
		print "Sensor data prediction: (1 = good, 0 = bad)" + str(self.neigh.predict(self.predict_data))
		print "Fake data prediction:" + str(self.neigh.predict(self.train_data[:, :-1])) 
		print "Probability of correct assessment (sensor data):"
		print "[1st column: bad | 2nd column: good]"
		print str(self.neigh.predict_proba(self.predict_data))
		print "Probability of correct assessment (fake data): \n" + str(self.neigh.predict_proba(self.train_data[:, :-1]))
		Logger.StopClassifierLog()



	def __GetPredictSensorData(self, sensorstringid):
		conn = sqlite3.connect(Paths.DirDataDB)
		c = conn.cursor()
		sensor = {"mean":[],"rms":[],"skewness":[],"curtosis":[], "rate":[]} 
		command = "SELECT MEAN, RMS, CURTOSIS, SKEWNESS FROM DATA_SENSOR_{0} WHERE IS_ACCEPTED_FLAG=-1 ORDER BY TIME".format(sensorstringid)
		for row in c.execute(command):
			sensor["mean"].append(float(row[0]))
			sensor["rms"].append(float(row[1]))
			sensor["curtosis"].append(float(row[2]))	
			sensor["skewness"].append(float(row[3]))
		sensors = []
		for i in range(len(sensor["mean"])):
			sensors.append([sensor["mean"][i],sensor["rms"][i],sensor["curtosis"][i],sensor["skewness"][i]])
		return sensors	



	def __GetTrainSensorData(self,sensorstringid, timefrom = None, timeto = None):
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
				Logger.QuitProgram()

		conn = sqlite3.connect(Paths.DirDataDB)
		c = conn.cursor()
		sensor = {"mean":[],"rms":[],"skewness":[],"curtosis":[], "rate":[]} 
		command = ""
		if flag:
			command = "SELECT * FROM (SELECT MEAN, RMS, CURTOSIS, SKEWNESS, RATE, TIME FROM DATA_SENSOR_{0} WHERE IS_ACCEPTED_FLAG=1 ORDER BY TIME desc LIMIT {1}) ORDER BY TIME".format(sensorstringid, SensorsSettings.TrainUsingLastNMeasurements)
		else:
			command = "SELECT MEAN, RMS, CURTOSIS, SKEWNESS, RATE, TIME FROM DATA_SENSOR_{0} WHERE TIME BETWEEN date('{1}') AND date('{2}') AND IS_ACCEPTED_FLAG=1 ORDER BY TIME".format(sensorstringid,timefrom, timeto)
		try:
			execute = c.execute(command)
		except Exception as ex:
			Logger.ErrorLog(ex)
			Logger.QuitProgram()
		for row in c.execute(command):
			sensor["mean"].append(float(row[0]))
			sensor["rms"].append(float(row[1]))
			sensor["curtosis"].append(float(row[2]))	
			sensor["skewness"].append(float(row[3]))
			sensor["rate"].append(float(row[4]))

		sensors = []
		for i in range(len(sensor["mean"])):
			sensors.append([sensor["mean"][i],sensor["rms"][i],sensor["curtosis"][i],sensor["skewness"][i],sensor["rate"][i]])
		return sensors	



	def __GetFakeSensorData(self,sensorstringid):
		conn = sqlite3.connect(Paths.DirDataDB)
		c = conn.cursor()
		sensor = {"mean":[],"rms":[],"skewness":[],"curtosis":[]} 
		command = "SELECT MEAN, RMS, CURTOSIS, SKEWNESS FROM FAKE_DATA WHERE SENSORID={0}".format(int(sensorstringid))
		for row in c.execute(command):
			sensor["mean"].append(float(row[0]))
			sensor["rms"].append(float(row[1]))
			sensor["curtosis"].append(float(row[2]))	
			sensor["skewness"].append(float(row[3]))
			sensor["rate"].append(0)#UWAGA!
		sensors = []
		for i in range(len(sensor["mean"])):
			sensors.append([sensor["mean"][i],sensor["rms"][i],sensor["curtosis"][i],sensor["skewness"][i],sensor["rate"][i]])
		return sensors	

