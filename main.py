from tkinter import *
from tkinter import Frame
from encrypt import encryptWin

class mainWin(Frame):
    def __init__(self, root=None):
        super().__init__(root, width=400, height=400)
        self.root = root
        self.pack()
        self.widgets()

    def widgets(self):
        self.lblFrame = LabelFrame(self)
        self.lblFrame.grid(column=0, row=0)
        self.lblFrame.config(width="500", height="500", padx=5, pady=5)
        self.lblFrame.place(x=200, y=200, anchor=CENTER)

        self.btnScan=Button(self.lblFrame,text="Escanear")
        self.btnScan.grid(column=0,row=0)
        self.btnScan.config(width="30",height="3")
        self.btnSave=Button(self.lblFrame,text="Menu")
        self.btnSave.grid(column=0,row=1)
        self.btnSave.config(width="30",height="3", command = self.actionEncryp)

    def actionEncryp(self):
        self.root.destroy()
        encryptWin()

if __name__ == "__main__":
    root = Tk()
    app = mainWin(root)
    root.resizable(0,0)
    root.title("Menu") 
    root.iconbitmap("icon.ico")
    root.mainloop()