def extract(paginas, directorio, prefijoArchivo, nombreArchivo):
    from bs4 import BeautifulSoup, Tag, UnicodeDammit
    import re, os

    noEsPuntoFinal = re.compile('[^.?:\']$')
    textoImagen = re.compile(r'(Table)|(Figure)\D+(\xa0)*\d+.')
    esSeccion = re.compile(r'[0-9].\s\'?[A-Z]')
    esSubseccion = re.compile(r'\([a-z]\)\s+[A-Z]')
    esCapitulo = re.compile(r'PART\s[A-Z]+')
    mydir = os.path.abspath(os.path.dirname(__file__))
    parrafo = ''
    esParrafo = False
    sigueImagen = False

    with open(directorio + prefijoArchivo + nombreArchivo + ".html", 'w') as cap:
        cap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        cap.write('<html xmlns="http://www.w3.org/1999/xhtml">\n')
        cap.write('<head>\n')
        cap.write('<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />\n')
        cap.write(
            '<title>Decision and Control: The meaning of Operational Research and Management Cybernetics</title>\n')
        cap.write('<link rel="stylesheet" href="SBDecisionandControl.css" type="text/css" />\n')
        cap.write('</head>\n')
        cap.write('<body style="margin:5px; padding: 5px;">\n')

        # Para el manejo de las imagenes, se cambia el padre por <font> a excepción de que sea <i>
        for i in paginas:
            with open(os.path.join(mydir, '..', '1995StaffordBeer', 'OEBPS', 'oldData',
                                   'page_' + str(i) + ".xml")) as sf1:
                soup = BeautifulSoup(sf1, 'html.parser')
                for img in soup.find_all('img'):
                    src = img['src']
                    img['src'] = 'images/' + src
                    parent = img.parent
                    width = img['width']
                    if (parent.name == 'td'):
                        parent.name = 'font'
                        parent['face'] = 'imagen'
                    if (parent.parent.name == 'font'):
                        parent.parent['size'] = '6'
                    if (float(width) > 100):
                        parent['size'] = '6'
                    else:
                        parent['size'] = '3'
                    # print(img.parent.parent)

                # cadena = '<td><font face="Times New Roman, Times, Serif" size="3">We are concerned with times, which are numbered consecutively 0, 1, 2, 3, 4 and so on. Typically, the time is t, and the time before it <i>t-1;</i> so the gap between them prescribes a basic interval, typically the <i>t</i>th interval. There is a range of activities which could occur in this interval, and a range of items which could be manufactured too. These could all be nominated by a string of consecutive numbers as well; but typically there is a jth activity and an ith item. Now if an increment a is defined as an addition to the cumulative flow function through the works, it must relate to a certain time interval, and it may pair off any item with any activity. The whole range of such possibilities is written </font><font face="Symbol" size="3"><i>a</i></font><i><font face="Times New Roman, Times, Serif" size="1"><sub>ij</sub></font><sub><font face="Times New Roman, Times, Serif" size="2">(t)</font></sub></i><sub><font face="Times New Roman, Times, Serif" size="2"></font></sub><sub><font face="Times New Roman, Times, Serif" size="2"></font><font face="Times New Roman, Times, Serif" size="3"> Similarly, a decrement <img src="6b58e80766105c011135240bb26d95b7.gif" border="0" alt="C0159-01.gif" width="10" height="12" /> is defined as subtracting from the cumulative flow; its particulars are specified in the same way. The first is an input coefficient, occurring at the end of the interval. The unknown, x (or series <i>of xs),</i> which must be calculated is in this case the number of units of each item that must be produced by each activity. The following expression accounts precisely for the equilibrial condition (that is, that the input to and the output from the system must match) of the dynamic system described above:</font></sub></td>'
                # soup = BeautifulSoup(cadena, 'html.parser')

                for data in soup.find_all('font'):
                    if (data['size'] == "2" and data.get_text()[0:4] == "Page"):  # Para eliminar el dato de páginas
                        # cap.write(str(data) + "\n")
                        continue
                    elif (data['size'] == "0"):  # para eliminar los saltos entre parrafo
                        continue
                    elif (data['size'] == "2" and textoImagen.match(UnicodeDammit.detwingle(data.get_text()))
                            # (textoImagen.match(data.get_text()))
                    ):  # para las tablas
                        data.name = "p"
                        data['class'] = "center"
                        del data['size']
                        del data['face']
                        cap.write(str(data) + "\n")
                        sigueImagen = False
                        continue
                    elif (data['size'] == "2" and data.contents == []):  # para los superindices vacios
                        continue
                    elif (data['size'] == "2" and
                          isinstance(data.contents[0], Tag) and
                          data.contents[0].name == 'sup'):  # para los superindices
                        linea = ''
                        for child in data.children:
                            linea = linea + str(child)
                        parrafo = parrafo + linea
                    elif (data['size'] == "1" and data.contents == []):  # para los subindices vacios
                        continue
                    elif (data['size'] == "1" and
                          isinstance(data.contents[0], Tag) and
                          data.contents[0].name == 'sub'):  # para los subindices
                        linea = ''
                        for child in data.children:
                            linea = linea + str(child)
                        parrafo = parrafo + linea
                    elif (data['size'] == "2" and data.parent.name == 'sub'):  # para superindices solos
                        data.name = "sub"
                        del data['size']
                        del data['face']
                        linea = str(data)
                        # for child in data.children:
                        #    linea = linea + str(child)
                        parrafo = parrafo + linea
                    elif (data['size'] == "2"):  # para las tablas
                        data.name = "p"
                        data['class'] = "bl_extract"
                        del data['size']
                        del data['face']
                        cap.write(str(data) + '<br/>' + "\n")
                        # cap.write(data.get_text() + "\n")
                    elif (data["size"] == "6"): #Para obtener las imagenes preprocesadas
                        data.name = "p"
                        data['class'] = "center"
                        del data['size']
                        del data['face']
                        cap.write(str(data) + "\n")
                    elif (data["size"] == "3" and esSeccion.match(data.get_text())):  # Para los subtitulos
                        data.name = "h2"
                        data['class'] = "section"
                        del data['size']
                        del data['face']
                        cap.write(str(data) + "\n")
                    elif (data["size"] == "3" and esSubseccion.search(data.get_text())):  # Para los subsecciones
                        data.name = "h3"
                        data['class'] = "section"
                        del data['size']
                        del data['face']
                        cap.write(str(data) + "\n")
                    elif (data["size"] == "3" and data['face'] == 'Symbol'):
                        if (esParrafo):
                            # linea = data.get_text()
                            linea = str(data)
                            parrafo = parrafo + linea
                            print('Symbol: ' + data.get_text())
                        else:
                            cap.write('Symbol: ' + str(data) + "\n")
                            print('Symbol: ' + data.get_text())
                            continue
                    elif (data["size"] == "3" and data.contents == []):
                        continue
                    elif (data["size"] == "3" and esParrafo):  # Para unir los parrafos
                        data.name = "p"
                        data['class'] = "indent"
                        del data['size']
                        del data['face']
                        if (noEsPuntoFinal.search(data.get_text().rstrip())):
                            linea = ''
                            for child in data.children:
                                linea = linea + str(child)
                            parrafo = parrafo + linea + " "
                            # cap.write("Entre Parrafo: " + str(parrafo) + "\n")
                        else:
                            esParrafo = False
                            linea = ""
                            for child in data.children:
                                linea = linea + str(child)
                            parrafo = parrafo + linea
                            cap.write('<p class="indent">' + str(parrafo) + "</p>\n")
                            parrafo = ''
                    elif (data["size"] == "3"):  # Para los parrafos del libro
                        data.name = "p"
                        data['class'] = "indent"
                        del data['size']
                        del data['face']
                        if noEsPuntoFinal.search(data.get_text().rstrip()):  # Busca si es punto final
                            esParrafo = True
                            linea = ""
                            for child in data.children:
                                linea = linea + str(child)
                                # cap.write("Children: " + str(child) + "\n")
                            parrafo = linea + " "
                            # cap.write("Inicio Parrafo: "+str(parrafo) + "\n")
                            continue
                        cap.write(str(data) + "\n")
                    elif (data['size'] == "4"):  # Para los títulos y encabezados
                        data.name = "h1"
                        if(esCapitulo.match(data.get_text())):
                            data['class'] = 'chapter1'
                        else:
                            data['class'] = 'section'
                        del data['size']
                        del data['face']
                        cap.write(str(data) + "\n")
                    else:  # Por si pasa algo
                        data.name = "p"
                        cap.write(str(data) + "\n")

        cap.write('</body>\n')
        cap.write('</html>\n')


def extractOther(paginas, directorio, prefijoArchivo, nombreArchivo, nombreClase = 'nonindent'):
    from bs4 import BeautifulSoup
    import os

    mydir = os.path.abspath(os.path.dirname(__file__))

    with open(directorio + prefijoArchivo + nombreArchivo + ".html", 'w') as cap:
        cap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        cap.write('<html xmlns="http://www.w3.org/1999/xhtml">\n')
        cap.write('<head>\n')
        cap.write('<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />\n')
        cap.write(
            '<title>Decision and Control: The meaning of Operational Research and Management Cybernetics</title>\n')
        cap.write('<link rel="stylesheet" href="SBDecisionandControl.css" type="text/css" />\n')
        cap.write('</head>\n')
        cap.write('<body style="margin:5px; padding: 5px;">\n')

        for i in paginas:
            with open(os.path.join(mydir, '..', '1995StaffordBeer', 'OEBPS', 'oldData',
                                   'page_' + str(i) + ".xml")) as sf1:

                soup = BeautifulSoup(sf1, 'html.parser')

                for img in soup.find_all('img'):
                    src = img['src']
                    img['src'] = 'images/' + src
                    parent = img.parent
                    parent['size'] = '6'

                for data in soup.find_all('font'):
                    if (data['size'] == "2" and data.get_text()[0:4] == "Page"):  # Para eliminar el dato de páginas
                        # cap.write(str(data) + "\n")
                        continue
                    elif (data['size'] == "6"):
                        data.name = "p"
                        data['class'] = "center"
                        del data['size']
                        del data['face']
                        cap.write(str(data) + "\n")
                    else:
                        data.name = "p"
                        data['class'] = nombreClase
                        del data['size']
                        del data['face']
                        cap.write(str(data) + "\n")

        cap.write('</body>\n')
        cap.write('</html>\n')


