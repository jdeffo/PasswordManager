#! /usr/bin/env python3

import sys, pyperclip

PASSWORDS = { }

def passwords_read():
    global PASSWORDS
    with open("passwords.txt") as f:
        for line in f:
            (key, value) = line.split()
            PASSWORDS[key] = value
    f.close()

if len(sys.argv) < 2:
    print("Usage: Python V1.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

passwords_read()

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('Password for ' + account + ' does not exist')
