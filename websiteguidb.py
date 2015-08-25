from tkinter import*
import sqlite3
import webbrowser

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        a = StringVar()
        b = StringVar()
        a1 = StringVar()
        b1 = StringVar()
        c = StringVar()
        self.button = Button(frame, text='Open Db', 
                                      fg='red',
                                      command=self.ouvrir)
        self.button.pack(side=LEFT)

        self.button2 = Button(frame,
                              text='Create Table', 
                              command = self.tabluh)
        self.button2.pack(side=LEFT)

        self.button3 = Button(frame, 
                              text='Close Dbase', 
                              command= self.fermer)
        self.button3.pack(side=LEFT)

        self.button4 = Button(frame, 
                              text='Insert Rec', 
                              command=self.insertar)
        self.button4.pack(side=LEFT)

        self.button5 = Button(frame, 
                              text='List Recs', 
                              command=self.listar)
        self.button5.pack(side=LEFT)

        self.button6 = Button(frame, 
                         text="Create Page", fg="red",
                         command=self.web)

        self.button6.pack(side=LEFT)

        self.button7 = Button(frame,
                         text="Open File", fg="green",
                         command=self.openFile)
    
        self.button7.pack(side=LEFT)

        

        self.a = Entry(frame)
        self.a.pack(side=BOTTOM)
        

        self.b = Entry(frame)
        self.b.pack(side=BOTTOM)
        
       

        self.c = Entry(frame)
        self.c.pack(side=BOTTOM)




        
    def web(self):
          webbrowser.open('summersale.html')


    def openFile(self):
        fname = filedialog.askopenfilename(parent=root)
        fname2 = filedialog.asksaveasfilename()
        dirname = filedialog.askdirectory()
            
        
        
    def ouvrir(self):
        self.con = sqlite3.connect('webpage.db')
        self.cur = self.con.cursor()

    def tabluh(self):
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE page_content(
                            id INT,
                            name stringvar(30),
                            content stringvar(30))''')
    def fermer(self):
        self.con.close()

    def insertar(self):
        a1 = self.a.get()
        b1 = self.b.get()
        c1 = int(self.c.get())
        self.cur.execute \
                         ("INSERT INTO \
                          page_content(id, name, content) \
                          values(?,?,?)", \
                          (c1, a1, b1))

    def listar(self):
        self.cur.execute('SELECT * FROM page_content')
        print(self.cur.fetchall())

root = Tk()
root.title("Webpage GUI")
root.geometry('700x300')
app = App(root)
root.mainloop()
            
                
                                 
        
