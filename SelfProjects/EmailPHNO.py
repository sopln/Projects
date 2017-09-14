"""The following code counts the number of occurances of a given email id or contact info in a given web page. 
To use this just copy the entire text of the given web page and run this program"""
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

pussy = re.compile(r'pussy')    #code for pussy
# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
ph_no = 0
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    ph_no += 1
email_no = 0
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    email_no += 1
k = 0                               #code for pussy
for groups in pussy.findall(text):  #Code for pussy
    matches.append(groups[:])       #Code for pussy
    k += 1                          #code for pussy 
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:','No of email ids',email_no,'No of contact infos',ph_no,'No of pussy\'s',k)    #k is added over here to count the number of pussy's 
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


