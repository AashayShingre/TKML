from tkinterxml import TKML
from sys import argv

tkmlfile = argv[1]

a = TKML(tkmlfile)
builtWindow = a.getBuiltWindow()

#calculator logic
state = 'read'

label = a.getTag('Label')[0]

if (a.getTag('Label')[0]['text'] == 100) : print('yess')
print(a.getTag('Button')[0]['text'])

def buttonClick(event, arg):
    global state
    if state == 'read':
        label['text'] = arg
        state = 'write'
    else:
        label['text'] = label['text'] + arg 

def evaluate(event):
    label['text'] = eval(label['text'])
    global state
    state = "read"

def clear(event):
    label['text'] = ""

for element in a.getTag('Button'):
    if element['text'] == '=':
        element.bind('<Button-1>', evaluate)
    else:
        element.bind('<Button-1>', lambda event, arg=element['text']: buttonClick(event, arg))

a.getTag('Menu')[0].bind('<<MenuSelect>>', clear)

builtWindow.mainloop()