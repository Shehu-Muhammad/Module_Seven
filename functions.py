# a function to print the opening of an html file, the head section with a title, and link to css file
def printHtmlOpeningAndHeadSection(title):
    css = "<link rel=\"stylesheet\" href=\"index.css\">"
    language = "<html lang=\"en\">"
    meta1 = "<meta charset=\"UTF-8\">"
    meta2 =	"<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
    meta3 = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    htmlOpening = ["<!DOCTYPE html>", language, "<head>", meta1, meta2, meta3, "<title>", title, "</title>", css, "</head>", "<body>"]
    for tag in htmlOpening:
        file = open("index.html", 'a')
        if(tag == "<head>" or tag == "</head>" or tag == "<body>"):
            file.write("\n\t")
        elif(tag == language):
            file.write("\n")
        elif(tag == meta1 or tag == meta2 or tag == meta3 or tag == "<title>" or tag == css):
            file.write("\n\t\t")
        file.write(tag)
        file.close()

# a function to print the content of the body section
def printHtmlBodyContent(name, imageSource, imageAlt, paragraph):
    name = name
    outerDiv = "<div class=\"outerDiv\">"
    h1 = f"<h1>About {name}</h1>"
    innerDivRight = "<div class=\"innerDivRight\">"
    imageSource = imageSource
    imageAlt = imageAlt
    imageTag = f"<img class=\"center\" src=\"{imageSource}\" alt=\"{imageAlt}\">"
    paragraph = f"<p>{paragraph}</p>"
    h2 = f"<h2>Things {name} likes to do for Fun</h2>"
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

# a function to add fun things to a list
def addFunThing(number, fun):
    for number in range(number):
        thing = input(f"Enter a fun thing to do {number+1}: ")
        fun.append(thing)

# a function to print the ordered list to the html
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
    file.close()
        
# a function to print the footer and closing tags of the html
def printHtmlFooterAndClosingTags():
    footer = "&copy; All Rights Reserved."
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

# a function to clear the HTML file
def clearHtmlFile():
    file = open("index.html", 'w')
    file.close()

# a function to read the HTML file
def readHTMLFile():
    file = open("index.html", "r")
    print(file.read())
    file.close()

# a function to ask for information from the user
def askForQuestions():
    name = input("Enter your name: ")
    title = input("Enter a title: ")
    imageSource = input("Enter an image source: ")
    imageAlt = input("Enter a description of the image: ")
    paragraph = input("Enter a paragraph about yourself: ")
    number_input = input("Enter number for fun: ")

    return name, title, imageSource, imageAlt, paragraph, number_input

# a function to run all the functions
def main():
    fun = []
    goodNumber = False

    try:
        name, title, imageSource, imageAlt, paragraph, number_input = askForQuestions()
        number = int(number_input)
    except ValueError as valueErrorExceptionThrown:
        print("Specific value details: ", valueErrorExceptionThrown)

        while not goodNumber:
            try:
                number_input = input("Enter number for fun: ")
                number = int(number_input)
            except:
                print("Specific value details: ", valueErrorExceptionThrown)
            else:
                goodNumber = True
                continue

    finally:
        clearHtmlFile()
        printHtmlOpeningAndHeadSection(title)
        printHtmlBodyContent(name, imageSource, imageAlt, paragraph)
        addFunThing(number, fun)
        printHtmlOlList(fun)
        printHtmlFooterAndClosingTags()
        readHTMLFile()
