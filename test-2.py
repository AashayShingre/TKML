from tkinterxml import TKML
from sys import argv

tkmlfile = argv[1]

a = TKML(tkmlfile)
builtWindow = a.getBuiltWindow()

button_tags = a.getTag('Button') ##returns a list of all tkinter button instances

button_tags[0]['text'] = "Press"

builtWindow.mainloop()