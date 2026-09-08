import zipfile
import sys
import os

apk_path = sys.argv[1]

with zipfile.ZipFile(apk_path, "r") as apk:
    files = apk.namelist()

    for file in files:
        if file.endswith("libil2cpp.so"):
            apk.extract(file, path="output")
            size = os.path.getsize(os.path.join("output", file))
            print("Byte Size of libil2cpp.so:", size, "Found libil2cpp.so:", file)

        if file.endswith("global-metadata.dat"):
            apk.extract(file, path="output")
            size = os.path.getsize(os.path.join("output", file))
            print("Byte Size of global-metadata.dat:", size, "Found global-metadata.dat:", file)
            