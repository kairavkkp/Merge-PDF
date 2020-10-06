import os
import argparse
import re
import logging
from PyPDF2 import PdfFileReader, PdfFileWriter
import random
import re
import uuid
from PIL import Image
import img2pdf
import io
import fitz
from io import BytesIO
from getpass import getpass

image_extns = ['jpg', 'jpeg', 'tiff', 'png', 'gif']


def pdf_global(pdfs, args, pdf_writer):
    cnt = 0

    for pdf in pdfs:
        idata = open(pdf, "rb").read()  # read the PDF into memory and
        ibuffer = BytesIO(idata)  # convert to stream
        
        doc = fitz.open("pdf", ibuffer)

        if doc.isEncrypted:
            if args.password:
                rc = doc.authenticate(args.password)
                if not rc > 0:
                    raise ValueError("wrong password")
            else:
                password = getpass(f"{pdf} is encrypted. Please enter password: ")
                rc = doc.authenticate(password)
                if not rc > 0:
                    raise ValueError("wrong password")

        c = doc.write(garbage=3, deflate=True)
        del doc  # close & delete doc

        if cnt == args.count:
            break

        if args.start_string == None and args.end_string == None and args.contains == None:
            pdf_reader = PdfFileReader(BytesIO(c))
            pdf_writer = read_pdf(pdf_reader, pdf_writer)

            cnt += 1

        # With end or start strings
        else:
            # Starts

            if args.start_string is not None:
                #print('DEBUG: Entered StartsWith Portion')

                if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+', pdf[:-4], re.IGNORECASE):
                    pdf_reader = PdfFileReader(BytesIO(c))
                    pdf_writer = read_pdf(pdf_reader, pdf_writer)

                    cnt += 1

            if args.end_string is not None:
                #print('DEBUG: Entered EndsWith Portion')

                if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$', pdf[:-4], re.IGNORECASE):
                    pdf_reader = PdfFileReader(BytesIO(c))
                    pdf_writer = read_pdf(pdf_reader, pdf_writer)
                    cnt += 1

            if args.contains is not None:
                #print('DEBUG: Entered Contains Portion')

                if re.search(re.escape(str(args.contains)), pdf[:-4], re.IGNORECASE):
                    pdf_reader = PdfFileReader(BytesIO(c))
                    pdf_writer = read_pdf(pdf_reader, pdf_writer)
                    cnt += 1

    return pdf_writer


def epub_global(epubs, args, pdf_writer):
    cnt = 0

    for epub in epubs:     
        doc = fitz.open(epub)
        c = doc.convertToPDF()

        if cnt == args.count:
            break

        if args.start_string == None and args.end_string == None and args.contains == None:
            pdf_reader = PdfFileReader(BytesIO(c))
            pdf_writer = read_pdf(pdf_reader, pdf_writer)

            cnt += 1

        # With end or start strings
        else:
            # Starts
            if args.start_string is not None:
                #print('DEBUG: Entered StartsWith Portion')

                if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+', epub[:-5], re.IGNORECASE):
                    pdf_reader = PdfFileReader(BytesIO(c))
                    pdf_writer = read_pdf(pdf_reader, pdf_writer)

                    cnt += 1

            if args.end_string is not None:
                #print('DEBUG: Entered EndsWith Portion')

                if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$', epub[:-5], re.IGNORECASE):
                    pdf_reader = PdfFileReader(BytesIO(c))
                    pdf_writer = read_pdf(pdf_reader, pdf_writer)
                    cnt += 1

            if args.contains is not None:
                #print('DEBUG: Entered Contains Portion')

                if re.search(re.escape(str(args.contains)), epub[:-5], re.IGNORECASE):
                    pdf_reader = PdfFileReader(BytesIO(c))
                    pdf_writer = read_pdf(pdf_reader, pdf_writer)
                    cnt += 1

    return pdf_writer


def image_global(imgs, args, pdf_writer, count=-1):

    cnt = 0
    for img in imgs:

        if cnt == args.count:
            break
        if args.start_string == None and args.end_string == None and args.contains == None:
            pdf_writer = read_img(img, pdf_writer)
            cnt += 1

        # With end or start strings
        else:
            # Starts

            if args.start_string is not None:
                #print('DEBUG: Entered StartsWith Portion')

                if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+', img[:-4], re.IGNORECASE):
                    pdf_writer = read_pdf(img, pdf_writer)
                    cnt += 1

            if args.end_string is not None:
                #print('DEBUG: Entered EndsWith Portion')

                if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$', img[:-4], re.IGNORECASE):
                    pdf_writer = read_pdf(img, pdf_writer)
                    cnt += 1

            if args.contains is not None:
                #print('DEBUG: Entered Contains Portion')

                if re.search(re.escape(str(args.contains)), img[:-4], re.IGNORECASE):
                    pdf_writer = read_pdf(img, pdf_writer)
                    cnt += 1

    return pdf_writer


def read_img(image, pdf_writer):
    try:
        pdf_bytes = img2pdf.convert(image)
        pdf_reader = PdfFileReader(io.BytesIO(pdf_bytes))
        pdf_writer.addPage(pdf_reader.getPage(0))
    except:
        print('Image cannot be added to PDF.')

    return pdf_writer


def read_pdf(pdf_reader, pdf_writer):
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    return pdf_writer


def main():

    parser = argparse.ArgumentParser(
        description='A package which merges all PDFs from a folder into a single PDF.')
    parser.add_argument('-c', '--count', action='store', dest='count', type=int,
                        help='Total number of PDFs to be merged. Default is all.')  # fixed count, all

    parser.add_argument('-o', '--order', action='store', dest='order', type=int, default=0,
                        help='Order in which PDFs need to be merged. 0 is Ascending, 1 is descending and 2 is shuffle.')  # ascending, descending, shuffle

    parser.add_argument('-s', '--startswith', action='store', dest='start_string',
                        help='Only merge PDFs whose names startswith provided strings.')  # default None
    parser.add_argument('-e', '--endswith', action='store', dest='end_string',
                        help='Only merge PDFs whose names startswith provided strings.')  # default None
    parser.add_argument('-cn', '--contains', action='store', dest='contains',
                        help='Only merge PDFs whose names contains provided strings.')  # default None
    parser.add_argument('-i', '--imageonly', action='store', dest='imageonly', default=0, type=int,
                        help='Only merge Images. Please avoid images with Transparency. Default is 0 (No images)')  # default None
    parser.add_argument('-ip', '--image_pdf', action='store', dest='image_pdf', default=0, type=int,
                        help='Merge Both PDFs and Images. Default is Only PDF')  # default Only PDF
    parser.add_argument('-f', '--filename', action='store', dest='filename_string', default=str(uuid.uuid4()
                                                                                                ).split('-')[0]+'.pdf', help='Filename of the merged PDF. Default is randomly generated names.')
    parser.add_argument('-p', '--password', action='store',dest='password', help='Password used to decrypt all PDFs. If the PDFs have individually different passwords omit this and you will be prompted to enter each password.')
    
    parser.add_argument('-epub', '--epubonly', action='store', dest='epubonly', default=0, type=int,
                        help='Only merge EPUB files. Default is 0 (No images)')  # default None
    parser.add_argument('-ep', '--epub_pdf', action='store', dest='epub_pdf', default=0, type=int,
                        help='Merge both EPUBs and PDFs. Default is only PDFs')  # default None
    parser.add_argument('-ie', '--image_epub', action='store', dest='image_epub', default=0, type=int,
                        help='Merge both Images and EPUBs. Default is only PDFs')  # default None
    parser.add_argument('-a', '--all', action='store', dest='all', default=0, type=int,
                        help='Merge all support file types (PDF, Images and EPUBS). Default is only PDFs')  # default None


    args = parser.parse_args()
    print(args)

    os.chdir(os.getcwd())

    pdf_writer = PdfFileWriter()

    pdfs = sorted([x for x in os.listdir() if ('.pdf' in x.lower())])
    imgs = sorted([x for x in os.listdir() if (
        x.lower().split('.')[-1] in image_extns)])
    epubs = sorted([x for x in os.listdir() if ('.epub' in x.lower())])


    # Ascending
    if args.order == 0:
        if args.imageonly == 1:
            pdf_writer = image_global(imgs, args, pdf_writer)

        elif args.image_pdf == 1:
            pdf_writer = pdf_global(pdfs, args, pdf_writer)
            pdf_writer = image_global(imgs, args, pdf_writer)

        elif args.epubonly == 1:
            pdf_writer = epub_global(epubs, args, pdf_writer)
        
        elif args.epub_pdf == 1:
            pdf_writer = epub_global(epubs, args, pdf_writer)
            pdf_writer = pdf_global(pdfs, args, pdf_writer)

        elif args.image_epub == 1:
            pdf_writer = image_global(imgs, args, pdf_writer)
            pdf_writer = epub_global(epubs, args, pdf_writer)
        
        elif args.all == 1:
            pdf_writer = pdf_global(pdfs, args, pdf_writer)
            pdf_writer = image_global(imgs, args, pdf_writer)
            pdf_writer = epub_global(epubs, args, pdf_writer)
        
        else:
            pdf_writer = pdf_global(pdfs, args, pdf_writer)

        with open(args.filename_string, 'wb') as out:
            pdf_writer.write(out)

    # Descending
    if args.order == 1:
        pdfs = pdfs[::-1]
        imgs = imgs[::-1]
        epubs = epubs[::-1]

        if args.imageonly == 1:
            pdf_writer = image_global(imgs, args, pdf_writer)

        elif args.image_pdf == 1:
            pdf_writer = pdf_global(pdfs, args, pdf_writer)
            pdf_writer = image_global(imgs, args, pdf_writer)

        elif args.epubonly == 1:
            pdf_writer = epub_global(epubs, args, pdf_writer)
        
        elif args.epub_pdf == 1:
            pdf_writer = epub_global(epubs, args, pdf_writer)
            pdf_writer = pdf_global(pdfs, args, pdf_writer)

        elif args.image_epub == 1:
            pdf_writer = image_global(imgs, args, pdf_writer)
            pdf_writer = epub_global(epubs, args, pdf_writer)
        
        elif args.all == 1:
            pdf_writer = pdf_global(pdfs, args, pdf_writer)
            pdf_writer = image_global(imgs, args, pdf_writer)
            pdf_writer = epub_global(epubs, args, pdf_writer)
            
        else:
            pdf_writer = pdf_global(pdfs, args, pdf_writer)

        with open(args.filename_string, 'wb') as out:
            pdf_writer.write(out)

    # Shuffle
    if args.order == 2:
        pdf_choice = []
        img_choice = []
        epub_choice = []

        count = 0
        for count in range(len(pdfs)):
            choice = random.choice(pdfs)
            pdf_choice.append(choice)
            pdfs.remove(choice)

        count = 0
        for count in range(len(imgs)):
            choice = random.choice(imgs)
            img_choice.append(choice)
            imgs.remove(choice)

        count = 0
        for count in range(len(epubs)):
            choice = random.choice(epubs)
            epub_choice.append(choice)
            epubs.remove(choice)


        if args.imageonly == 1:
            pdf_writer = image_global(img_choice, args, pdf_writer)

        elif args.image_pdf == 1:
            pdf_writer = pdf_global(pdf_choice, args, pdf_writer)
            pdf_writer = image_global(img_choice, args, pdf_writer)

        elif args.epubonly == 1:
            pdf_writer = epub_global(epubs, args, pdf_writer)

        elif args.epub_pdf == 1:
            pdf_writer = epub_global(epubs, args, pdf_writer)
            pdf_writer = pdf_global(pdfs, args, pdf_writer)

        elif args.image_epub == 1:
            pdf_writer = image_global(imgs, args, pdf_writer)
            pdf_writer = epub_global(epubs, args, pdf_writer)
        
        elif args.all == 1:
            pdf_writer = pdf_global(pdfs, args, pdf_writer)
            pdf_writer = image_global(imgs, args, pdf_writer)
            pdf_writer = epub_global(epubs, args, pdf_writer)

        else:
            pdf_writer = pdf_global(pdf_choice, args, pdf_writer)

        with open(args.filename_string, 'wb') as out:
            pdf_writer.write(out)


if __name__ == '__main__':
    main()
