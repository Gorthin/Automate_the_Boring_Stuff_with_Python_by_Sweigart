import pyperclip, re

dataRegex = re.compile(r"^([0-2][1-9]|3[01])/(0[1-9]|1[0-2])/[12]\d{3}$")

text = str(pyperclip.paste())
matches = []
for groups in dataRegex.findall(text):
    dataNum = '/'.join([groups[1], groups[2], groups[3]])
    matches.append(dataNum)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copy to pyperclip:')
    print('\n'.join(matches))
else:
    print('Don,t matches any date.')