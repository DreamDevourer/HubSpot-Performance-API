#! /usr/bin/env python3
"""Emails CC

This module defines emails to CC and Sender
"""

CCmails = "NAME@COMPANY.com,NAME@COMPANY.com"
devMail = "NAME@COMPANY.com"
toMail = "NAME@COMPANY.com"
# Check if there is no intruder inside the main script


def mainEmailFrom(numL: int):
    if numL == 224:
        mainEmailFrom = "API_EMAIL@gmail.com"
    else:
        mainEmailFrom = ""
    return mainEmailFrom
