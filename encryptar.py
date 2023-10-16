from tkinter import *
from tkinter import ttk
from cifrado import *

class Aplicacion:

    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Encrytar")
        self.ventana.geometry("500x350")
        self.ventana.resizable(0,0)

        #atributos
        Label(self.ventana,text="Mensaje a cifrar: ").grid(row=0,column=0)
        self.mensaje = Entry(self.ventana, width=50)
        self.mensaje.grid(row=0,column=1, padx=10, pady=10, ipadx=20, ipady=15)
        boton = ttk.Button(self.ventana, text="Encriptar", command=self.encriptar).grid(row=2, columnspan=2)
        Label(self.ventana,text="Mensaje cifrado: ").grid(row=3,column=0)
        self.msgencr = StringVar()
        self.mensaje2 = Entry(self.ventana, width=50, textvariable=self.msgencr)
        self.mensaje2.grid(row=3,column=1, padx=10, pady=10, ipadx=20, ipady=15)

    def encriptar(self):
        key = 34
        msg = self.mensaje.get()
        print(msg)
        encr = Cifrado_XOR().encrypt_string(msg, key)
        self.msgencr.set(encr)
    
if __name__=="__main__":
    ventana=Tk()
    aplicacion=Aplicacion(ventana)
    ventana.mainloop()

