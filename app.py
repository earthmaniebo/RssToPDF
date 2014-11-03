import os
import requests
import xml.etree.ElementTree as ET

url = 'http://www.inquirer.net/fullfeed'
resp = requests.get(url)

# xml_doc = ET.fromstring(resp.content)
xml_doc = ET.parse('test.xml')




for entity in xml_doc.iter('item'):
    print entity.find("title").text
    print entity.find("description").text
    print entity.find("link").text
    print entity.find("pubDate").text