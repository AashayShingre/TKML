from tkinterxml import TKML
from sys import argv

tkmlfile = argv[1]

a = TKML(tkmlfile)
builtWindow = a.getBuiltWindow()

print(a.getTag("Button"))
print(*a.getClass())
print(*a.getID())

builtWindow.mainloop()