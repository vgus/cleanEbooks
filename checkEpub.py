import os.path, shutil
from lxml import etree

def find_resources(path ='/path/to/our/epub/directory'):
    opf = etree.parse(os.path.join(path, 'OEBPS', 'content.opf'))

    # All the opf:item elements are resources
    for item in opf.xpath('//opf:item',
                          namespaces= { 'opf': 'http://www.idpf.org/2007/opf' }):

        # If the resource was not already created by DocBook XSL itself,
        # copy it into the OEBPS folder
        href = item.attrib['href']
        referenced_file = os.path.join(path, 'OEBPS', href):
        if not os.path.exists(referenced_file):
            shutil.copy(href, os.path.join(path, 'OEBPS'))