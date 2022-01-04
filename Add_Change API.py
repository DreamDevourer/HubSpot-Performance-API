#! /usr/bin/env python3
import base64
import os
import pathlib
import string
import re
import string
import random
from pathlib import Path

# Nick's security protocol
os.system("clear")

# Disable in production
debugMode = False

# Dynamic File Path Solution
API_PATH = pathlib.Path(__file__).parent.absolute()


def relative_to_assets(path: str) -> Path:
    return API_PATH / Path(path)


def encryptSecurity():
    key = "MjI0"  # up 255
    key = base64.b64decode(key)
    cleanKey = re.sub(
        r"[^A-Za-z0-9-]", "", key.decode("utf-8"))
    finalKey = int(cleanKey)

    loadEnc00 = open(relative_to_assets("Data/security/.tmp/.API"), "rb")
    byteReaderData = loadEnc00.read()
    loadEnc00.close()

    byteReaderData = bytearray(byteReaderData)
    for index, value in enumerate(byteReaderData):
        byteReaderData[index] = value ^ finalKey

    Enc = open(relative_to_assets("Data/security/.API.nclmE"), "wb")
    Enc.write(byteReaderData)
    Enc.close()

    # Delete Data/security/API
    os.remove(relative_to_assets("Data/security/.tmp/.API"))


print("\nChange your API here if needed.\nNEVER CHANGE THE API KEY DIRECTLY\nFOR SECURITY REASONS!\n")
userChange = input("Enter new API key: ").strip()

# Check if ./Data/security/.tmp folder exists, if not create it.
if not os.path.exists(relative_to_assets("Data/security")):
    os.makedirs(relative_to_assets("Data/security"))

if not os.path.exists(relative_to_assets("Data/security/.tmp")):
    os.makedirs(relative_to_assets("Data/security/.tmp"))

# Caesar Cipher
alphaCharset = string.ascii_letters
numCharset = string.digits
# Combine both alphaCharset with numCharset in one variable
charsetMain = alphaCharset + numCharset

totalNum = 0
for i in range(len(charsetMain)):
    totalNum += i

# print(totalNum)
shiftAlpha = 4
shiftAlpha %= totalNum

alphaShifted = None
alphaShifted = charsetMain[shiftAlpha:] + charsetMain[:shiftAlpha]
tableContent = str.maketrans(charsetMain, alphaShifted)

CIPHER_APPLIED = userChange.translate(tableContent)

# Pick userChange and encode it to base64
userChange = base64.b64encode(CIPHER_APPLIED.encode('utf-8'))
# Save userChange to "API" file
with open(relative_to_assets('Data/security/.tmp/.API'), 'wb') as f:
    # Delete everything inside the file.
    f.truncate()
    f.write(userChange)

    os.system("clear")
    f.close()

encryptSecurity()
print("DONE! You are ready to use the API!")
