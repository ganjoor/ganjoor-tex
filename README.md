# Ganjoor-TeX

Ganjoor-TeX is a set of scripts to convert the content of the ganjoor.net (a Persian poetry) website into LaTeX files.

## Getting started

### Html to Text

The script `html2txt.py` reads the content of the ganjoor.net and creates text files.

```
usage:   ./html2txt.py <ganjoor link> <txt directory>

example: ./html2txt.py https://ganjoor.net/moulavi/masnavi/daftar1/ moulavi/masnavi/daftar1/
```

### Text to TeX

The script `txt2tex.py` reads the content of text files created by `html2txt.py` and creates TeX files.

```
usage:   ./txt2tex.py <txt directory> <tex directory>

example: ./txt2tex.py ../txt/moulavi/masnavi/daftar1/ moulavi/masnavi/daftar1
```
