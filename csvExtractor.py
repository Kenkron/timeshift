#imports the csv library
import csv
#open the output file for writing
f = open('extractOutput.txt','w')
#create a hash table for the values that have already been processed
values = {}
#open the input file
inputFile=open('timezone.csv')
#extract the lines of the input file
inputLines=csv.reader(inputFile);
#go through each of the lines of input
for data in inputLines:
    #see if the element at 1 is already in the hash table
    if (data[1] not in values):
        #If it is not, write an output for this line
        f.write ("'"+data[1]+"':"+data[3]+",\n")
        #and add the element at 1 to the hash table
        #(so that it won't be written again)
        values[data[1]]=data[3]
