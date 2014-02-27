import os
from os import listdir
from os.path import isfile, join

#import wand.Image

class pdftojpg:
	def __init__(self,path,pathTo):
		self.content = []
		# try:
		if not os.path.exists(pathTo):
			os.makedirs(pathTo)
		os.system("convert -quality 100% "+path+" "+ pathTo+"/page.jpg")
		self.content = [ f for f in listdir(pathTo) if isfile(join(pathTo,f)) ]
		# except (OSError) as e:
  #       		print e
		# with Image(filename=path) as img:
		# 	img.save(filename=pathTo+"/page.jpg")

