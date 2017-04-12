
from __future__ import division
from itertools import groupby
import itertools
#import groupby
import operator


f = open("movie_metadata.txt","r")  # open file, read-only raw data

o = open("mapper_output.txt", "w") # open file, write - just our key, value pairs

for line in f:  

    data = line.strip().split("\t") 

    #print data

    #print len(data)

    if len(data) == 6:

        color, director_name, duration, actor_1_name, movie_title, title_year = data
        #print "{1}\t{4}".format(director_name, movie_title)
        o.write("{0}\t{1}\n".format(title_year, movie_title))

       
f.close()
o.close()
o = open("mapper_output.txt", "r")
sorted = open("sortedMapper_output.txt", "w")
lines = o.readlines()
lines.sort()
#print(lines)
for line in lines:
	sorted.write(line)
o.close()
sorted.close()
