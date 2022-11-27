from tkinter import *
from Crypto.Cipher import AES
from secrets import token_bytes #pip install secrets
from tkinter import messagebox
from menu import menuWin

class encryptWin(Frame):
    def __init__(self, root=None):
        super().__init__(root, width=300, height=250)
        self.root = root
        self.pack()
        self.widgetInput()
        self.btnInput()

    def widgetInput(self):
        self.frameInput = Frame(self)
        self.frameInput.grid(column=0, row=0)
        self.frameInput.config(width="200", height="200", padx=5, pady=5)
        self.frameInput.place(x=150, y=90, anchor=CENTER)

        self.lblUser = Label(self.frameInput, text="Usuario")
        self.lblUser.grid(column=0, row=0)
        self.lblUser.config(width="10", height="2")
        self.inputUser = Entry(self.frameInput)
        self.inputUser.grid(column=0, row=1)
        self.inputUser.config(width="30", justify="center")

        self.lblPass = Label(self.frameInput, text="Contraseña")
        self.lblPass.grid(column=0, row=2)
        self.lblPass.config(width="10", height="2")
        self.inputPass = Entry(self.frameInput)
        self.inputPass.grid(column=0, row=3)
        self.inputPass.config(width="30", justify="center")
        
    def btnInput(self):
        self.btnStart = Button(self, text="Iniciar") #Btn Iniciar
        self.btnStart.place(x=100, y=180, anchor=CENTER)
        self.btnStart.config(width="10", height="1", command=self.iniciar)
        
        self.btnReturn = Button(self, text="Volver") #Btn Volver
        self.btnReturn.config(width="10", height="1", command=self.volver)
        self.btnReturn.place(x=200, y=180, anchor=CENTER)

    def iniciar(self):
        if self.inputUser.get() == "" or self.inputPass.get() == "":
            messagebox.showerror("Error", "No se permiten campos vacios")
        else:
            user, password = self.leerTxt()
            key, nonce, ciphertext, tag = self.encriptar(user, password)
            if self.inputUser.get() == user and self.inputPass.get() == self.descifrar(key, nonce, ciphertext, tag):
                messagebox.showinfo("Iniciar", "Iniciando sesion")
                self.root.destroy()
                menuWin()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def leerTxt(self):
        with open("user.txt", "r") as file:
            for line in file:
                user, password = line.split(" ")
                return user, password

    def encriptar(self, user, password):
        key = token_bytes(16)
        #with open("key.key", "wb") as file:
            #file.write(key)
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(password.encode("ascii"))
        return key, nonce, ciphertext, tag

    def descifrar(self, key, nonce, ciphertext, tag):
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)
        try:
            cipher.verify(tag)
            return plaintext.decode("ascii")
        except ValueError:
            print("Clave incorrecta o mensaje corrupto")

    def volver(self): #Arreglar
        pass 
        
if __name__ == "__main__" or __name__ == "main":
    root = Tk()
    app = encryptWin(root)
    root.resizable(0,0)
    root.title("Iniciar sesión")
    root.geometry("300x250") 
    root.iconbitmap("icon.ico")
    root.mainloop()