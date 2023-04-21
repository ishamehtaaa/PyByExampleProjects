# bulletpointadder.py

import pyperclip
text = pyperclip.paste()


lines = text.split(text)
for i in range(len(lines)):
    lines[i] = "* " + lines[i]
text = "\n".join(lines)

pyperclip.copy(text)