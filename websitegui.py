from tkinter import*
import webbrowser
import tkinter.filedialog


class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()


    
    self.button = Button(frame, 
                         text="Create Page", fg="red",
                         command=self.web)

    self.button.pack(side=LEFT)

    self.button = Button(frame,
                         text="Open File", fg="green",
                         command=self.openFile)
    
    self.button.pack(side=LEFT)

    scroll = Scrollbar(frame, orient=VERTICAL)
    select = Listbox(frame, yscrollcommand=scroll.set, width=20, height=20)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)

    

    

  def web(self):
      webbrowser.open('summersale.html')


  def openFile(self):
    fname = filedialog.askopenfilename(parent=root)
    fname2 = filedialog.asksaveasfilename()
    dirname = filedialog.askdirectory()
        

                     



 
   










root = Tk()
app = App(root)
mainloop()
