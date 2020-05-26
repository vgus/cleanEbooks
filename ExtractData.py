from bs4 import BeautifulSoup

nombreArchivo = "IntroPreface"


with open("C:\\Users\\Uriel\\Downloads\\1995StaffordBeer\\content\\" + "0_1_6" + nombreArchivo + ".html", 'w') as cap:
    cap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    cap.write('<html xmlns="http://www.w3.org/1999/xhtml">\n')
    cap.write('<head>\n')
    cap.write('<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />\n')
    cap.write('<title>page_1</title>\n')
    cap.write('<link rel="stylesheet" href="stylesheet.css" type="text/css" />\n')
    cap.write('</head>\n')
    cap.write('<body style="margin:5px; padding: 5px;">\n')

    for i in ['ix','x','xi']:
        with open("C:\\Users\\Uriel\\Downloads\\1995StaffordBeer\\content\\page_" + str(i) + ".xml") as sf1:
            soup = BeautifulSoup(sf1, 'html.parser')
            for data in soup.find_all('font'):
                # print("<p>" + str(data) + "</p>")
                cap.write("<p>" + str(data) + "</p>\n")

    cap.write('</body>\n')
    cap.write('</html>\n')
