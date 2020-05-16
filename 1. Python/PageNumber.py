def findMissing():
    l = input("Enter page numbers in the book, seperated by commas\n")
    l = set(l.split(","))
    l = {int(i) for i in l}
    check = set(range(1, 26))
    print("Missing page numbers are:\n")
    print(check - l)

findMissing()


