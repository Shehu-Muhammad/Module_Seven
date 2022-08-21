def my_function():
    thisTuple = ["Hello", "World", "Apples"]
    for x in thisTuple:
        print(x)

# my_function()

def writeNameToPage():
    username = input("Enter a username: ")
    file = open("test.txt", 'a')
    file.write(username)
    file.close()
# writeNameToPage()

def readNameFromPage():
    file = open("test.txt", "r")
    print(file.read())

# readNameFromPage()

print("Hello World")



# print(username)


