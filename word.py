from pdf2docx import Converter

old_pdf = "Contour.pdf"
new_doc = "new.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()




