#! /usr/bin/env python3
import hubspot
from pprint import pprint
from hubspot.cms.domains import ApiException
import os
import pathlib
from pathlib import Path
import base64
import re
import json
import requests
import string

# DOMAIN DOC: https://developers.hubspot.com/docs/api/cms/domains
os.system("clear")

# Dynamic File Path Solution
API_PATH = pathlib.Path(__file__).parent.absolute()


def relative_to_assets(path: str) -> Path:
    return API_PATH / Path(path)


shiftAlpha = 4

# Check if ./Data/security/.tmp folder exists, if not create it.
if not os.path.exists(relative_to_assets("Data/security")):
    os.makedirs(relative_to_assets("Data/security"))

if not os.path.exists(relative_to_assets("Data/security/.tmp")):
    os.makedirs(relative_to_assets("Data/security/.tmp"))

# Nick's Security checks


def decryptSecurity():
    key = "MjI0"  # up 255
    key = base64.b64decode(key)
    cleanKey = re.sub(
        r"[^A-Za-z0-9-]", "", key.decode("utf-8"))
    finalKey = int(cleanKey)

    loadEnc00 = open(relative_to_assets(
        "Data/security/.API.nclmE"), "rb").read()

    byteReader = bytearray(loadEnc00)
    for index, value in enumerate(byteReader):
        byteReader[index] = value ^ finalKey

    decEnc = open(relative_to_assets("Data/security/.tmp/.API"), "wb")
    decEnc.write(byteReader)


def API_SEC():
    decryptSecurity()

    global shiftAlpha

    # Caesar Cipher
    alphaCharset = string.ascii_letters
    numCharset = string.digits
    charsetMain = alphaCharset + numCharset

    totalNum = 0
    for i in range(len(charsetMain)):
        totalNum += i

    shiftAlpha %= totalNum

    unshiftAlpha = -shiftAlpha

    alphaUnshifted = None
    alphaUnshifted = charsetMain[unshiftAlpha:] + charsetMain[:unshiftAlpha]
    tableContentUn = str.maketrans(charsetMain, alphaUnshifted)

    # Security measures
    API_CONTENT = open(relative_to_assets(
        "Data/security/.tmp/.API"), "r").read()
    API_DECODED = base64.b64decode(API_CONTENT.encode("utf-8"))

    # Regular expression to remove garbage characters, do not remove "-"
    API_DECODED_CLEAN = re.sub(
        r"[^A-Za-z0-9-]", "", API_DECODED.decode("utf-8"))

    UNLOCKED_CONTENT = str(API_DECODED_CLEAN).translate(tableContentUn)

    os.remove(relative_to_assets("Data/security/.tmp/.API"))
    return UNLOCKED_CONTENT


client = hubspot.Client.create(api_key=f"{API_SEC()}")
headers = {'accept': 'application/json'}

api_response = client.cms.domains.domains_api.get_page(
    sort=['domain', 'id'], async_req=False)

pprint(api_response)

# try:
#     api_response = client.cms.domains.domains_api.get_page(
#         sort=['domain', 'id'], async_req=False)

#     pprint(api_response)
#     # Export api_response to a json file called "mainDomain.json".
#     with open(relative_to_assets("mainDomain.json"), "w") as f:
#         json.dump(api_response.__dict__, f)

# except ApiException as e:
#     print("Exception when calling domains_api->get_page: %s\n" % e)
