# -*- coding: utf-8 -*-
#! python3

#Automate the Boring Stuff with Python - Chapter 9 Practice Project - Deleting Unneeded Files

#big_files.py - A program that walks through a folder tree and searches for exceptionally
#large files or folders—say, ones that have a file size of more than 100MB.

import os

folder = 'D:\1_PYTHON_PROJEKTY\Sweigart_tasks' #input("Enter a folder path to start searching: ")
size = int(input('Enter the size in MB: ')) * 10**6 #100*10**6

def bigFiles(folder, size):
	files = []
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			filesize = os.path.getsize(os.path.join(foldername, filename))
			if filesize > size:
					files.append(os.path.relpath(filename) + " - " + str(int(filesize/(2**20))) + " MB")

	return files

print(bigFiles(folder, size))