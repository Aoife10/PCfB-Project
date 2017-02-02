#! /usr/bin/env python

#This script will make a subset of a complete data set according to what the user would like to use

#Make a dictionary to transform the names of the columns (user input) into column names
Trans={
'NInd':2,
'R14':3,
'Na14':4,
'A20':5,
'Ho14':6}

#Give the user a choice of possible data and its associated code
print "Make a map of: "
print ""
print "Number of individuals: NoInd"
print "Genotypic Richness (N=14): R14"
print "Number Of Alleles Per Locus(N=14): Na14"
print "AllelicRichness(MLG=20): A20"
print "Observed Heterozygozity (N=14): Ho14"

# Set the input file name of the complete data set
InFileName = 'CompleteData.txt' #alias to make it easier

# Make an output file
OutFileName = "newdata.txt"

# Open the input file, InFileName, and specify the mode, read
InFile = open(InFileName, 'r')
OutFile = open(OutFileName, 'w') 	# Open the output file, and set the mode to 'write'



#ask the user to input the code of the desired data
#output "error" if the user did not enter a correct code. 
#In this case the user will have to reenter a new code
#If the code is correct, tranlate code to the column number
def getCol():
	d = raw_input("Enter the desired data: ")
	if d in Trans:
		n = Trans[d]
		return n
	else:
		print "error"
		return getCol()

a = getCol()	
	
# Loop over each line in the file
for Line in InFile:
	Line = Line.strip('\n') #overwrite Line without enter
	# Split the line into a list of ElementList, using tab as a delimiter
	ElementList = Line.split('\t') 

	#write a new subset of the data to the new output file according to the desired data (called a)
	OutFile.write(ElementList[0])
	OutFile.write("\t")
	OutFile.write(ElementList[1])
	OutFile.write("\t")
	OutFile.write(ElementList[a])
	OutFile.write("\n")

# Close the files
InFile.close()
OutFile.close()
