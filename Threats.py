#! /usr/bin/env python

#This script will make a subset of a complete data set according to what the user would like to use

#Make a dictionary to transform the names of the columns (user input) into column names
Trans={
'fish':0,
'nut':1,
'ship':2,
'pol':3,
'uv':4,
'uvb':5,
'oa':6,
'sst':7,
'inv':8,
'pop':9,
'oil':10,
'hypoxinv':11,
'cthreat':12}


#Give the user a choice of possible data and its associated code
print "Make a map of: "
print ""
print "Destructive fishing: fish"
print "Nutrien input: nut"
print "Commercial shipping: ship"
print "Organic pollution: pol"
print "uv radiation: uv"
print "urban runoff: uvb"
print "ocean acidification: oa"
print "SST increase"
print "Invasive species: inv"
print "Coastal population density: pop"
print "oil spills: oil"
print "risk of hypoxia: hypoxinv"
print "Cumulative threat: cthreat"

# Set the input file name of the complete data set
InFileName = 'human_impact.txt' #alias to make it easier

# Make an output file
OutFileName = "newdataHI.txt"

# Open the input file, InFileName, and specify the mode, read
InFile = open(InFileName, 'r')
OutFile = open(OutFileName, 'w') 	# Open the output file, and set the mode to 'write'

#ask the user to input the code of the desired data
a = raw_input("Enter the code of the desired data: ")

#output "error" if the user did not enter a correct code. 
#In this case the user will have to restart the program
#If the code is correct, tranlate code to the column number
if a in Trans:
	a = Trans[a]
else:
	print("error")

# Loop over each line in the file
for Line in InFile:
	Line = Line.strip('\n') #overwrite Line without enter
	# Split the line into a list of ElementList, using tab as a delimiter
	ElementList = Line.split('\t') 

	#write a new subset of the data to the new output file according to the desired data (called a)
	OutFile.write(ElementList[13])
	OutFile.write("\t")
	OutFile.write(ElementList[14])
	OutFile.write("\t")
	OutFile.write(ElementList[a])
	OutFile.write("\n")

# Close the files
InFile.close()
OutFile.close()
