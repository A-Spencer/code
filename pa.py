import sys
import os
import subprocess
import json

def writeJSON(mydictionary: dict()) -> None:
	'''
	writes a JSON object file to 'command.db'
	'''
	jsondict = json.dumps(mydictionary)
	with open ('/home/aspencer/command.db', 'wt') as output:
		output.write(jsondict)
	output.close()

def readJSON() -> dict():
	'''
	reads 'command.db' and returns a JSON object file
	'''
	with open ('/home/aspencer/command.db', 'rt') as inputfile:
		jsondict = inputfile.read()
		mydictionary = json.loads(jsondict)
		return mydictionary
	inputfile.close()

def processCMD(input: str, mydictionary: dict()) -> None:
	if (input in str(mydictionary.values())):
		gethelp = subprocess.run(["man", sys.argv[2]], stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
		print(gethelp.stdout)
	#else:
	#	pathdict[sys.argv[2]]

def FillDict() -> dict():
	'''
	reads all files in path locations and outputs a dictionary in the form of {'path directory': 'filename1', 'filename2', 'etc'}
	'''
	#make a list of paths (directories)
	paths = os.getenv("PATH")
	paths = paths.split(":")

	pathdict = dict()

	for dir in paths:
		for file in os.listdir(dir):
			fullname = os.path.join(dir, file)
			#checks if file is executable and is a file, not a directory
			if(os.access(fullname, os.X_OK) and os.path.isfile(fullname)):
				pathdict[dir] = os.listdir(dir)
	
	return pathdict



if (len(sys.argv) != 3):
	print("incorrect number of args.  quitting.")

def main():
	#FillDict()

if __name__ == "__main__":
    # execute only if run as a script
    main()

