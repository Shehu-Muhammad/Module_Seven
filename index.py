def my_function():
    thisTuple = ["Hello", "World", "Apples"]
    for x in thisTuple:
        print(x)

# my_function()

def writeNameToPage():
    username = input("Enter a username: ")
    file = open("test.txt", 'a')
    file.write(f"My Name is {username}")
    file.close()
writeNameToPage()

def clearNameFromPage():
    file = open("test.txt", 'w')
    file.close()

# clearNameFromPage()

def readNameFromPage():
    file = open("test.txt", "r")
    print(file.read())

readNameFromPage()



# print(username)


