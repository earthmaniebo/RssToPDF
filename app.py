import os
import pdfkit
import requests
import xml.etree.ElementTree as ET

# URL of RSS/Atom Feed
url = 'http://www.inquirer.net/fullfeed'

# Send get request 
resp = requests.get(url)

# Parse XML
# We can either save it in a file before reading or
# Read it directly from the response

# xml_doc = ET.fromstring(resp.content)
xml_doc = ET.parse('test.xml')

# Nested dictionary to store news
news = []
indentifier_str =  'headline'
counter = 0

for entity in xml_doc.iter('item'):
    
    # Generate the unique name of the index
    counter = counter + 1
    index = indentifier_str + str(counter)

    # Dictionary to store inside the news dictionary
    title       = entity.find("title").text
    link        = entity.find("link").text
    pubDate     = entity.find("pubDate").text
    description = entity.find("description").text

    headline = {
        'title' : title,
        'link' : link,
        'pubDate' : pubDate,
        'description' : description
    }

    news.append(headline)

for d in news:



# pdfkit.from_url('http://www.inquirer.net/fullfeed', 'out.pdf')