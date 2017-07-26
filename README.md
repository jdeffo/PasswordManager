# Password Manager

A password manager to store encrypted, private passwords for my various accounts.  Accepts the account and an encrypted master password (a randomly generated key in the future) and copies the correlated password to the clipboard.

## Getting Started

Download the project to your local machine, set the accounts you desire to manage as well as generate passwords for them.  Then, set your master password.  See config examples for more detials.

### Prerequisites

* Python 3.6 - [Download Python](http://www.python.org)
  * sys, pyperclip

```
import sys, pyperclip
```

## Built With

* Python
  * sys, pyperclip


## Versioning

* V1 - Stores accounts and passwords in memory.  Copies the desired password (fake passwords for now) to the clipboard.
* V2 (Current) - Stores the (fake) passwords on the Mac, and loads them into a dictionary
## Authors

* **Jeremy DeFossett** - (http://www.jdeffo.com)

## Acknowledgments
* [Automate The Boring Stuff](https://automatetheboringstuff.com) - Inspiration, Chapter 6

