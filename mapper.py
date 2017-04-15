
from __future__ import division
from itertools import groupby
import itertools
#import groupby
import operator

#this will open movie_metadata.txt file in read format and mapper_output file in write format
f = open("movie_metadata.txt","r")  # open file, read-only raw data

o = open("mapper_output.txt", "w") # open file, write - just our key, value pairs
#this for loop picks one line record from data set and writes only director name and movie title to the movie_output file
for line in f:  

    data = line.strip().split("\t") 

    #print data

    #print len(data)

    if len(data) == 6:

        color, director_name, duration, actor_1_name, movie_title, title_year = data
        #print "{1}\t{4}".format(director_name, movie_title)
        o.write("{0}\t{1}\n".format(director_name, movie_title))

 #closes movie_metadata file and mapper_output file   
f.close()
o.close()
#opens mapper_output file in read mode
o = open("mapper_output.txt", "r")
#opens sortedMapper_output file in wirte mode
sorted = open("sortedMapper_output.txt", "w")
lines = o.readlines()
lines.sort()
#print(lines)
# this for loop sorts output in sorted order
for line in lines:
	sorted.write(line)
o.close()
sorted.close()
