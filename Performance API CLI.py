#! /usr/bin/env python3
import requests
import json
import os
import time
import string
import calendar
import datetime
import base64
import pathlib
import re
import smtplib
import signal
from pathlib import Path
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from Data.persistent.emailsCC import CCmails, mainEmailFrom, toMail
import csv

""" SUMMARY:

- ⚙️ Fundamental setup (Path, API URLs and others)
- 📜 Load resources
- 🔐 Security execution
- ✍️ Misc variables
- 🔖 Email function
- 🦾 CSV generator, checks and cleaning
- 🎯 API functions
- 🏞 User Interface start
"""

# ⚙️ Fundamental setup (Path, API URLs and others)
os.system("clear")

# API DOCUMENTATION LINK: https://developers.hubspot.com/docs/api/cms/performance
urlPerformance = "https://api.hubapi.com/cms/v3/performance/"
urlUptime = "https://api.hubapi.com/cms/v3/performance/uptime"

# Disable in production
debugMode = False
enableLogs = True

shiftAlpha = 4

# Dynamic File Path Solution
API_PATH = pathlib.Path(__file__).parent.absolute()


def relative_to_assets(path: str) -> Path:
    return API_PATH / Path(path)


def getTime():
    # Get  current time and store inside a variable. [used for LOGS]
    currentTime = datetime.datetime.now()
    return currentTime


def signal_handler(sig, frame):
    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStepEx = f"{getTime()} - WARNING: User interrupted the execution manually. Removing temporary files."
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

        # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStepEx}\n")
        # ===== 🚨 LOGS STEP =====

    # If the program exits then remove important files.
    # Delete Data/security/.tmp/.API file
    os.remove(relative_to_assets("Data/security/.tmp/.API"))
    os.remove(relative_to_assets("Data/security/.tmp/.epasswd"))
    exit()


# 📜 Load resources


# Load URLs.json and store in a variable
with open(relative_to_assets("Data/persistent/URLs.json"), "r") as f:
    jsonURLs = json.load(f)
    # print(jsonURLs)

# Load mainDomain.json and store in a variable
with open(relative_to_assets("Data/persistent/mainDomain.json"), "r") as f:
    jsonMainDomain = json.load(f)
    targetDomain = jsonMainDomain.get("domain")


# Nick's Security checks and loads


def decryptSecurity():
    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStepEx = (
            f"{getTime()} - SECURITY: Decrypting API key for internal usage in memory."
        )
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

        # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStepEx}\n")
        # ===== 🚨 LOGS STEP =====

    key = "MjI0"  # up 255
    key = base64.b64decode(key)
    cleanKey = re.sub(r"[^A-Za-z0-9-]", "", key.decode("utf-8"))
    finalKey = int(cleanKey)

    loadEnc00 = open(relative_to_assets("Data/security/.API.nclmE"), "rb").read()

    byteReader = bytearray(loadEnc00)
    for index, value in enumerate(byteReader):
        byteReader[index] = value ^ finalKey

    decEnc = open(relative_to_assets("Data/security/.tmp/.API"), "wb")
    decEnc.write(byteReader)


def decryptMailSecurity():
    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStepEx = f"{getTime()} - SECURITY: Decrypting Email credentials for internal usage in memory."
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

        # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStepEx}\n")
        # ===== 🚨 LOGS STEP =====

    key = "MTkw"  # up to 255
    key = base64.b64decode(key)
    cleanKey = re.sub(r"[^A-Za-z0-9-]", "", key.decode("utf-8"))
    finalKey = int(cleanKey)

    loadEnc00 = open(relative_to_assets("Data/security/.epasswd.nclmE"), "rb").read()

    byteReader = bytearray(loadEnc00)
    for index, value in enumerate(byteReader):
        byteReader[index] = value ^ finalKey

    decEnc = open(relative_to_assets("Data/security/.tmp/.epasswd"), "wb")
    decEnc.write(byteReader)


# 🔐 Security execution


def API_SEC():
    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStepEx = f"{getTime()} - SECURITY: Main security function started... Running checks and crypto jobs."
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

        # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStepEx}\n")
        # ===== 🚨 LOGS STEP =====

    decryptSecurity()
    decryptMailSecurity()

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
    API_CONTENT = open(relative_to_assets("Data/security/.tmp/.API"), "r").read()
    API_DECODED = base64.b64decode(API_CONTENT.encode("utf-8"))

    # Regular expression to remove garbage characters, do not remove "-"
    API_DECODED_CLEAN = re.sub(r"[^A-Za-z0-9-]", "", API_DECODED.decode("utf-8"))

    UNLOCKED_CONTENT = str(API_DECODED_CLEAN).translate(tableContentUn)

    os.remove(relative_to_assets("Data/security/.tmp/.API"))
    return UNLOCKED_CONTENT


def EMAIL_SEC():
    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStepEx = f"{getTime()} - SECURITY: Email decryption was called... Running crypto jobs to provide email credentials."
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

        # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStepEx}\n")
        # ===== 🚨 LOGS STEP =====

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

    # Email passwd security measures
    EMAIL_CONTENT = open(relative_to_assets("Data/security/.tmp/.epasswd"), "r").read()
    EMAIL_DECODED = base64.b64decode(EMAIL_CONTENT.encode("utf-8"))

    EMAIL_FINAL_DECODE = EMAIL_DECODED.decode("utf-8")

    UNLOCKED_CONTENT = str(EMAIL_FINAL_DECODE).translate(tableContentUn)

    os.remove(relative_to_assets("Data/security/.tmp/.epasswd"))

    return UNLOCKED_CONTENT


# ✍️ Misc variables
allPaths = []
usingPath = None
executeNow = False
# constantlyCheck = True

# UNIX TIMESTAMP RESOLVER
# unixCurrentTimestamp = calendar.timegm(time.gmtime())
unixCurrentTimestamp = datetime.datetime.now().timestamp()
# Remove "." from unixCurrentTimestamp
unixCurrentTimestamp = str(unixCurrentTimestamp).replace(".", "")
# Convert unixCurrentTimestamp to int
unixCurrentTimestamp = int(unixCurrentTimestamp)
unixFuture = unixCurrentTimestamp + 600000

# This querystring is temporary
querystring = {
    "domain": f"{targetDomain}",
    "path": f"{usingPath}",
    "period": "4h",
    "interval": "10m",
    "hapikey": f"{API_SEC()}",
}

headers = {"accept": "application/json"}

clientName = "CLIENT NAME"
ver = "v1.9.4"
dev = "Nick"

emailFrom = mainEmailFrom(224)
emailBCC = CCmails

for url in jsonURLs["results"]:
    # Append url to usingPath
    allPaths.append(url)

if debugMode == True:
    print(f"\n\nDEBUG: {allPaths}\n\n")


# 🔖 Email function
def sendEmail(subject: str, message: str):
    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStepEx = f"{getTime()} - Email send function started."
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

            # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStepEx}\n")
        # ===== 🚨 LOGS STEP =====

    # Email settings
    emailSubject = f"HubSpot Performance API Report - {subject}"
    rcpt = emailBCC.split(",") + [toMail]
    msg = MIMEMultipart()
    msg["From"] = emailFrom
    msg["To"] = toMail
    msg["Cc"] = emailBCC
    msg["Subject"] = emailSubject
    body_part = MIMEText(f"{message}", "plain")
    msg.attach(body_part)

    for content in msg:
        content.encode("utf-8")

    with open(relative_to_assets("Data/release/resultsOutput.csv"), "rb") as file:
        # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name="resultsOutput.csv"))

    try:
        emailServer = smtplib.SMTP("smtp.gmail.com", 587)
        emailServer.ehlo()
        emailServer.starttls()
        emailServer.login(emailFrom, EMAIL_SEC())
        emailServer.sendmail(msg["From"], rcpt, msg.as_string())
        emailServer.quit()
        print("Success: Email sent!")
    except FileNotFoundError:
        if enableLogs == True:
            # ===== 🚨 LOGS STEP =====
            logStepEx = f"{getTime()} - EMAIL SEND ERROR. Please check 'sendEmail()' function - Probably a file is missing, or incorrect encoding or credential error with email server."
            # Check if Data/logs/log.txt exists, if not create it.
            if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
                open(relative_to_assets("Data/logs/log.txt"), "w+")

                # Append logStep to log.txt
            with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
                logFile.write(f"{logStepEx}\n")
            # ===== 🚨 LOGS STEP =====

        print("Email failed to send.")


# 🦾 CSV generator, checks and cleaning


def csvEngine():

    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStep = f"{getTime()} - CSV ENGINE fetching data."
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

        # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStep}\n")
        # ===== 🚨 LOGS STEP =====

    print("Generating CSV...")
    try:
        # Load the file resultsOutput.json
        with open(relative_to_assets("Data/export/resultsOutput.json")) as jsonFile:
            jsonResults = json.load(jsonFile)

            with open(
                relative_to_assets("Data/release/resultsOutput.csv"), "w"
            ) as csvFile:

                writer = csv.writer(csvFile)
                writer.writerow(
                    ["Path", "404 Status", "Period", "Interval", "Domain"]
                )  # Header

                pathNum = 0

                for _ in jsonResults["Path"]:
                    pathNum += 1  # 100

                for i in range(len(jsonResults["Path"])):
                    writer.writerow(
                        [
                            jsonResults["Path"][i],
                            jsonResults["Data"][i][0]["404"],
                            "4 Hours",
                            "10 Minutes",
                            targetDomain,
                        ]
                    )

        csvCheck()

    except FileNotFoundError:
        if enableLogs == True:
            # ===== 🚨 LOGS STEP =====
            logStepEx = f"{getTime()} - CSV ENGINE ERROR. File not found - Probably the JSON file was not found."
            # Check if Data/logs/log.txt exists, if not create it.
            if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
                open(relative_to_assets("Data/logs/log.txt"), "w+")

            # Append logStep to log.txt
            with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
                logFile.write(f"{logStepEx}\n")
            # ===== 🚨 LOGS STEP =====

        print("ERROR! JSON not found.")


def csvCheck():
    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStepEx = f"{getTime()} - CSV Checks started. Searching for 404s and if detected an email will be sent."
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

        # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStepEx}\n")
        # ===== 🚨 LOGS STEP =====

    print("Checking if there is pages with 404.")
    print("If there is a 404, the script will send an email.")
    time.sleep(15)

    with open(relative_to_assets("Data/export/resultsOutput.json")) as jsonFile:
        jsonResults = json.load(jsonFile)
        issueFound = False

        # if jsonResults 'Data' key contains a 404 key greater than 0, then issueFound = True
        pagesError = 0
        for i in range(len(jsonResults["Data"])):
            if jsonResults["Data"][i][0]["404"] > 0:
                print("404 found! Sending email.")
                pagesError += 1
            else:
                print("No 404s found.")

    if pagesError > 0:
        if enableLogs == True:
            # ===== 🚨 LOGS STEP =====
            logStepEx = f"{getTime()} - WARNING: 404s found. Triggering email."
            # Check if Data/logs/log.txt exists, if not create it.
            if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
                open(relative_to_assets("Data/logs/log.txt"), "w+")

                # Append logStep to log.txt
            with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
                logFile.write(f"{logStepEx}\n")
            # ===== 🚨 LOGS STEP =====

        sendEmail(
            "HubSpot Performance API",
            f"Hi,\n\nThere are some pages that need attention, 404 status has been found in a period of 4 hours and interval of 10 minutes in domain '{targetDomain}'.\n\nBest regards,\n{clientName} Performance API",
        )


# 🎯 API functions


def funcPerformance(performanceAPI: str):
    global querystring

    if enableLogs == True:
        # ===== 🚨 LOGS STEP =====
        logStep = f"{getTime()} - Performance API is running once again..."
        # Check if Data/logs/log.txt exists, if not create it.
        if not os.path.exists(relative_to_assets("Data/logs/log.txt")):
            open(relative_to_assets("Data/logs/log.txt"), "w+")

        # Append logStep to log.txt
        with open(relative_to_assets("Data/logs/log.txt"), "a") as logFile:
            logFile.write(f"{logStep}\n")
        # ===== 🚨 LOGS STEP =====

    response = requests.request(
        "GET", performanceAPI, headers=headers, params=querystring
    )
    finalOutputPer = response.json()

    if debugMode == True:
        print(f"{dev}'s DEBUG: {finalOutputPer}")

    if finalOutputPer.get("status") is not None:
        # Error handling
        if finalOutputPer["status"] == "error":
            os.remove(relative_to_assets("Data/security/.tmp/.API"))
            os.remove(relative_to_assets("Data/security/.tmp/.epasswd"))
            print(f"ERROR!\n{finalOutputPer['message']}\n")
    else:
        resultPathStorage = {"Path": []}
        resultDataStorage = {"Data": []}
        print("Getting information of all URLs inside the domain...")
        for path in allPaths:
            usingPath = path
            querystring = {
                "domain": f"{targetDomain}",
                "path": f"{usingPath}",
                "start": f"{unixCurrentTimestamp}",
                "end": f"{unixFuture}",
                "period": "4h",
                "interval": "10m",
                "hapikey": f"{API_SEC()}",
            }
            response = requests.request(
                "GET", performanceAPI, headers=headers, params=querystring
            )
            finalOutputPer = response.json()

            resultPathStorage[path] = finalOutputPer.get("path")
            resultDataStorage[path] = finalOutputPer.get("data")
        # Store both resultPathStorage and resultDataStorage in a JSON file called "resultsOutput"
        with open(relative_to_assets("Data/export/resultsOutput.json"), "w") as f:
            # Clear f
            f.seek(0)
            f.truncate()
            # Append each url value to the resultPathStorage dictionary as values of the 'Path' key.
            for path in allPaths:
                resultPathStorage["Path"].append(resultPathStorage[path])

            # Append each data value to the resultDataStorage dictionary as values of the 'Data' key.
            for data in allPaths:
                resultDataStorage["Data"].append(resultDataStorage[data])

            # Combine resultPathStorage and resultDataStorage. Export as json.
            json.dump(
                {"Path": resultPathStorage["Path"], "Data": resultDataStorage["Data"]},
                f,
            )
        print("Information stored in JSON file.")
        # time.sleep(15)
        csvEngine()


# Used but not directly


def funcUptime(uptimeAPI: str):
    responseUp = requests.request("GET", uptimeAPI, headers=headers, params=querystring)
    finalOutputUp = responseUp.json()

    if debugMode == True:
        print(f"{dev}'s DEBUG: {finalOutputUp}")

    if finalOutputUp.get("status") is not None:
        # Error handling
        if finalOutputUp["status"] == "error":
            print(f"ERROR!\n{finalOutputUp['message']}\n")

    else:
        pass


def mainController():
    global executeNow

    print(
        "The script will continue running. After 10 minutes it will start checking again."
    )
    print(
        f"Scanning {targetDomain} to get performance information...(Please wait. This can take a while)\n"
    )
    # Check if Data folder exists, if not break.
    if not os.path.exists(relative_to_assets("Data/export")):
        print("ERROR! Data folder not found.")
        exit()

    # Check if ./Data/security/.tmp folder exists, if not create it.
    if not os.path.exists(relative_to_assets("Data/security/.tmp")):
        os.makedirs(relative_to_assets("Data/security/.tmp"))

    # Check if ./Data/export folder exists, if not create it.
    if not os.path.exists(relative_to_assets("Data/export")):
        os.makedirs(relative_to_assets("Data/export"))

    # Check if ./Data/release folder exists, if not create it.
    if not os.path.exists(relative_to_assets("Data/release")):
        os.makedirs(relative_to_assets("Data/release"))

    # Check if ./Data/export/persistent exists, if not create it.
    if not os.path.exists(relative_to_assets("Data/export/persistent")):
        os.makedirs(relative_to_assets("Data/export/persistent"))

    funcPerformance(urlPerformance)
    constantlyCheck = True

    while constantlyCheck == True:
        # Wait 10 minutes (600) and toggle executeNow.
        time.sleep(600)
        print("Checking again...")
        executeNow = True

        while executeNow == True:
            funcPerformance(urlPerformance)
            executeNow = False
        while executeNow == False:
            time.sleep(600)
            executeNow = True


# 🏞 User Interface start
print(f"Welcome to {clientName} Performance CLI {ver}\n")

# signal handler for "CTRL + C"
signal.signal(signal.SIGINT, signal_handler)

if debugMode is True:
    API_SEC()

mainController()

signal.pause()
