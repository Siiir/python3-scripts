import os
from PyPDF2 import PdfMerger
dir_path= r"I:\HPSCANS"
out_name= "Przebieg choroby"

pdfm= PdfMerger()
for i in range(8, 10):
    pdfm.append(
        os.path.join(dir_path, f"scan{i:0>4d}.pdf")
    )

pdfm.write(
    os.path.join(dir_path, out_name+".pdf")
)
pdfm.close()
