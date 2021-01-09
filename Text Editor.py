from tkinter import *
from tkinter import filedialog,font
from tkinter.font import Font
from tkinter.ttk import Combobox

class editor:
    current_open_file="no_file"
    background_color="white"
    foregroung_color="black"
    selected_color="blue"
    highlighted_color="red"
    def __init__(self,root):
        root.title("TEXT EDITOR")

        self.text_area=Text(root, undo=True,wrap=WORD,font=font_for_text)
        self.text_area.pack(fill=BOTH,expand=1)
        #******************CREATING MENU************************************

        self.main_menu=Menu(bg='#2A2C2B')
        root.config(menu=self.main_menu)
        #************* file menu *************************
        self.file_menu=Menu(self.main_menu,tearoff=False,)
        self.main_menu.add_cascade(label="file",menu=self.file_menu)
                    #*****sub menu **********
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open",command=self.Open_File)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save           (ctrl+s)", command=self.Save_File)
        self.file_menu.add_command(label="Save as      (ctrl+a)", command=self.Save_as_File)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)


        #******************* edit menu in file menu************************
        self.edit_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Search", command=self.search)

        #***********Mode***********************************
        self.Mode_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Mode", menu=self.Mode_menu)
        self.Mode_menu.add_command(label="Dark Mode", command=self.Dark_mode)
        self.Mode_menu.add_command(label="Light Mode", command=self.Light_mode)

        #*********************TEXT ******************************
        self.Text_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Format", menu=self.Text_menu)
        self.Text_menu.add_command(label="Font..", command=self.New_Window)


        # ******************** Shortcut keys ******************************
        root.bind("<Control-s>", self.Save_File)  # save
        root.bind("<Control-a>", self.Save_as_File)  # save as




    def Open_File(self):
        result = result=filedialog.askopenfile(initialdir="D:/",title="select file",filetypes=(("text files",".txt"),("python files",".Py")))
        if (result != None):
            self.text_area.delete(1.0, END)
            root.title(f"{result.name} - TEXT EDITOR")
            for text in result:
                self.text_area.insert(END, text)
            self.current_open_file = result.name
            result.close()
    def Save_as_File(self,event=None):
        save_as_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if(save_as_file!=None):
            save_as_file.write(self.text_area.get(1.0, END))
            save_as_file.close()
            self.current_open_file = save_as_file.name
    def Save_File(self,event=None):
        if self.current_open_file=="no_file":
            self.Save_as_File()
        else:
            f=open(self.current_open_file,"w+")
            f.write(self.text_area.get(1.0,END))
            f.close()
    def new_file(self):
        self.text_area.delete(1.0,END)
        root.title("TEXT EDITOR")
        self.current_open_file="no_file"
    def copy_text(self):
        self.text_area.clipboard_clear()
        filess=self.text_area.selection_get()
        self.text_area.clipboard_append(filess)
    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")
    def paste_text(self):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())
    def Dark_mode(self):
        self.text_area.config(bg="#303030",fg="white",selectbackground="#008040")
        self.background_color="#303030"
        self.foregroung_color="white"
        self.selected_color="#008040"
        self.highlighted_color="red"
    def Light_mode(self):
        self.text_area.config(bg="white",fg="black",selectbackground="blue")
        self.background_color = "white"
        self.foregroung_color = "black"
        self.selected_color = "blue"
        self.highlighted_color = "red"
    def New_Window(self):
        top = Toplevel()
        font_sample = Font(family="Times New Roman", size=19, weight="normal")

        # ******************Labels ********************
        label1 = Label(top, text="Font:")
        label1.grid(row=1, column=1, padx=9, pady=9)

        label2 = Label(top, text="Font style:")
        label2.grid(row=1, column=2, padx=9, pady=9)

        label2 = Label(top, text="Size:")
        label2.grid(row=1, column=3)

        # *********************** Combo boxes***********************
        current_family = font_for_text["family"]
        family = list(font.families())

        combo_box = Combobox(top, values=family, height=20, width=20)
        combo_box.set(current_family)
        combo_box.grid(row=2, column=1, padx=9, pady=9)

        current_weight = font_for_text["weight"]
        weight = ["normal", "bold"]
        combo_box1 = Combobox(top, values=weight, height=20, width=20)
        combo_box1.set(current_weight)
        combo_box1.grid(row=2, column=2, padx=9, pady=9)

        size = list(range(1, 90))
        current_size = font_for_text["size"]

        combo_box2 = Combobox(top, values=size, height=20, width=15)
        combo_box2.set(current_size)
        combo_box2.grid(row=2, column=3, padx=9, pady=9)

        # ***************LAbel Frame for example ******************

        fr = LabelFrame(top, text="labelFrame", padx=5, pady=5)
        fr.grid(row=4, column=3, pady=20)
        label3 = Label(fr, text="AbCdEfGh", font=font_sample)
        label3.pack(pady=20, padx=20)
        # in bind lambda function take an argument o asight nun to hold the event argument

        combo_box.bind("<<ComboboxSelected>>", lambda nun: font_sample.config(family=combo_box.get()))
        combo_box1.bind("<<ComboboxSelected>>", lambda nun: font_sample.config(weight=combo_box1.get()))
        combo_box2.bind("<<ComboboxSelected>>", lambda nun: font_sample.config(size=int(combo_box2.get())))
        #*******Last button to execute selected commands *************************
        but = Button(top, text="DONE", command=lambda: [font_for_text.config(
            family=combo_box.get(),weight=combo_box1.get(), size=combo_box2.get()), top.destroy()])
        but.grid(row=5, column=2, padx=2, pady=9)
    def search(self):
        top1=Toplevel()
        top1.geometry("200x200")
        global edit
        edit=Entry(top1)
        edit.grid(row=1,column=1)
        butt=Button(top1,text="Search",command=self.highlight_search)
        butt.grid(row=1,column=2)
    def highlight_search(self):

        self.text_area.tag_remove('found', '1.0', END)

        s = edit.get()
        if s:
            idx = '1.0'
            while 1:
                idx = self.text_area.search(s, idx, nocase=1, stopindex=END)
                if not idx: break

                lastidx = '%s+%dc' % (idx, len(s))

                self.text_area.tag_add('found', idx, lastidx)
                idx = lastidx

            self.text_area.tag_config('found', foreground=self.highlighted_color)
        edit.focus_set()


root=Tk()
root.geometry("900x500")
font_for_text = Font(family="Times New Roman", size=19, weight="normal")
te=editor(root)


root.mainloop()