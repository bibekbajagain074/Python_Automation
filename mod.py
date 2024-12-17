
import os

import shutil

files =os.listdir()


if not os.path.exists("pythonCodes"):
    os.mkdir("PythonCodes")
    print("Created newFolder")

for file in files:
    if ".py" in files:
        print("pyton file dectected "+ file +"is python file")

