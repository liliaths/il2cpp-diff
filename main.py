import zipfile
import sys

apk_path = sys.argv[1]

with zipfile.ZipFile(apk_path, "r") as apk:
    files = apk.namelist()

    for file in files:
        if file.endswith("libil2cpp.so"):
            print("Found libil2cpp.so:", file)

        if file.endswith("global-metadata.dat"):
            print("Found global-metadata.dat:", file)
            