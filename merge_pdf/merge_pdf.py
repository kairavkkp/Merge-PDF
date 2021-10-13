import os
import argparse
import re
import random
import re
import uuid
import fitz
from getpass import getpass

image_extns = ['jpg', 'jpeg', 'tiff', 'png', 'gif']

def pdf_global(pdfs, args, pdf_writer):
    cnt = 0
    for pdf in pdfs:
        doc = fitz.open(pdf)
        if doc.is_encrypted:
            if args.password:
                rc = doc.authenticate(args.password)
                if not rc > 0:
                    raise ValueError("wrong password")
            else:
                password = getpass(f"{pdf} is encrypted. Please enter password: ")
                rc = doc.authenticate(password)
                if not rc > 0:
                    raise ValueError("wrong password")

        if cnt == args.count:
            break

        if args.start_string == None and args.end_string == None and args.contains == None:
            pdf_writer.insert_pdf(doc)
            cnt += 1
        # With end or start strings
        else:
            # Starts
            if args.start_string is not None:
                #print('DEBUG: Entered StartsWith Portion')
                if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+', pdf[:-4], re.IGNORECASE):
                    pdf_writer.insert_pdf(doc)
                    cnt += 1

            if args.end_string is not None:
                #print('DEBUG: Entered EndsWith Portion')
                if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$', pdf[:-4], re.IGNORECASE):
                    pdf_writer.insert_pdf(doc)
                    cnt += 1

            if args.contains is not None:
                #print('DEBUG: Entered Contains Portion')
                if re.search(re.escape(str(args.contains)), pdf[:-4], re.IGNORECASE):
                    pdf_writer.insert_pdf(doc)
                    cnt += 1


def epub_global(epubs, args, pdf_writer):
    cnt = 0
    for epub in epubs:     
        if cnt == args.count:
            break
        if args.start_string == None and args.end_string == None and args.contains == None:
            doc = fitz.open(epub)
            pdfbytes = doc.convert_to_pdf()
            doc.close()
            epubPDF = fitz.open("pdf", pdfbytes)
            pdf_writer.insert_pdf(epubPDF)
            cnt += 1
        # With end or start strings
        else:
            # Starts
            if args.start_string is not None:
                #print('DEBUG: Entered StartsWith Portion')
                if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+', epub[:-5], re.IGNORECASE):
                    doc = fitz.open(epub)
                    pdfbytes = doc.convert_to_pdf()
                    doc.close()
                    epubPDF = fitz.open("pdf", pdfbytes)
                    pdf_writer.insert_pdf(epubPDF)
                    cnt += 1
            if args.end_string is not None:
                #print('DEBUG: Entered EndsWith Portion')
                if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$', epub[:-5], re.IGNORECASE):
                    doc = fitz.open(epub)
                    pdfbytes = doc.convert_to_pdf()
                    doc.close()
                    epubPDF = fitz.open("pdf", pdfbytes)
                    pdf_writer.insert_pdf(epubPDF)
                    cnt += 1
            if args.contains is not None:
                #print('DEBUG: Entered Contains Portion')
                if re.search(re.escape(str(args.contains)), epub[:-5], re.IGNORECASE):
                    doc = fitz.open(epub)
                    pdfbytes = doc.convert_to_pdf()
                    doc.close()
                    epubPDF = fitz.open("pdf", pdfbytes)
                    pdf_writer.insert_pdf(epubPDF)             
                    cnt += 1

def image_global(imgs, args, pdf_writer, count=-1):
    cnt = 0
    for img in imgs:
        if cnt == args.count:
            break
        if args.start_string == None and args.end_string == None and args.contains == None:
            img = fitz.open(img) # open pic as document
            rect = img[0].rect # pic dimension
            pdfbytes = img.convert_to_pdf() # make a PDF stream
            img.close() # no longer needed
            imgPDF = fitz.open("pdf", pdfbytes) # open stream as PDF
            page = pdf_writer.new_page(width = rect.width, height = rect.height) # new page with pic dimensions
            page.show_pdf_page(rect, imgPDF, 0) # image fills the page
            cnt += 1
         # With end or start strings
        else:
            # Starts
            if args.start_string is not None:
                #print('DEBUG: Entered StartsWith Portion')
                if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+', img[:-4], re.IGNORECASE):
                    img = fitz.open(img) # open pic as document
                    rect = img[0].rect # pic dimension
                    pdfbytes = img.convert_to_pdf() # make a PDF stream
                    img.close() # no longer needed
                    imgPDF = fitz.open("pdf", pdfbytes) # open stream as PDF
                    page = pdf_writer.new_page(width = rect.width, height = rect.height) # new page with pic dimensions
                    page.show_pdf_page(rect, imgPDF, 0) # image fills the page
                    cnt += 1
            if args.end_string is not None:
                #print('DEBUG: Entered EndsWith Portion')
                if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$', img[:-4], re.IGNORECASE):
                    img = fitz.open(img) # open pic as document
                    rect = img[0].rect # pic dimension
                    pdfbytes = img.convert_to_pdf() # make a PDF stream
                    img.close() # no longer needed
                    imgPDF = fitz.open("pdf", pdfbytes) # open stream as PDF
                    page = pdf_writer.new_page(width = rect.width, height = rect.height) # new page with pic dimensions
                    page.show_pdf_page(rect, imgPDF, 0) # image fills the page
                    cnt += 1
            if args.contains is not None:
                #print('DEBUG: Entered Contains Portion')
                if re.search(re.escape(str(args.contains)), img[:-4], re.IGNORECASE):
                    img = fitz.open(img) # open pic as document
                    rect = img[0].rect # pic dimension
                    pdfbytes = img.convert_to_pdf() # make a PDF stream
                    img.close() # no longer needed
                    imgPDF = fitz.open("pdf", pdfbytes) # open stream as PDF
                    page = pdf_writer.new_page(width = rect.width, height = rect.height) # new page with pic dimensions
                    page.show_pdf_page(rect, imgPDF, 0) # image fills the page
                    cnt += 1

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

    pdf_writer = fitz.open()

    pdfs = sorted([x for x in os.listdir() if ('.pdf' in x.lower())])
    imgs = sorted([x for x in os.listdir() if (
        x.lower().split('.')[-1] in image_extns)])
    epubs = sorted([x for x in os.listdir() if ('.epub' in x.lower())])

    # Ascending
    if args.order == 0:
        if args.imageonly == 1:
            image_global(imgs, args, pdf_writer)

        elif args.image_pdf == 1:
            pdf_global(pdfs, args, pdf_writer)
            image_global(imgs, args, pdf_writer)

        elif args.epubonly == 1:
            epub_global(epubs, args, pdf_writer)
        
        elif args.epub_pdf == 1:
            epub_global(epubs, args, pdf_writer)
            pdf_global(pdfs, args, pdf_writer)

        elif args.image_epub == 1:
            image_global(imgs, args, pdf_writer)
            epub_global(epubs, args, pdf_writer)
        
        elif args.all == 1:
            pdf_global(pdfs, args, pdf_writer)
            image_global(imgs, args, pdf_writer)
            epub_global(epubs, args, pdf_writer)
        
        else:
            pdf_global(pdfs, args, pdf_writer)
            
        pdf_writer.save(args.filename_string)

    # Descending
    if args.order == 1:
        pdfs = pdfs[::-1]
        imgs = imgs[::-1]
        epubs = epubs[::-1]

        if args.imageonly == 1:
            image_global(imgs, args, pdf_writer)

        elif args.image_pdf == 1:
            pdf_global(pdfs, args, pdf_writer)
            image_global(imgs, args, pdf_writer)

        elif args.epubonly == 1:
            epub_global(epubs, args, pdf_writer)
        
        elif args.epub_pdf == 1:
            epub_global(epubs, args, pdf_writer)
            pdf_global(pdfs, args, pdf_writer)

        elif args.image_epub == 1:
            image_global(imgs, args, pdf_writer)
        
        elif args.all == 1:
            pdf_global(pdfs, args, pdf_writer)
            image_global(imgs, args, pdf_writer)
            epub_global(epubs, args, pdf_writer)
        
        else:
            pdf_global(pdfs, args, pdf_writer)
            
        pdf_writer.save(args.filename_string)

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
            image_global(imgs, args, pdf_writer)

        elif args.image_pdf == 1:
            pdf_global(pdfs, args, pdf_writer)
            image_global(imgs, args, pdf_writer)

        elif args.epubonly == 1:
            epub_global(epubs, args, pdf_writer)
        
        elif args.epub_pdf == 1:
            epub_global(epubs, args, pdf_writer)
            pdf_global(pdfs, args, pdf_writer)

        elif args.image_epub == 1:
            image_global(imgs, args, pdf_writer)
            epub_global(epubs, args, pdf_writer)
        
        elif args.all == 1:
            pdf_global(pdfs, args, pdf_writer)
            image_global(imgs, args, pdf_writer)
            epub_global(epubs, args, pdf_writer)
        
        else:
            pdf_global(pdfs, args, pdf_writer)
        
        pdf_writer.save(args.filename_string)


if __name__ == '__main__':
    main()
