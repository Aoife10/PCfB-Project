#! /usr/bin/env python

Trans={
'Na14':2,
'Ho14':3}

a = raw_input("Enter the desired data: ")

# Set the input file name
InFileName = 'try1.txt' #alias to make it easier

# Derive the output file name from the input file name
OutFileName = "newdata.txt"

# Open the input file, InFileName, and specify the mode, read
InFile = open(InFileName, 'r')
OutFile = open(OutFileName, 'w') 	# Open the output file, and set the mode to 'write'

if a in Trans:
	a = Trans[a]
else:
	print("error")

# Loop over each line in the file
for Line in InFile:
	Line = Line.strip('\n') #overwrite Line without enter
	# Split the line into a list of ElementList, using tab as a delimiter
	ElementList = Line.split('\t') #6........
	
	# Returns a list and changes the order of the elements so that it will be changed to this format:
	Long    = ElementList[0] 
	Lat    = ElementList[1]
	Na14   = ElementList[2]  # A string, not a number
	Ho14   = ElementList[3]

	OutFile.write(ElementList[0])
	OutFile.write("\t")
	OutFile.write(ElementList[1])
	OutFile.write("\t")
	OutFile.write(ElementList[a])
	OutFile.write("\n")

	
# Close the files
InFile.close()
OutFile.close()
