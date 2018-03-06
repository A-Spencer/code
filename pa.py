#!/usr/bin/python3

###########################
## pa.py v1.0			 ##
## Alec Spencer			 ##
## aspencer18@my.bcit.ca ##
## March 5, 2018		 ##
###########################

import sys
import os
import subprocess
import json

def writeJSON(mydictionary: dict()) -> None:
	'''
	writes a JSON object file to 'command_db.json'
	'''
	jsondict = json.dumps(mydictionary)
	with open ('command_db.json', 'wt') as output:
		output.write(jsondict)
	output.close()


def readJSON() -> dict():
	'''
	reads 'command_db.json' and returns a JSON object file
	'''
	with open ('command_db.json', 'rt') as inputfile:
		jsondict = inputfile.read()
		return json.loads(jsondict)
	inputfile.close()


def processCMD(cmd: str, mydictionary: dict()) -> None:
	'''
	Prints the man pages for a command if it exists in the command dictionary.
	If not, adds the command to the dictionary
	'''
	if (cmd in str(mydictionary.values())):
		gethelp = subprocess.run(["man", sys.argv[2]], stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
		print(gethelp.stdout)
	else:
		#make a list of paths (dirsectories)
		paths = os.getenv("PATH")
		paths = paths.split(":")

		try:
				
			for dirs in paths:
				for filename in os.listdir(dirs):
					fullname = os.path.join(dirs, filename)
					if ((filename == cmd) and os.access(fullname, os.X_OK) and os.path.isfile(fullname)):
						if dirs not in mydictionary:
							mydictionary[dirs] = [cmd]
						else:
							mydictionary[dirs].append(cmd)
		except:
			pass

		writeJSON(mydictionary)

	return


def FillDict() -> dict():
	'''
	reads all files in path locations and outputs a dictionary in the form of {'path dirsectory': 'filename1', 'filename2', 'etc'}
	'''
	#make a list of paths (dirsectories)
	paths = os.getenv("PATH")
	paths = paths.split(":")

	mydictionary = dict()

	try:
		for dirs in paths:
			for filename in os.listdir(dirs):
				fullname = os.path.join(dirs, filename)
				#checks if filename is executable and is a file, not a dirsectory
				if(os.access(fullname, os.X_OK) and os.path.isfile(fullname)):
					mydictionary[dirs] = os.listdir(dirs)
	except:
		pass

	return mydictionary



def main():

	if (len(sys.argv) != 3):
		print("Incorrect number of args.  \nSyntax:\n$ python pa.py cmd <command>\n$ python pa.py rep term\n$ python pa.py rep file")
	else:
	
		pathdict = dict()
		
		try:
			pathdict = readJSON()
		except:
			pass	

		if sys.argv[1] == 'cmd':
			processCMD(sys.argv[2], pathdict)
		elif sys.argv[1] == 'rep':
			if sys.argv[2] == 'term':
				print(pathdict)
			elif sys.argv[2] == 'file':
				writeJSON(pathdict)

if __name__ == "__main__":
    main()

