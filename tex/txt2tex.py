#!/usr/bin/env python

import sys
import os

def writefile(textpath, texpath, fname):
    name = fname.split(".")[0]
    inf = open(textpath+'/'+fname)
    outf = open(texpath+'/'+name+".tex", "w")
    lines = inf.readlines()
    title = lines.pop(0).split('\n')[0]
    print(title)

    outf.write("\\begin{center}\n")
    outf.write("\\section*{"+title+"}\n")
    outf.write("\\label{sec:"+name+"}\n")
    outf.write("\\addcontentsline{toc}{section}{\\nameref{sec:"+name+"}}\n")
    outf.write("\\begin{longtable}{l p{0.5cm} r}\n")
    
    verse = 1
    for line in lines:
        if line == "" or line == "\n":
            continue
        outf.write(line)
        if verse == 1:
            outf.write("&&\n")
            verse = 2
            continue
        if verse == 2:
            outf.write("\\\\\n")
            verse = 1
            continue
    outf.write("\\end{longtable}\n")
    outf.write("\\end{center}\n")
    inf.close()
    outf.close()

if len(sys.argv) < 3 :
    print("usage: "+sys.argv[0]+" <txt directory> <tex directory>")
    sys.exit(0)

files = os.listdir(sys.argv[1])

texpath = sys.argv[2]
if texpath[len(texpath)-1] == '/':
    texpath = texpath[:-1]

texf = open(texpath+'.tex', 'w')
texpathlist = texpath.split('/')
pname = texpathlist[len(texpathlist)-1]

texf.write("\\documentclass[14pt,b5paper]{book}\n")

texf.write("\\usepackage[top=3cm, bottom=2cm, left=2cm, right=2cm]{geometry}\n")
texf.write("\\usepackage{longtable}\n")
texf.write("\\usepackage[hidelinks]{hyperref}\n")
texf.write("\\setlength{\parskip}{1em}\n")
texf.write("\\usepackage{color,xcolor}\n")   
texf.write("\\usepackage{xepersian}\n")
texf.write("\\usepackage{fontspec}\n")
texf.write("\\usepackage{nameref}\n")
texf.write("\\settextfont[Scale=1.5]{IranNastaliq}\n")
texf.write("\\setlatintextfont[Scale=1]{TeX Gyre Termes}\n")
texf.write("\\renewcommand{\\arraystretch}{3.5}\n")

texf.write("\\begin{document}\n")
texf.write("\\input{"+pname+"-title}\n")
texf.write("\\pagestyle{empty} {\n")
texf.write(" \\renewcommand{\\thispagestyle}[1]{}\n")
texf.write(" \\maketitle\n")
texf.write(" \\tableofcontents\n")
texf.write("}\n")
texf.write("\\clearpage\n")
texf.write("\\pagestyle{plain}\n")
texf.write("\\setcounter{page}{1}\n")

for fname in sorted(files):
    writefile(sys.argv[1], texpath, fname)
    texf.write("\\input{"+pname+'/'+fname.split('.')[0]+"}\n")
    texf.write("\\newpage\n")

texf.write("\\end{document}\n")

texf.close()
