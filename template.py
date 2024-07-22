import pdfkit

# Spécifiez le chemin de votre fichier HTML

import pdfkit

path_wkthmltopdf = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

input_html = 'D:/Projets/EDU-Thementor/Student-Report-card/student_report_main.html'
output_pdf = 'sortie.pdf'
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-images': '',  # Ajoutez ceci pour désactiver le chargement des images
    'disable-javascript': '',  # Ajoutez ceci pour désactiver JavaScript
}

pdfkit.from_file(input_html, output_pdf, options=options, configuration=config)

print("La conversion est terminée. Le fichier PDF est enregistré à :", output_pdf)
