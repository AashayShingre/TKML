from sys import argv
import tkinter as tk
import xml.etree.ElementTree as ET
import os
from PIL import Image, ImageTk

class TKML:
    def __init__(self, TKMLfile = ""):
        self.build = ""
        self.classes = dict()
        self.ids = dict()
        self.tags = dict()
        if TKMLfile != "":
            ETree = ET.parse(TKMLfile)
            root = ETree.getroot()
            self.build = self.buildComponents(root, self.build, root.attrib.get('layout'))

    def buildComponents(self, element, parent, layout):
        if element.tag == "Window":
            self.build = tk.Tk(screenName="Test1", baseName="test-1", className=element.attrib['formName'])
            parent = self.build
            
            self.tags.setdefault(element.tag,[]).append(parent)
        elif element.tag == "Label":
            #we are not assuming any child for it anyways
            ph = None
            cmp = None
            if 'imageSrc' in element.attrib:
                im = Image.open(element.attrib['imageSrc'])
                imWidth, imHeight = im.size
                if 'imageWidth' in element.attrib : imWidth = int(element.attrib['imageWidth'])
                if 'imageHeight' in element.attrib : imHeight = int(element.attrib['imageHeight'])
                im = im.resize((imWidth, imHeight), Image.ANTIALIAS)
                ph = ImageTk.PhotoImage(im)
                if 'compound' in element.attrib:
                    if element.attrib['compound'] == "center": 
                        cmp = tk.CENTER
            label  = tk.Label(parent, anchor=element.attrib.get('anchor'), cursor=element.attrib.get('cursor'), height=element.attrib.get('height'), width=element.attrib.get('width'), wraplength=element.attrib.get('wrapLength'), justify=element.attrib.get('justify'), padx=element.attrib.get('padX'), pady=element.attrib.get('pady=Y'), relief=element.attrib.get('relief'), compound = cmp, text = element.text, fg=element.attrib.get("fg"), bg=element.attrib.get("bg"), font=element.attrib.get("font"), image = ph, textvariable=element.attrib.get('textVariable'), underline=element.attrib.get('underline'))
            #label = tk.Label(parent, **element.attrib, text=element.text, image=ph)
            label.image = ph
            self.setLayout(label, layout, element.attrib)
            parent = label
            #add to dict
            self.tags.setdefault(element.tag,[]).append(parent)
            if 'id' in element.attrib : self.ids.setdefault(element.attrib['id'], []).append(parent)
            if 'class' in element.attrib : self.ids.setdefault(element.attrib['class'], []).append(parent)
        elif element.tag == "Message":
            message = tk.Message(parent, anchor=element.attrib.get('anchor'), bg=element.attrib.get('bg'), cursor=element.attrib.get('cursor'), font=element.attrib.get('font'), fg=element.attrib.get('fg'), highlightbackground=element.attrib.get('highlightBackground'), highlightcolor = element.attrib.get('highlightcolor'), highlightthickness=element.attrib.get('highlightthickness'), justify=element.attrib.get('justify'), padx=element.attrib.get('padX'), pady=element.attrib.get('padY'), relief=element.attrib.get('relief'), takefocus=element.attrib.get('takeFocus'), text=element.text, textvariable=element.attrib.get('textVariable'), width=element.attrib.get('width'))
            self.setLayout(message, layout, element.attrib)
            parent = message
            #add to dict
            self.tags.setdefault(element.tag,[]).append(parent)
            if 'id' in element.attrib : self.ids.setdefault(element.attrib['id'], []).append(parent)
            if 'class' in element.attrib : self.ids.setdefault(element.attrib['class'], []).append(parent)
        elif element.tag == "Button":
            #button bitmap ? image ? command ?
            button = tk.Button(parent, text=element.text, width=element.attrib.get('width'), activebackground=element.attrib.get('activebackground'), activeforeground=element.attrib.get('activeforeground'), anchor=element.attrib.get('anchor'), bg=element.attrib.get('bg'), borderwidth=element.attrib.get('borderwidth'), compound=element.attrib.get('compound'), cursor=element.attrib.get('cursor'), default=element.attrib.get('default'), disabledforeground=element.attrib.get('disabledforeground'), font=element.attrib.get('font'), fg=element.attrib.get('fg'), padx=element.attrib.get('padx'), pady=element.attrib.get('pady'), relief=element.attrib.get('relief'), state=element.attrib.get('state'))
            self.setLayout(button, layout, element.attrib)
            parent = button
            #add to dict
            self.tags.setdefault(element.tag,[]).append(parent)
            if 'id' in element.attrib : self.ids.setdefault(element.attrib['id'], []).append(parent)
            if 'class' in element.attrib : self.ids.setdefault(element.attrib['class'], []).append(parent)
        elif element.tag == "RadioButton":
            radio_button = tk.Radiobutton(parent , text=element.attrib.get('label'), variable=element.attrib.get('name'), value=element.attrib.get('value'), activebackground=element.attrib.get('activebackground'), anchor=element.attrib.get('anchor'), bg=element.attrib.get('bg'), borderwidth=element.attrib.get('borderwidth'), compound=element.attrib.get('compound'), cursor=element.attrib.get('cursor'), font=element.attrib.get('font'), fg=element.attrib.get('fg'), height=element.attrib.get('height'), justify=element.attrib.get('justify'), padx=element.attrib.get('padx'))
            self.setLayout(radio_button, layout, element.attrib)
            parent = radio_button
            #add to dict
            self.tags.setdefault(element.tag,[]).append(parent)
            if 'id' in element.attrib : self.ids.setdefault(element.attrib['id'], []).append(parent)
            if 'class' in element.attrib : self.ids.setdefault(element.attrib['class'], []).append(parent)
        elif element.tag == "CheckBox":
            checkBox = tk.Checkbutton(parent, text=element.attrib.get('label'), variable=element.attrib.get('name'))
            self.setLayout(checkBox, layout, element.attrib)
            parent = checkBox
            #add to dict
            self.tags.setdefault(element.tag,[]).append(parent)
            if 'id' in element.attrib : self.ids.setdefault(element.attrib['id'], []).append(parent)
            if 'class' in element.attrib : self.ids.setdefault(element.attrib['class'], []).append(parent)
        elif element.tag == "Canvas":
            print("canvas encountered !!!")
            print(*element.attrib)
            print(element.attrib.get('width'))
            canvas = tk.Canvas(parent, width=element.attrib.get('width'), height=element.attrib.get('height'), bg=element.attrib.get('bg'), border=element.attrib.get('border'))
            self.setLayout(canvas, layout, attrib=element.attrib)
            parent = canvas
            #add to dict
            self.tags.setdefault(element.tag,[]).append(parent)
            if 'id' in element.attrib : self.ids.setdefault(element.attrib['id'], []).append(parent)
            if 'class' in element.attrib : self.ids.setdefault(element.attrib['class'], []).append(parent)
        elif element.tag == "Line":
            points = eval(element.attrib['endpt'])
            parent.create_line(*points, fill=element.attrib['fill'])
        elif element.tag == "Rect":
            points = eval(element.attrib['fixpt'])
            parent.create_rectangle(*points, int(element.attrib['height']), int(element.attrib['width']), fill=element.attrib['fill'])
        elif element.tag == "Text":
            if (isinstance(parent, tk.Canvas)):
                points = eval(element.attrib['xy'])
                parent.create_text(*points, text = element.text, fill=element.attrib['fill'])
            else:
                print('text class not made yet')
        elif element.tag == "Frame" :
            frame = tk.Frame(parent, bg=element.attrib.get('bg'))
            self.setLayout(frame, layout, element.attrib)
            parent = frame
            layout = element.attrib.get('layout')
            #add to dict
            self.tags.setdefault(element.tag,[]).append(parent)
            if 'id' in element.attrib : self.ids.setdefault(element.attrib['id'], []).append(parent)
            if 'class' in element.attrib : self.ids.setdefault(element.attrib['class'], []).append(parent)
        elif element.tag == "Menu" :
            if ( not isinstance(parent, tk.Menu)) :
                menu = tk.Menu(parent)
                parent.config(menu=menu)
                parent = menu

                #add to dict
                self.tags.setdefault(element.tag,[]).append(parent)
                if 'id' in element.attrib : self.ids.setdefault(element.attrib['id'], []).append(parent)
                if 'class' in element.attrib : self.ids.setdefault(element.attrib['class'], []).append(parent)
            else:
                menu = tk.Menu(parent)
                parent.add_cascade(label=element.attrib.get("name"), menu=menu)
                parent=menu
        elif element.tag == "MenuOption":
            parent.add_command(label=element.text)
            
        #append to dictionary
        

        for childElement in element:
            self.buildComponents(childElement, parent, element.attrib.get('layout'))
        if (element.tag == "Window"):
            return self.build

    def setLayout(self, element, parentlayout, attrib=dict()):
        if parentlayout == "grid":
            #print(tk.Widget._nametowidget(a))
            tk.Grid.rowconfigure( element.master, index=attrib.get('row'), weight=1 )
            tk.Grid.columnconfigure( element.master, index=attrib.get('column'), weight=1 )
            element.grid(row=attrib.get('row'), column=attrib.get('column'), fill=attrib.get('fill'), ipadx=attrib.get('paddingx'), ipady=attrib.get('paddingy'), padx=attrib.get('marginx'), pady=attrib.get('marginy'), sticky=attrib.get('sticky'), columnspan=attrib.get('columnspan'))
        elif parentlayout == 'place':
            element.place(x=element.attrib.get('x'), y=attrib.get('y'))
        else: #even when the layout will be none
            element.pack(fill=attrib.get('fill'), expand=attrib.get('expand'))

    def getTag(self, name):
        return self.tags

    def getClass(self):
        return self.classes.get('name')
    
    def getID(self):
        return self.ids.get('name')

    def getBuiltWindow(self):
        return self.build
    