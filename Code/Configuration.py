# -*- coding: utf-8 -*-


from XMLConfiguration import XMLConfiguration
import lxml.etree as ET

class Paths(XMLConfiguration):
	"""This class keeps information about environmental variables and directories"""

	Dir = "dsadsa" # Have to be defined!
	DirData = Dir + "Data\\" # Have to be defined!
	DirDataDB = DirData + "TEST.db" # Have to be defined!
	DirDataLogs = DirData + "Logs\\" # Have to be defined!
	DirDataLogsErrors = DirDataLogs + "Errors\\" # Have to be defined!
	DirDataLogsClassifier = DirDataLogs + "Classifier\\" # Have to be defined!
	DirDataLogsAnalize = DirDataLogs + "Analize\\" # Have to be defined!
	DirDataLogsEquations = DirDataLogs + "equations.xml" # Have to be defined!
	DirDataSensorsNewData = DirData + "Sensors_newdata\\" # Have to be defined!
	DirDataSensorsPreprocess = DirData + "Sensors_preprocess\\" # Have to be defined!
	DirDataProjectedSensors = DirData + "Sensors_projected\\" # Have to be defined!
	DirFig = Dir + "Fig\\" # Have to be defined!
	DirFigSensors = DirFig + "Sensors\\" # Have to be defined!
	DirFigProjectedSensors = DirFig + "Sensors_projected\\" # Have to be defined!
	DirDataXML = "C:\\Users\\Michal\\Documents\\Visual Studio 2015\\Projects\\Magisterka\\Magisterka\\Data\\Configuration.XML" # HAVE TO BE DEFINED IN CODE !!!

	def __init__(self):
		XMLConfiguration.__init__(self,Paths.DirDataXML)

		elem = self.XMLRoot.find("Paths/Dir")
		Paths.Dir = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirData")
		Paths.DirData = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirDataDB")
		Paths.DirDataDB = self.ValidateType(elem)
		elem = self.XMLRoot.find("Paths/DirDataLogs")
		Paths.DirDataLogs = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirDataLogsErrors")
		Paths.DirDataLogsErrors = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirDataLogsClassifier")
		Paths.DirDataLogsClassifier = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirDataLogsAnalize")
		Paths.DirDataLogsAnalize = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirDataLogsEquations")
		Paths.DirDataLogsEquations = self.ValidateType(elem)
		elem = self.XMLRoot.find("Paths/DirDataSensorsNewData")
		Paths.DirDataSensorsNewData = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirDataSensorsPreprocess")
		Paths.DirDataSensorsPreprocess = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirDataProjectedSensors")
		Paths.DirDataProjectedSensors = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirFig")
		Paths.DirFig = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirFigSensors")
		Paths.DirFigSensors = self.ValidateBackSlash(self.ValidateType(elem))
		elem = self.XMLRoot.find("Paths/DirFigProjectedSensors")
		Paths.DirFigProjectedSensors = self.ValidateBackSlash(self.ValidateType(elem))




class SensorsSettings(XMLConfiguration):
	"""This class keeps information about settings which apply for predictions"""

	SensorsCount = 84
	LastMeasurementsNumber = 10 #number of measurements which will be taken to compute local trend line
	TrainUsingLastNMeasurements = 50
	TrainUsingLastNFake = 50 # narazie nieuzywane

	def __init__(self):
		XMLConfiguration.__init__(self,Paths.DirDataXML)

		elem = self.XMLRoot.find("SensorsSettings/SensorsCount")
		SensorsSettings.SensorsCount = self.ValidateType(elem)
		elem = self.XMLRoot.find("SensorsSettings/LastMeasurementsNumber")
		SensorsSettings.LastMeasurementsNumber = self.ValidateType(elem)
		elem = self.XMLRoot.find("SensorsSettings/TrainUsingLastNMeasurements")
		SensorsSettings.TrainUsingLastNMeasurements = self.ValidateType(elem)
		elem = self.XMLRoot.find("SensorsSettings/TrainUsingLastNFake")
		SensorsSettings.TrainUsingLastNFake = self.ValidateType(elem)


class KNNSettings(XMLConfiguration):
	"""This class keeps information about settings which apply for single classification"""

	n_neighbors=3
	weights= "distance"
	algorithm= "auto"
	metric= "minkowski"

	def __init__(self):
		XMLConfiguration.__init__(self,Paths.DirDataXML)
		
		elem = self.XMLRoot.find("KNNSettings/n_neighbors")
		KNNSettings.n_neighbors =  self.ValidateKNNValues(self.ValidateType(elem), elem.tag)
		elem = self.XMLRoot.find("KNNSettings/weights")
		KNNSettings.weights =  self.ValidateKNNValues(self.ValidateType(elem), elem.tag)
		elem = self.XMLRoot.find("KNNSettings/algorithm")
		KNNSettings.algorithm =  self.ValidateKNNValues(self.ValidateType(elem), elem.tag)
		elem = self.XMLRoot.find("KNNSettings/metric")
		KNNSettings.metric =  self.ValidateKNNValues(self.ValidateType(elem), elem.tag)



class ProjectSettings(XMLConfiguration):
	"""This class define some properties helpfull for code debug"""
	
	DebugMode = False

	def __init__(self):
		XMLConfiguration.__init__(self,Paths.DirDataXML)

		elem = self.XMLRoot.find("ProjectSettings/DebugMode")
		ProjectSettings.DebugMode = self.ValidateType(elem)



class MainSettings(XMLConfiguration):
	"""This class define actions which migh be taken during system lifetime"""
	
	CreateDB = False
	UpdateDBWithNewData = False
	DrawCharts = False
	DrawChartsTimeFrom = None
	DrawChartsTimeTo = None
	DrawProjectedCharts = False
	DrawProjectedChartsTimeFrom = None
	DrawProjectedChartsTimeTo = None
	Analyze = False
	AnalyzeTimeFrom = None
	AnalyzeTimeTo = None
	Classifier = False
	ClassifierTimeFrom = None
	ClassifierTimeTo = None
	ClassifierGenerateFakeData = False
	ClassifierGenerateFakeDataSamples = None
	ClassifierFakeDataMinMultiplier = None
	ClassifierFakeDataMaxMultiplier = None
	ClassifierParameters = {"mean" : True, "rms" : True, "skewness" : True, "curtosis" : True, "time" : False}

	def __init__(self):
		XMLConfiguration.__init__(self,Paths.DirDataXML)
		
		elem = self.XMLRoot.find("MainSettings/CreateDB")
		MainSettings.CreateDB = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/UpdateDBWithNewData")
		MainSettings.UpdateDBWithNewData = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/DrawCharts")
		MainSettings.DrawCharts = self.ValidateAttributeType(elem)
		elem = self.XMLRoot.find("MainSettings/DrawCharts/timefrom")
		MainSettings.DrawChartsTimeFrom = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/DrawCharts/timeto")
		MainSettings.DrawChartsTimeTo = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/DrawProjectedCharts")
		MainSettings.DrawProjectedCharts = self.ValidateAttributeType(elem)
		elem = self.XMLRoot.find("MainSettings/DrawProjectedCharts/timefrom")
		MainSettings.DrawProjectedChartsTimeFrom = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/DrawProjectedCharts/timeto")
		MainSettings.DrawProjectedChartsTimeTo = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Analyze")
		MainSettings.Analyze = self.ValidateAttributeType(elem)
		elem = self.XMLRoot.find("MainSettings/Analyze/timefrom")
		MainSettings.AnalyzeTimeFrom = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Analyze/timeto")
		MainSettings.AnalyzeTimeTo = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier")
		MainSettings.Classifier = self.ValidateAttributeType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/timefrom")
		MainSettings.ClassifierTimeFrom = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/timeto")
		MainSettings.ClassifierTimeTo = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/GenerateFakeData")
		MainSettings.ClassifierGenerateFakeData = self.ValidateAttributeType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/GenerateFakeData/Samples")
		MainSettings.ClassifierGenerateFakeDataSamples = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/GenerateFakeData/minimumvalue")
		MainSettings.ClassifierFakeDataMinMultiplier = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/GenerateFakeData/maximumvalue")
		MainSettings.ClassifierFakeDataMaxMultiplier = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/Parameters/mean")
		MainSettings.ClassifierParameters["mean"] = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/Parameters/rms")
		MainSettings.ClassifierParameters["rms"] = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/Parameters/skewness")
		MainSettings.ClassifierParameters["skewness"] = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/Parameters/curtosis")
		MainSettings.ClassifierParameters["curtosis"] = self.ValidateType(elem)
		elem = self.XMLRoot.find("MainSettings/Classifier/Parameters/time")
		MainSettings.ClassifierParameters["time"] = self.ValidateType(elem)
