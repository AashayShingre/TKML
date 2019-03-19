from sys import argv
import tkinter as tk
import xml.etree.ElementTree as ET
import os
from PIL import Image, ImageTk

class TKML:
    def __init__(self, TKMLfile = ""): #for now we just take
        # if filename != '':
        #     self.TKMLTree = ETree.parse(filename)
        self.build = ""
        if TKMLfile != "":
            ETree = ET.parse(TKMLfile)
            root = ETree.getroot()
            self.build = self.buildComponents(root, self.build)

    def buildComponents(self, element, parent):
        if element.tag == "Window":
            self.build = tk.Tk(screenName="Test1", baseName="test-1", className=element.attrib['formName'])
            parent = self.build
        elif element.tag == "Label":
            #we are not assuming any child for it anyways
            ph = None
            cmp = None
            fg = None
            bg = None
            font = None
            if 'imageSrc' in element.attrib:
                im = Image.open(element.attrib['imageSrc'])
                imWidth, imHeight = im.size
                if 'imageWidth' in element.attrib : imWidth = int(element.attrib['imageWidth'])
                if 'imageHeight' in element.attrib : imHeight = int(element.attrib['imageHeight'])
                im = im.resize((imWidth, imHeight), Image.ANTIALIAS)
                ph = ImageTk.PhotoImage(im)
                if 'imageSide' in element.attrib:
                    if element.attrib['imageSide'] == "center": 
                        cmp = tk.CENTER
            if 'fg' in element.attrib: fg = element.attrib["fg"]
            if 'bg' in element.attrib: bg = element.attrib["bg"]
            if 'font' in element.attrib: font = element.attrib["font"]
            label  = tk.Label(parent, compound = cmp, text = element.text, fg=fg, bg=bg, font=font, image = ph)
            label.image = ph
            label.pack()
            parent = label
        elif element.tag == "Image":
            # logo = tk.PhotoImage(file=attrib['src'])
            pass
        elif element.tag == "Button":
            width = int(element.attrib['width']) if ('width' in element.attrib) else None
            button = tk.Button(parent, text=element.text, width=width)
            button.pack()
            parent = button
        elif element.tag == "RadioButton":
            radio_button = tk.Radiobutton(parent , text=element.attrib['label'], variable=element.attrib['name'], value=element.attrib['value'])
            if ('position' in element.attrib):
                if element.attrib['position'] == 'absolute':
                    radio_button.place(x=element.attrib['x'], y = element.attrib['y'])
                elif element.attrib['position'] == 'grid':
                    radio_button.grid(row = int(element.attrib["row"]), column = int(element.attrib["column"]))
                elif element.attrib['postion'] == 'static':
                    radio_button.pack()
            else:
                radio_button.pack()
            parent = radio_button
        elif element.tag == "CheckBox":
            checkBox = tk.Checkbutton(parent, text=element.attrib['label'], variable=element.attrib['name'])
            checkBox.pack()
            parent = checkBox
        elif element.tag == "Canvas":
            canvas = tk.Canvas(parent, width=element.attrib['width'], height=element.attrib['height'], bg=(element.attrib['bg'] if ('bg' in element.attrib) else None), border=element.attrib['border'])
            canvas.pack()
            parent = canvas
        elif element.tag == "Line":
            points = eval(element.attrib['endpt'])
            parent.create_line(*points, fill=element.attrib['fill'])  
        elif element.tag == "Rect":
            points = eval(element.attrib['fixpt'])
            parent.create_rectangle(*points, int(element.attrib['height']), int(element.attrib['width']), fill=element.attrib['fill'])
        elif element.tag == "Text":
            points = eval(element.attrib['xy'])
            parent.create_text(*points, text = element.text)


        for childElement in element:
            self.buildComponents(childElement, parent)
        if (element.tag == "Window"):
            return self.build

    def getBuiltWindow(self):
        return self.build
    

# if __name__ == "__main__":
    # filename_ = argv[1]
    # if isValidXML(filename_):
    #     ETree = ET.parse(filename_)
    #     root = ETree.getroot()
    #     mainWindow = tkinter.Tk()
    #     traverse_tree_and_render(root)
    #     mainWindow.mainloop()
tkmlfile = argv[1]
builtWindow = TKML(tkmlfile).getBuiltWindow()
builtWindow.mainloop()