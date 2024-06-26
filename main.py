import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of Filepaths
filepaths = glob.glob("files/*.txt")
print(filepaths)
# Create one pdf file
pdf = FPDF(orientation="p", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # Add a page in pdf file for each text file
    pdf.add_page()

    # Get filename without extension
    # and convert it to tile case

    filename = Path(filepath).stem
    name = filename.title()

    # Add name to pdf file
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(h=10, w=50, txt=name, ln=1)
    # Get content of text file
    with open(filepath, "r") as file:
        content = file.read()
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(txt=content, h=6, w=0)

# Produce the pdf

pdf.output("pdfs/output.pdf")



