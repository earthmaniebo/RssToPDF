import os
import requests
from xhtml2pdf import pisa
import xml.etree.ElementTree as ET


# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(sourceHtml, dest=resultFile)

    # close output file
    resultFile.close()

    # return True on success and False on errors
    return pisaStatus.err

# URL of RSS/Atom Feed
url = 'http://www.inquirer.net/fullfeed'

# Send get request 
resp = requests.get(url)

# Parse XML
# We can either save it in a file before reading or
# Read it directly from the response

# xml_doc = ET.fromstring(resp.content)
xml_doc = ET.parse('test.xml')

# List of dictionaries to store news
news = []

# Iterate over the item/entry tag
# <item> for RSS and <entry for Atom
for entity in xml_doc.iter('item'):
    # Store data from XML to variables
    title       = entity.find('title').text
    link        = entity.find('link').text
    pubDate     = entity.find('pubDate').text
    description = entity.find('description').text

    # Create dictionary and store the data
    headline = {
        'title'         : title,
        'link'          : link,
        'pubDate'       : pubDate,
        'description'   : description
    }

    # Add the dictionary to the list
    news.append(headline)

for article in news:
    print article['description']

sourceHtml = "<html><body><p>To PDF or not to PDF<p></body></html>"
srcHtml = 'test.html'
outputFilename = "test.pdf"

convertHtmlToPdf(srcHtml, outputFilename)
