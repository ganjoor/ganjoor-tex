#!/usr/bin/env python3

import sys
import urllib.request

from html.parser import HTMLParser
from html.entities import name2codepoint

class PoemParser(HTMLParser):
    def __init__(self, outf):
        super(PoemParser, self).__init__()
        self.tags = []
        self.out = outf
        self.divclass = ""
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        for attr in attrs:
            if attr[0] == "class":
                self.divclass = attr[1]

    def handle_endtag(self, tag):
        if len(self.tags)>=2 and self.tags[-1] == "p" and self.tags[-2] == "div":
            if self.divclass == "m1":
                self.out.write('\n')
            if self.divclass == "m2":
                self.out.write('\n\n')

        self.tags.pop()

    def handle_data(self, data):
        if len(self.tags)>=2 and self.tags[-1] == "p" and self.tags[-2] == "div":
            if self.divclass == "m1" or self.divclass == "m2":
                self.out.write(data)

class ContentTableParser(HTMLParser):
    def __init__(self, outpath):
        super(ContentTableParser, self).__init__()
        self.tags = []
        self.url = ""
        self.path = outpath
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        for attr in attrs:
            if attr[0] == "href":
                self.url = attr[1]

    def handle_endtag(self, tag):
        self.tags.pop()

    def handle_data(self, data):
        if len(self.tags)>=2 and self.tags[-1] == "a" and self.tags[-2] == "p" and self.url[0:4]=="http":
            
            urllist = self.url.split("/")
            urllist = list(filter(None, urllist))
            outname = urllist[len(urllist)-1]
            if (len(outname)==3):
                outname = outname[0:2] + "00" + outname[2:3]
            if (len(outname)==4):
                outname = outname[0:2] + "0" + outname[2:4]

            self.writefile(data, outname)

    def writefile(self, title, outname):
        outf = open(self.path+"/"+outname+".txt", "w")
        outf.write(title+'\n\n')
        print(title)
        outcontent = urllib.request.urlopen(self.url).read().decode("utf8")

        parser = PoemParser(outf)
        parser.feed(outcontent)

        outf.close()

if len(sys.argv) < 3 :
    print("usage: "+sys.argv[0]+" <ganjoor link> <text directory>")
    sys.exit(0)

outpath = sys.argv[2]

inf = urllib.request.urlopen(sys.argv[1])
content = inf.read().decode("utf8")

parser = ContentTableParser(outpath)
parser.feed(content)

inf.close()
