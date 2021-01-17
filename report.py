import time

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.tables import TableStyle
doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
Story= []
logo = "python_logo.png"
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"
count = 1
owner = ['owner']

formatted_time = time.ctime()
full_name = "Mike Driscoll"
address_parts = ["411 State St.", "Marshalltown, IA 50158"]

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

ptext = '<font size="12"><b>Department of Agriculture and Farmers Welfare, Haryana</b></font>'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 18))

ptext = '<font size="10"><b>Serial No.</b> %s</font>' % count
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 18))

ptext = '<font size="10"><b>Date</b> %s</font>' % formatted_time
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 18))

ptext = '<font size="10">Given information is provided by HARSAC about the detected Active fire location</font>'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 18))
data = [
    ['SNo', 'District', 'Block Name', 'Village Name', 'Longitude', 'Latitude', 'Acq Date', 'Acq Time', 'Murraba no.',
     'Kila no.'], ['00', '01', '02', '03', '04']]

t = Table(data)
t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black)]))
Story.append(t)
Story.append(Spacer(1, 18))

ptext = '<font size="12"><b>List of owner:</b></font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 25))


t = Table(owner)
t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black)]))
Story.append(t)
Story.append(Spacer(1, 18))

ptext = '<font size="12">Yor are advised to act accordingly, and immediately.</font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 18))

ptext = '<font size="10"><b>Department of Agriculture and Farmers Welfare, Haryana</b></font>'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 25))
doc.build(Story)
