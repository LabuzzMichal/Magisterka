# -*- coding: utf-8 -*-

import lxml.etree as ET
import os
from datetime import datetime

class XMLConfiguration():
	"""This class load configuration from XML and valdiate it"""
	XMLTree = None
	XMLRoot = None
	def __init__(self, xmlfile):
		self.XMLTree = ET.parse(xmlfile)
		self.XMLRoot = self.XMLTree.getroot()
		schema = ET.XMLSchema(file=os.path.join(os.path.dirname(xmlfile),"Configuration.XSD"))
		schema.assertValid(self.XMLTree)


	def ValidateType(self, elementnode):
		if elementnode.attrib["Type"] == "str":
			return str(elementnode.text)
		elif elementnode.attrib["Type"] == "int":
			try:
				return int(elementnode.text)
			except ValueError as ve:
				raise "Value in field {0} should be integer type!".format(elementnode.tag)
		elif elementnode.attrib["Type"] == "bool":
			if elementnode.text in ['true', 'True', 't', '1', 'yes', 'y']:
				return True
			else:
				 return False
		elif elementnode.attrib["Type"] == "datetime":
			if elementnode.text == "None":
				return None
			else:
				try:
					return datetime.datetime.strptime(elementnode.text, '%Y-%m-%d')
				except ValueError:
					raise "Error occured. Data in XML should be in YYYY-MM-DD format"
		elif elementnode.attrib["Type"] == "float":
			try:
				return float(elementnode.text)
			except ValueError as ve:
				print "Value in field {0} should be float type!".format(elementnode.tag)
				

	def ValidateAttributeType(self, elementnode):
		if elementnode.attrib["ValueType"] == "str":
			return str(elementnode.attrib["Value"])
		elif elementnode.attrib["ValueType"] == "int":
			try:
				return int(elementnode.attrib["Value"])
			except ValueError as ve:
				raise "Attribute Value in field {0} should be integer type!".format(elementnode.tag)
		elif elementnode.attrib["ValueType"] == "bool":
			if elementnode.attrib["Value"] in ['true', 'True', 't', '1', 'yes', 'y']:
				return True
			else:
				 return False
	
	def ValidateBackSlash(self,value):
		if value[-1] != '\\' and value[-1] != '/':
			return value + '\\'
		else:
			return value


	def ValidateKNNValues(self,value,tag):
		if tag == "n_neighbors":
			if value > 0 and value < 100:
				return value
			else:
				pass
				#TODO: WYMYSLIC CO DOPISAC
		elif tag == "weights":
			if value in ["distance", "uniform"]:
				return value
			else:
				pass
				#TODO: WYMYSLIC CO DOPISAC
		elif tag == "algorithm":
			if value in ["auto", "ball_tree", "kd_tree", "brute"]:
				return value
			else:
				pass
				#TODO: WYMYSLIC CO DOPISAC
		elif tag == "metric":
			if value in ["euclidean", "manhattan", "chebyshev", "minkowski", "wminkowski", "seucliean", "mahalanobis"]:
				return value
			else:
				pass
				#TODO: WYMYSLIC CO DOPISAC
		else:
			pass



