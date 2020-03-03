import os
import argparse
import re
import logging
from PyPDF2 import PdfFileReader, PdfFileWriter
import random
import re
import uuid


def main():        

    parser = argparse.ArgumentParser(description='A package which merges all PDFs from a folder into a single PDF.')
    parser.add_argument('-c','--count',action='store',dest='count',type=int,
            help='Total number of PDFs to be merged. Default is all.')#fixed count, all

    parser.add_argument('-o','--order',action='store',dest='order',type=int,default=0,
            help='Order in which PDFs need to be merged. 0 is Ascending, 1 is descending and 2 is shuffle.')#ascending, descending, shuffle

    parser.add_argument('-s','--startswith',action='store',dest='start_string',
            help='Only merge PDFs whose names startswith provided strings.')# default None
    parser.add_argument('-e','--endswith',action='store',dest='end_string'
            ,help='Only merge PDFs whose names startswith provided strings.')#default None
    parser.add_argument('-cn','--contains',action='store',dest='contains'
            ,help='Only merge PDFs whose names contains provided strings.')#default None
    parser.add_argument('-f','--filename',action='store',dest='filename_string',default=str(uuid.uuid4()).split('-')[0]+'.pdf'
            ,help='Filename of the merged PDF. Default is randomly generated names.')



    args = parser.parse_args()
    print(args)

    #print(args)

    os.chdir(os.getcwd())

    pdf_writer = PdfFileWriter()

    ## If no count mentioned
    if args.count == None:
        #Ascending
        if args.order == 0:
            pdfs = sorted([x for x in os.listdir() if ('.pdf' in x)])
            for pdf in pdfs:
                if '.pdf' in pdf:
                    if args.start_string == None and args.end_string == None and args.contains == None:
                        pdf_reader = PdfFileReader(pdf)
                        for page in range(pdf_reader.getNumPages()):
                            pdf_writer.addPage(pdf_reader.getPage(page))
                    
                    #With end or start strings
                    else:
                        #Starts
                
                        if args.start_string is not None:
                            #print('DEBUG: Entered StartsWith Portion')

                            if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+',pdf[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(pdf)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))


                        if args.end_string is not None:
                            #print('DEBUG: Entered EndsWith Portion')

                            if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$',pdf[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(pdf)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))

                        
                        if args.contains is not None:
                            #print('DEBUG: Entered Contains Portion')

                            if re.search(re.escape(str(args.contains)),pdf[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(pdf)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))

        

            with open(args.filename_string, 'wb') as out:
                pdf_writer.write(out)

        #Descending
        if args.order == 1:
            pdfs = [x for x in os.listdir() if ('.pdf' in x)]
            
            for pdf in pdfs[::-1]:
                if '.pdf' in pdf:

                    if args.start_string == None and args.end_string == None and args.contains == None:

                        pdf_reader = PdfFileReader(pdf)
                        for page in range(pdf_reader.getNumPages()):
                            pdf_writer.addPage(pdf_reader.getPage(page))

                    else:
                        #Starts
                
                        if args.start_string is not None:
                            #print('DEBUG: Entered StartsWith Portion')

                            if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+',pdf[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(pdf)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))


                        if args.end_string is not None:
                            #print('DEBUG: Entered EndsWith Portion')

                            if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$',pdf[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(pdf)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))

                        
                        if args.contains is not None:
                            #print('DEBUG: Entered Contains Portion')

                            if re.search(re.escape(str(args.contains)),pdf[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(pdf)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))


            with open(args.filename_string, 'wb') as out:
                pdf_writer.write(out)

        #Shuffle
        if args.order == 2:
            pdfs = [x for x in os.listdir() if ('.pdf' in x)]
            for count in range(len(pdfs)):
                choice = random.choice(pdfs)

                if args.start_string == None and args.end_string == None and args.contains == None:

                    pdf_reader = PdfFileReader(choice)
                    pdfs.remove(choice)
                    for page in range(pdf_reader.getNumPages()):
                        pdf_writer.addPage(pdf_reader.getPage(page))

                else:
                    #Starts
                
                        if args.start_string is not None:
                            #print('DEBUG: Entered StartsWith Portion')

                            if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+',choice[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(choice)
                                pdfs.remove(choice)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))


                        if args.end_string is not None:
                            #print('DEBUG: Entered EndsWith Portion')

                            if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$',choice[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(choice)
                                pdfs.remove(choice)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))

                        
                        if args.contains is not None:
                            #print('DEBUG: Entered Contains Portion')

                            if re.search(re.escape(str(args.contains)),choice[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(choice)
                                pdfs.remove(choice)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))




            
            with open(args.filename_string, 'wb') as out:
                pdf_writer.write(out)

            

    else:
        ## Count is within range of the available PDFs
        if args.count <= len(os.listdir()):

            #Ascending
            if args.order == 0:
                pdfs = sorted([x for x in os.listdir() if ('.pdf' in x)])

                cnt = 0
                for pdf in pdfs:
                    if pdf[-3:] == 'pdf':
                        if args.start_string == None and args.end_string == None and args.contains == None:
                            pdf_reader = PdfFileReader(pdf)
                            for page in range(pdf_reader.getNumPages()):
                                pdf_writer.addPage(pdf_reader.getPage(page))
                            cnt+=1
                        if cnt == args.count:
                                break


                        else:
                            if args.start_string is not None:
                            #print('DEBUG: Entered StartsWith Portion')

                                if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+',pdf[:-4],re.IGNORECASE):
                                    pdf_reader = PdfFileReader(pdf)
                                    for page in range(pdf_reader.getNumPages()):
                                        pdf_writer.addPage(pdf_reader.getPage(page))
                                    cnt+=1
                                if cnt == args.count:
                                        break

                            if args.end_string is not None:
                            #print('DEBUG: Entered EndsWith Portion')

                                if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$',pdf[:-4],re.IGNORECASE):
                                    pdf_reader = PdfFileReader(pdf)
                                    for page in range(pdf_reader.getNumPages()):
                                        pdf_writer.addPage(pdf_reader.getPage(page))
                                    cnt+=1
                                if cnt == args.count:
                                        break

                            if args.contains is not None:
                                if re.search(re.escape(str(args.contains)),pdf[:-4],re.IGNORECASE):
                                    pdf_reader = PdfFileReader(pdf)
                                    for page in range(pdf_reader.getNumPages()):
                                        pdf_writer.addPage(pdf_reader.getPage(page))
                                    cnt+=1
                                if cnt == args.count:
                                        break






                with open(args.filename_string, 'wb') as out:
                    pdf_writer.write(out)
            
            #Descending
            if args.order == 1:
                pdfs = [x for x in os.listdir() if ('.pdf' in x)]

                cnt = 0
                for pdf in pdfs[::-1]:
                    if pdf[-3:] == 'pdf':

                        if args.start_string == None and args.end_string == None and args.contains == None:
                            pdf_reader = PdfFileReader(pdf)
                            for page in range(pdf_reader.getNumPages()):
                                pdf_writer.addPage(pdf_reader.getPage(page))
                            cnt+=1
                        if cnt == args.count:
                            break  

                        else:
                            if args.start_string is not None:
                            #print('DEBUG: Entered StartsWith Portion')

                                if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+',pdf[:-4],re.IGNORECASE):
                                    pdf_reader = PdfFileReader(pdf)
                                    for page in range(pdf_reader.getNumPages()):
                                        pdf_writer.addPage(pdf_reader.getPage(page))
                                    cnt+=1
                                if cnt == args.count:
                                        break
                                
                            if args.end_string is not None:
                            #print('DEBUG: Entered EndsWith Portion')

                                if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$',pdf[:-4],re.IGNORECASE):
                                    pdf_reader = PdfFileReader(pdf)
                                    for page in range(pdf_reader.getNumPages()):
                                        pdf_writer.addPage(pdf_reader.getPage(page))
                                    cnt+=1
                                if cnt == args.count:
                                        break

                            if args.contains is not None:
                                if re.search(re.escape(str(args.contains)),pdf[:-4],re.IGNORECASE):
                                    pdf_reader = PdfFileReader(pdf)
                                    for page in range(pdf_reader.getNumPages()):
                                        pdf_writer.addPage(pdf_reader.getPage(page))
                                    cnt+=1
                                if cnt == args.count:
                                        break

                            


                with open(args.filename_string, 'wb') as out:
                    pdf_writer.write(out)

            #Shuffle
            if args.order == 2:
                cnt = 0

                pdfs = [x for x in os.listdir() if ('.pdf' in x)]
                for count in range(args.count):
                    choice = random.choice(pdfs)

                    if args.start_string == None and args.end_string == None and args.contains == None:
                        pdf_reader = PdfFileReader(choice)
                        pdfs.remove(choice)
                        for page in range(pdf_reader.getNumPages()):
                            pdf_writer.addPage(pdf_reader.getPage(page))
                        cnt+=1
                    
                    if cnt == args.count:
                        break

                    else:
                        if args.start_string is not None:
                            #print('DEBUG: Entered StartsWith Portion')

                            if re.search(r'^'+re.escape((args.start_string))+r'[\w+\s+\d+]+',choice[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(choice)
                                pdfs.remove(choice)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))
                                cnt+=1
                    
                            if cnt == args.count:
                                break


                        if args.end_string is not None:
                            #print('DEBUG: Entered EndsWith Portion')

                            if re.search(r'[\d+\w+\s+]'+re.escape(str(args.end_string))+r'$',choice[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(choice)
                                pdfs.remove(choice)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))
                                cnt+=1
                    
                            if cnt == args.count:
                                break

                        
                        if args.contains is not None:
                            #print('DEBUG: Entered Contains Portion')
                            if re.search(re.escape(str(args.contains)),choice[:-4],re.IGNORECASE):
                                pdf_reader = PdfFileReader(choice)
                                pdfs.remove(choice)
                                for page in range(pdf_reader.getNumPages()):
                                    pdf_writer.addPage(pdf_reader.getPage(page))
                                cnt+=1
                    
                            if cnt == args.count:
                                break

                    
                with open(args.filename_string, 'wb') as out:
                    pdf_writer.write(out)


            


        ##Count out of range
        else:
            print('Count is more than available PDFs.')

        
if __name__ == '__main__':
    main()






            



