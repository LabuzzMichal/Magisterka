#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lxml.etree as ET
from Configuration import *
from DataManager import DataManager
from FakeData import FakeData
from Classifier import KNN
from XMLConfiguration import XMLConfiguration
from Logger import Logger




try:
	paths = Paths()
	knnsettings = KNNSettings()
	sensorssettings = SensorsSettings()
	projectedsettings = ProjectSettings()
	mainsettings = MainSettings()
	Logger.InfoLog("Configuration classes iniziatized without error")
except Exception as e:
	Logger.InfoLog("Configuration classes initialized with errors")                                 
	Logger.ErrorLogMessage(e,"Some error found in Configuration.XML")
	Logger.QuitProgram()



if mainsettings.CreateDB:
	dataManager = DataManager()
	dataManager.PrepareSensorData()

if mainsettings.UpdateDBWithNewData:
	dataManager = DataManager()
	dataManager.PrepareSensorNewData()
	newsensors = dataManager.GetNewSensorData(timefrom = None, timeto = None)
	newtime = DataManager.GetTimeList(newdata = True, db = True,timefrom = None, timeto = None)
	dataManager.SaveProjectedData(newsensors,newtime)

if mainsettings.DrawCharts:
	dataManager = DataManager()
	sensors = dataManager.GetSensorData(timefrom = mainsettings.DrawChartsTimeFrom, timeto = mainsettings.DrawChartsTimeTo)
	time = GetTimeList(timefrom = mainsettings.DrawChartsTimeFrom, timeto = mainsettings.DrawChartsTimeTo)
	dataManager.DrawCharts(sensors,time)

if mainsettings.DrawProjectedCharts:
	dataManager = DataManager()
	projectedsensors = dataManager.GetProjectedSensorData(timefrom = mainsettings.DrawProjectedChartsTimeFrom, timeto = mainsettings.DrawProjectedChartsTimeTo)
	time = GetTimeList(timefrom = mainsettings.DrawProjectedChartsTimeFrom, timeto = mainsettings.DrawProjectedChartsTimeTo)
	dataManager.DrawProjectedCharts(projectedsensors,time)

if mainsettings.Analyze:
	dataManager = DataManager()	
	sensors = dataManager.GetSensorData(timefrom = mainsettings.AnalyzeTimeFrom, timeto = mainsettings.AnalyzeTimeTo)
	time = GetTimeList(timefrom = mainsettings.AnalyzeTimeFrom, timeto = mainsettings.AnalyzeTimeTo)
	dataManager.AnalyzeAndLog(sensors,time)

if mainsettings.Classifier:
	dataManager = DataManager()	
	sensors = dataManager.GetSensorData(timefrom = mainsettings.ClassifierTimeFrom, timeto = mainsettings.ClassifierTimeTo)
	time = GetTimeList(timefrom = mainsettings.ClassifierTimeFrom, timeto = mainsettings.ClassifierTimeTo)
	if MainSettings.ClassifierGenerateFakeData:
		fakeData = FakeData()
		rangelist = [[MainSettings.ClassifierFakeDataMinMultiplier,MainSettings.ClassifierFakeDataMaxMultiplier] for i in range(4)]
		for i in range(SensorsSettings.SensorsCount):
			fakeData.GenerateFakeData(sensorid=i, p_value_list = rangelist, samples = MainSettings.ClassifierGenerateFakeDataSamples)
	for i in range(SensorsSettings.SensorsCount):
		sensornumer = str(i) if i > 9 else "0"+str(i)
		classifier = KNN(sensornumer)
		classifier.ChooseParameters(MainSettings.ClassifierParameters["time"],MainSettings.ClassifierParameters["mean"],MainSettings.ClassifierParameters["rms"],MainSettings.ClassifierParameters["skewness"],MainSettings.ClassifierParameters["curtosis"])
		classifier.TrainAndPredict(KNNSettings.n_neighbors, KNNSettings.weights, KNNSettings.metric, KNNSettings.algorithm)
