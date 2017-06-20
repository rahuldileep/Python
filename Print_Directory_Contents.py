def printDirectory(path,file):
    import os
    for child in os.listdir(path):
        childpath=os.path.join(path,child)
        if os.path.isdir(childpath):
            printDirectory(childpath,file)
        elif child.endswith(file):
            print(child)

path=input("Enter the directory path")
file=input("Enter the extension of files")
printDirectory(path,file)
