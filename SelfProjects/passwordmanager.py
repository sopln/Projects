#! python3
"""The code below is used to copy your password on to the clipboard. You might have different passwords for different
accounts and its very noraml for people to forget these .  This code serves as a password manager for all your accounts. 
"""
PASSWORDS = {'email': 'Type your email password over here',
             'blog': 'Type your blog password over here',
             'facebook': 'Type your facebook password over here',
             'Add More':'Add more passwords'}
import sys, pyperclip
if len(sys.argv)<2:
    print('Supply a command line argument whose password you want to be copied')
    sys.exit()
account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)