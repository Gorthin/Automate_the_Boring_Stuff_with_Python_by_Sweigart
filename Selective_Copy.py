# -*- coding: utf-8 -*-
#! python3

#Automate the Boring Stuff with Python - Chapter 9 Practice Project - Selective Copy

#selec_co.py -  A program that walks through a folder tree and searches for files with
#a certain file extension and copy to a new folder.

import os
import shutil as s

def selectiveCopy(folder, extension):
	folder = os.path.relpath(folder)

	number = 1
	while True:
		try:
			new_folder = "%s_files_" % (extension.upper()) + str(number)
			os.makedirs(".\\%s" % (new_folder))
			break
		except:
			number += 1

	print("Creating %s..." % (os.path.relpath(new_folder)))

	for foldername, subfolder, filenames in os.walk(folder):
		if os.path.basename(foldername) == new_folder:
			continue
		print("Searchin for %s " %(extension.upper()) + "files in %s..." % (foldername))

		for filename in filenames:
			if filename.endswith(".%s" % (extension)):
				s.copy(os.path.join(foldername, filename), new_folder)

	return new_folder

print("Enter a file extension: ")
extension = input()
new_folder = selectiveCopy(".", extension.lower())
try:
	os.rmdir(new_folder)
	print("No %s files found." % (extension.upper()))
except:
	print("Done! Folder created!")