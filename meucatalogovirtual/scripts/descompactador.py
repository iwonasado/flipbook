# -*- coding: utf-8 -*-
import os
import zipfile

class Descompactador():

	def __init__(self):
		self.content = []

	def zip(self,path,pathTo):
		file = zipfile.ZipFile(path, "r")
		for name in file.namelist():
			ext = os.path.splitext(name)[1]
			if ext in ([".jpg",".png"]):
				file.extract(name, pathTo)
				self.content.append(name)