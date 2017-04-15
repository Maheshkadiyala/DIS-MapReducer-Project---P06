#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
from __future__ import division
from itertools import groupby
import itertools
#import groupby
import operator
#this will open sortedMapper_output.txt file in read format and result file in write format
s = open("sortedMapper_output.txt","r")
results = open("result.txt", "w")
oldTitle_year = None
moviesCount = 0

lines = s.readlines()
#this for loop picks one line record from data set and writes title year and number of movies in that year
for line in lines:
    #print line 
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisTitle_year, thisMovie_title = data_mapped
    #print thisTitle_year
    #print thisMovie_title, "\t", thisDirector_name
	
	
    if oldTitle_year and (oldTitle_year != thisTitle_year):
        #print oldTitle_year
        results.write("{0}\t{1}\n".format(oldTitle_year, moviesCount))
    
    if oldTitle_year and (oldTitle_year != thisTitle_year): 
			
        oldTitle_year = thisTitle_year
        moviesCount = 0
    #print thisDirector_name
    oldTitle_year = thisTitle_year
    moviesCount = moviesCount+1
    #print "hello"
	
    #if oldDirector_name != None: 
		#results.write("{0}\t{1}\n".format(oldDirector_name, moviesCount))
        #print "hello" 
#print "hello"	

# closes sortedMapper_output file and results file 		
s.close() 
results.close()