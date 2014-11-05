import os
import sys
import smtplib
import requests
from xhtml2pdf import pisa
import xml.etree.ElementTree as ET
from feed_list import feeds
from mail import sendemail

# Utility function for converting HTML to PDF
def convertHtmlToPdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(source_html, dest=result_file)
    result_file.close()

    return pisa_status.err

# Iterate each feed urls
for feed in feeds:
    feed_url = feed['url']
    feed_type = feed['type']

    # Send get request 
    resp = requests.get(feed_url)

    # Parse XML
    # We can either save it in a file before reading or
    # Read it directly from the response

    # xml_doc = ET.fromstring(resp.content)
    xml_doc = ET.parse('test.xml')

    # Iterate over the item/entry tag
    # <item> for RSS and <entry for Atom
    for entity in xml_doc.iter('item'):
        # Store data from XML to variables
        title       = entity.find('title').text
        link        = entity.find('link').text
        pubDate     = entity.find('pubDate').text
        description = entity.find('description').text

        source_html = """
            <html>
            <head>
                <style type="text/css">
                    h1 {
                        color:red;
                    }
                    body {
                        margin: 100px;
                    }
                    td, p{
                        font-size: 16px;
                    }
                    #article{
                    }
                    #label{
                        color:#59C;
                        text-transform: uppercase;
                        font-weight: bold;
                    }
                    a{
                    color: #000;
                    }
                </style>
            </head>
            <body>
                <div class="article">  
                    <table>
                        <tr>
                            <td id="label">
                                Date: 
                            </td>
                            <td>""" + pubDate + """</td>
                        </tr>
                        <tr>
                            <td id="label">
                                Classification: 
                            </td>
                            <td>
                            </td>
                        </tr>
                        <tr>
                            <td id="label">
                                Publication: 
                            </td>
                            <td>""" + title + """</td>
                        </tr>
                        <tr>
                            <td id="label">
                                Title:
                            </td>
                            <td>""" + title + """</td>
                        </tr>
                        <tr>
                            <td id="label">
                                Writer
                            </td>
                            <td>""" + title + """</td>
                        </tr>
                    </table>
                    <p>""" + description + """</p>
            </body>
            </html>
        """
        srcHtml = 'test.html'
        output_filename = title + '.pdf'

        convertHtmlToPdf(source_html, output_filename)

        sendemail(from_addr    = 'earthmaniebo@gmail.com', 
                  to_addr_list = ['earth@codesignate.com'],
                  cc_addr_list = ['earthmaniebo@gmail.com'], 
                  subject      = 'Howdy', 
                  message      = 'Howdy from a python function',
                  pdf_file     = output_filename,
                  login        = 'earthmaniebo', 
                  password     = 'thisissp@rt@')