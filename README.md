# [Merge-PDF](https://github.com/kairavkkp/Merge-PDF)
[![PyPI version](https://badge.fury.io/py/mergemypdf.svg)](https://badge.fury.io/py/mergemypdf)

Merge PDF files using customizations within a folder using Command line.

# How to Install
`pip install mergemypdf`

# How to use
- Open Terminal
- Move to the directory where PDFs are present.
- Run `mergemypdf -h` for more info.

#### Usage: 
`mergemypdf -c <number_of_pdfs> -o <order_of_merging>  -f <output_pdf_filename>`

#### Example Usage:
`mergemypdf -c 10 -o 1 -f merged.txt`


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

#### Usage of Optional Arguments.
- `mergemypdf -s 09` Only merge PDFs starting with 09.
- `mergemypdf -e Derivation` Only merge PDFs ending with Derivation.
- `mergemypdf -cn Lecture` Only merge PDFs having keyword 'Lecture' in the name.
