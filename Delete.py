import os
def Kill():
    print("Name file.") # Name and type.
    what = input()
    if os.path.exists(what):
      os.remove(what)
      print("Removed.")
    else:
      print("The file does not exist")
Kill()
print("Do you want continue?") 
contrr = input()
if contrr == "Yes" or contrr == "Yes." or contrr == "yes" or contrr == "yes." or contrr == "YES." or contrr == "YES":
    print("ok")
    Kill()