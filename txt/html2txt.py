#!/usr/bin/env python

import sys
import urllib2

def writefile(outname, title, outurl, outpath):
    outf = open(outpath+"/"+outname+".txt", "w")
    outf.write(title+'\n\n')
    print(title)
    response = urllib2.urlopen(outurl)
    content = response.read().split("\n")
    for line in content:
        if line[0:15] == "<div class=\"b\">": 
            m1 = line.split('>')[3].split('<')[0]
            m2 = line.split('>')[7].split('<')[0]
            outf.write(m1+'\n')
            outf.write(m2+'\n\n')
    outf.close()

if len(sys.argv) < 3 :
    print "usage:", sys.argv[0], "<ganjoor link> <text directory>"
    sys.exit(0)

url = sys.argv[1].split('/')
name = url[len(url)-1]

outpath = sys.argv[2]

inf = urllib2.urlopen(sys.argv[1])
content = inf.read().split("\n")

for line in content:
    if line[0:3] == "<p>": 
        line1 = line.split('>')[1]
        outurl = line1.split("\"")[1]
        outname = line1.split("/")[6]
        if (len(outname)==3):
            outname = "sh00" + outname[2:3]
        if (len(outname)==4):
            outname = "sh0" + outname[2:4]
        title = line.split('>')[2].split('<')[0]
        writefile(outname, title, outurl, outpath) 

inf.close()
