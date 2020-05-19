host = r"/etc/hosts"
redirect = "127.0.0.1"
def block():
    inp = input("Enter list of website URLs to block seperated by comma:\n")
    sites = inp.split(',')
    with open(host, "r+") as file:
        content = file.read()
        for site in sites:
            if site in content:
                pass
            else:
                file.write(redirect + " " + site + "\n")

def unblock():
    inp = input("Enter list of website URLs to unblock seperated by comma:\n")
    sites = inp.split(',')
    with open(host, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any (site in line for site in sites):
                file.write(line)
        file.truncate()

opt = int(input("1. Block Sites" + "\n" + "2. Unblock Sites\n"))
if(opt == 1):
    block()
elif(opt == 2):
    unblock()
else:
    print("Invalid Option!")
