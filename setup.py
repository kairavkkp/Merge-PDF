import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mergemypdf",
    version="0.0.2",
    author="kairavkkp",
    author_email="kairavpithadia13@gmail.com",
    description="Merge PDFs using CLI with customizations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/kairavkkp/Merge-PDF",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    keywords="Merge-pdf PDF-CLI merge pdf merge-pdf-local offline-merge pdf-merge",

    entry_points={
        "console_scripts": ['mergemypdf = merge_pdf.merge_pdf:main'],
    },
    python_requires='>=3.6',
    install_requires=[
        'PyPDF2==1.26.0'
    ],
)