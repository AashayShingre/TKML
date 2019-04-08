from tkinterxml import TKML
from sys import argv

tkmlfile = argv[1]

a = TKML(tkmlfile)
builtWindow = a.getBuiltWindow()

button_tags = a.getTag('Button') ##returns a list of all tkinter button instances
name_class = a.getClass('name') ##returns a list of all tkinter instances with class = name
equal_button = a.getID('id') ##return a list of all tkinter instance with id = id

builtWindow.mainloop()