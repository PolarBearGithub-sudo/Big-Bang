import os #Editing your PC.
import time
from xml.dom import InuseAttributeErr #Waiting.
import subprocess
print("Welcome to Big Bang project.")
print("This is automated project for convenient use without the intervention of the interface operation system.")
print("Select mode:")
OSWhat = int(input("1. Shutdown PC. 2. Delete file 3. Cancel shutdown 4. Create file 5. Read file 6. Open file PythonLearning:  "))
if OSWhat == 1:
    os.system("shutdown /s /t 10")
elif OSWhat == 2:
        print("Reading.")
        exec(open("Delete.py").read())
elif OSWhat == 3:
    print("The cancellation protocol is running.")
    os.system("shutdown /a")
    print("Success.")
elif OSWhat == 4:
    print("Ok.")
    WhatIsFileName = input("Write name and type file here: ")
    File = open(WhatIsFileName, "x")
    File.write("Im love python.")
elif OSWhat == 5:
    WhatISFileOpen = input("Write name and type file here: ")
    OpenFile = open(WhatISFileOpen, "r") 
    print(OpenFile.read())
elif OSWhat == 6:
    subprocess.Popen(r'explorer /select,"D:\PythonLearning"')
else:
    print("Invaild.")