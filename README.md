<div align="center">
  <img src="https://github.com/kairavkkp/Merge-PDF/blob/master/merge-pdf-logo.png" alt="Merge-PDF" align="center" width="150" height="150" />


# [Merge-PDF](https://github.com/kairavkkp/Merge-PDF) 

[![Build Status](https://travis-ci.com/kairavkkp/Merge-PDF.svg?branch=master)](https://travis-ci.com/kairavkkp/Merge-PDF)
[![PyPI version](https://badge.fury.io/py/mergemypdf.svg)](https://badge.fury.io/py/mergemypdf)
[![Downloads](https://pepy.tech/badge/mergemypdf)](https://pepy.tech/project/mergemypdf)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)



Merge PDF files using customizations within a folder using Command line.

</div>

# How to Install
`pip install mergemypdf`

# How to use
- Open Terminal
- Move to the directory where PDFs are present.
- Run `mergemypdf -h` for more info.

#### Usage: 
`mergemypdf -c <number_of_pdfs> -o <order_of_merging>  -f <output_pdf_filename>`

#### Examples:
`mergemypdf -c 10 -o 1 -f merged.pdf`

`mergemypdf -p password -f merged.pdf`

`mergemypdf -ep 1 -p password`

`mergemypdf -a 1 -f merged.pdf`


#### Optional arguments:
```
- s : <pdf_name_starting_with_string> 
- e : <pdf_name_endswith_string> 
- cn: <pdf_name_containing_string>
```

#### Note:
- `-c` represents number of PDFs needed to merge.
- `-o` represents order of merging PDFs, 0 is Ascending, 1 is descending and 2 is Shuffle. Default is Ascending.
- `-s` represents start string in PDF file's name.
- `-e` represents end string in PDF file's name.
- `-cn` represents string containing in PDF file's name.
- `-f` represents saved file name. Default names are randomly generated, adviced to specify a name everytime.
- `-i` represents the flag if only images need to be merged within a folder. Default is false.
- `-ip` represents the flag if both images and pdfs need to be merged within a folder. Default is false.
- `-p` represents password used to decrypt PDFs. If the PDFs have individually different passwords omit this and you will be prompted to enter each password.
- `-epub` represents the flag if only EPUBs need to be merged within a folder. Default is false.
- `-ep` represents the flag if both EPUBs and PDFs need to be merged within a folder. Default is false.
- `-ie` represents the flag if both images and EPUBs need to be merged within a folder. Default is false.
- `-a` represents the flag if all support file types (PDF, Images and EPUBS) need to be merged within a folder. Default is false.

#### Usage of Optional Arguments.
- `mergemypdf -s 09` Only merge PDFs starting with 09.
- `mergemypdf -e Derivation` Only merge PDFs ending with Derivation.
- `mergemypdf -cn Lecture` Only merge PDFs having keyword 'Lecture' in the name.
- `mergemypdf -i 1` Only merge Images from the directory.
- `mergemypdf -ip 1` Merge both Images and PDFs from the directory.
- `mergemypdf -p test123` Merge all PDFs from directory using the supplied password on any encrypted PDFs.
- `mergemypdf -epub 1` Only merge EPUB files from the directory.
- `mergemypdf -ep 1` Merge both EPUBs and PDFs from the directory.
- `mergemypdf -ie 1` Merge both Images and EPUBs from the directory.
- `mergemypdf -a 1` Merge PDFs, Images and EPUBs from the directory.

#### Tests
- Sample Files
  - `sample.pdf`, `sample-protected.pdf`, `sample.epub`, `sample.jpeg`, `sample.jpg`, `sample.tiff`, `sample.png`, `sample.gif`.
- Tests are based on pytest.
