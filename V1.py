#! /usr/bin/env python3

import sys, pyperclip

PASSWORDS = {
    'facebook': 'facebookPassword',
    'twitter': 'twitterPassword',
    'instagram': 'instagramPassword',
    'linkedIN': 'linkedINPassword',
    'gmail': 'gmailPassword',
    'github': 'githubPassword',
    'dropbox': 'dropboxPassword',
    'droplet': 'dropletPassword'
}

if len(sys.argv) < 2:
    print("Usage: Python V1.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('Password for ' + account + ' does not exist')
