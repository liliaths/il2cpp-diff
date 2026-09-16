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

            with open(os.path.join("output", file), "rb") as f:
                headerBytes = f.read(4)
                print("Header Bytes of libil2cpp.so:", headerBytes)
                if headerBytes == b'\x7fELF':
                    print("libil2cpp.so is a valid ELF file.")
                else:
                    print("libil2cpp.so is not a valid ELF file.")

        if file.endswith("global-metadata.dat"):
            apk.extract(file, path="output")
            size = os.path.getsize(os.path.join("output", file))
            print("Byte Size of global-metadata.dat:", size, "Found global-metadata.dat:", file)
            
            with open(os.path.join("output", file), "rb") as f:
                headerBytes = f.read(4)
                print("Header Bytes of global-metadata.dat:", headerBytes)
                if headerBytes == b'\xaf\x1b\xb1\xfa':
                    print("global-metadata.dat is a valid metadata file.")
                    
                    nextFourBytes = f.read(4)
                    metaDataVersion = int.from_bytes(nextFourBytes, byteorder='little')
                    print("Metadata Version of global-metadata.dat:", metaDataVersion)
                else:
                    print("global-metadata.dat is not a valid metadata file.")

