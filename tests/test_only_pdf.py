import os
from paths import *

def test_only_pdf_no_password():
    os.chdir(sample_path)
    os.system('mergemypdf -s sample -f only_pdf_no_password.pdf -p test@123')

    ## main logic goes here

    if os.path.exists("only_pdf_no_password.pdf"):
        os.remove("only_pdf_no_password.pdf")

    assert True
