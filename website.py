from functions import *

title = "My Website"
css = "<link rel=\"stylesheet\" href=\"index.css\">"
footer = "&copy; All Rights Reserved."
# imageSource = "https://images.pexels.com/photos/2233442/pexels-photo-2233442.jpeg?cs=srgb&dl=pexels-markus-distelrath-2233442.jpg&fm=jpg"
# imageAlt = "A picture of me"
# paragraph = "I am a computer scientist. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet est placerat in egestas erat. Porttitor rhoncus dolor purus non enim praesent elementum facilisis leo. Mi bibendum neque egestas congue quisque egestas diam. Posuere ac ut consequat semper viverra nam libero justo. Non quam lacus suspendisse faucibus interdum posuere lorem. In ornare quam viverra orci sagittis. Pretium fusce id velit ut tortor pretium. Mauris pellentesque pulvinar pellentesque habitant morbi tristique. Diam vel quam elementum pulvinar etiam non quam. Nulla facilisi nullam vehicula ipsum a arcu cursus vitae. I am a computer scientist. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet est placerat in egestas erat. Porttitor rhoncus dolor purus non enim praesent elementum facilisis leo. Mi bibendum neque egestas congue quisque egestas diam. Posuere ac ut consequat semper viverra nam libero justo. Non quam lacus suspendisse faucibus interdum posuere lorem. In ornare quam viverra orci sagittis. Pretium fusce id velit ut tortor pretium. Mauris pellentesque pulvinar pellentesque habitant morbi tristique. Diam vel quam elementum pulvinar etiam non quam. Nulla facilisi nullam vehicula ipsum a arcu cursus vitae. I am a computer scientist. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet est placerat in egestas erat. Porttitor rhoncus dolor purus non enim praesent elementum facilisis leo. Mi bibendum neque egestas congue quisque egestas diam. Posuere ac ut consequat semper viverra nam libero justo. Non quam lacus suspendisse faucibus interdum posuere lorem. In ornare quam viverra orci sagittis. Pretium fusce id velit ut tortor pretium. Mauris pellentesque pulvinar pellentesque habitant morbi tristique. Diam vel quam elementum pulvinar etiam non quam. Nulla facilisi nullam vehicula ipsum a arcu cursus vitae."
# task = ["I like to run", "I like to read", "I like to swim"]

fun = []
title = input("Enter a title: ")
imageSource = input("Enter an image source: ")
imageAlt = input("Enter a description of the image: ")
paragraph = input("Enter a paragraph about yourself: ")
number_input = input("Enter number for fun: ")
number = int(number_input)

clearHtmlFile()
printHtmlOpeningAndHeadSection(title, css)
printHtmlBodyContent(imageSource, imageAlt, paragraph)
addFunThing(number, fun)
printHtmlOlList(fun)
printHtmlFooterAndClosingTags(footer)

    
    
    


