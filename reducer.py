#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
from __future__ import division
from itertools import groupby
import itertools
#import groupby
import operator
s = open("sortedMapper_output.txt","r")
results = open("result.txt", "w")

oldDirector_name = None
moviesCount = 0

lines = s.readlines()
for line in lines:
    #print line 
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisDirector_name, thisMovie_title = data_mapped
    #print oldDirector_name
    #print thisMovie_title, "\t", thisDirector_name
	
	
    if oldDirector_name and (oldDirector_name != thisDirector_name):
        results.write("{0}\t{1}\n".format(oldDirector_name, moviesCount))
    
    if oldDirector_name and (oldDirector_name != thisDirector_name): 
			
        oldDirector_name = thisDirector_name
        moviesCount = 0
    #print thisDirector_name
    oldDirector_name = thisDirector_name
    moviesCount = moviesCount+1
    #print "hello"
	
    #if oldDirector_name != None: 
		#results.write("{0}\t{1}\n".format(oldDirector_name, moviesCount))
        #print "hello" 
#print "hello"		
s.close() 
results.close()