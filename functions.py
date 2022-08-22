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
        
def printHtmlBodyContent(imageSource, imageAlt, paragraph):
    outerDiv = "<div class=\"outerDiv\">"
    h1 = "<h1>About Me</h2>"
    innerDivRight = "<div class=\"innerDivRight\">"
    imageSource = imageSource
    imageAlt = imageAlt
    imageTag = f"<img class=\"center\" src=\"{imageSource}\" alt=\"{imageAlt}\">"
    paragraph = f"<p>{paragraph}</p>"
    h2 = "<h2>Things I like to do for Fun</h2>"
    innerDivLeft = "<div class=\"innerDivLeft\">"
    htmlBody = [outerDiv, h1, innerDivRight, imageTag, paragraph, "</div>", innerDivLeft, h2]
    for tag in htmlBody:
        file = open("index.html", "a")
        if(tag == outerDiv):
            file.write("\n\t\t")
        elif(tag == h1 or tag == innerDivRight or tag == innerDivLeft):
            file.write("\n\t\t\t")
        elif(tag == h2 or tag == imageTag or tag == paragraph):
            file.write("\n\t\t\t\t")
        elif(tag == "</div>"):
            file.write("\n\t\t\t")
        file.write(tag)
        file.close()
        
def addFunThing(number, fun):
    for number in range(number):
        thing = input(f"Enter a fun thing to do {number+1}: ")
        fun.append(thing)
        
def printHtmlOlList(task):
    file = open("index.html", "a")
    file.write("\n\t\t\t\t")
    file.write("<ol>")
    file.write("\n")
    for task in task:
        file.write("\t\t\t\t\t")
        file.write(f"<li>{task}</li>\n")
    file.write("\t\t\t\t</ol>\n")
    file.write("\t\t\t</div>")
        

def printHtmlFooterAndClosingTags(footer):
    htmlFooter = ["<footer>", footer, "</footer>", "</div>", "</body>","</html>"]
    for tag in htmlFooter:
        file = open("index.html", "a")
        if(tag == "<footer>"):
            file.write("\n\t\t\t")
        elif(tag == "</div>"):
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
