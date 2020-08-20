import pyperclip, re

strongPassword = re.compile(r'^(?=.*\d)(?=.*[A-Z])\w{8,15}$')

password = str(pyperclip.paste())
matches = []

for groups in strongPassword.findall(password):
    if len(matches) < 8:
        print('Password need to be at least 8 characters')
    else:
        print('Well done')