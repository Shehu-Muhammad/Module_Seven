def printHtmlOpeningAndHeadSection(title, css):
    htmlOpening = ["<!DOCTYPE html>", "<head>", "<title>", title, "</title>", css, "</head>", "<body>"]
    for tag in htmlOpening:
        file = open("index.html", 'a')
        if(tag == "<head>" or tag == "</head>" or tag == "<body>"):
            file.write("\n\t")
        elif(tag == "<title>" or tag == css):
            file.write("\n\t\t")
        file.write(tag)
        file.close()
        
def printHtmlBodyContent():
    htmlBody = ["<div>","</div>"]
    for tag in htmlBody:
        file = open("index.html", "a")
        if(tag == "<div>" or tag == "</div>"):
            file.write("\n\t\t")
        file.write(tag)
        file.close()

def printHtmlFooterAndClosingTags(footer):
    htmlFooter = ["<footer>", footer, "</footer>", "</body>","</html>"]
    for tag in htmlFooter:
        file = open("index.html", "a")
        if(tag == "<footer>"):
            file.write("\n\t\t")
        elif(tag == "</body>"):
            file.write("\n\t")
        elif(tag == "</html>"):
            file.write("\n")
        file.write(tag)
        file.close()

# print html header section with title <!DOCTYPE html><head><title>title</title></head><body>

# print html body section <body>

# print information for body section divs, images, uls, lis

# print html footer section <footer></footer></body></html>

# print css file
