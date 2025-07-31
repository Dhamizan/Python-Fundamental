import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
    
# Window
window = tk.Tk()
window.configure(bg="white")
window.geometry("600x400")
window.resizable(False,False)
window.title("Sapa Dia!")
window_frame = ttk.Frame()
window_frame.pack(padx=10, pady=10, expand=True, fill="x")

# PROGRAM Tambah, Kurang, Bagi, Kali
ANGKA_1 = tk.IntVar()
ANGKA_2 = tk.IntVar()
OPERASI = tk.StringVar()

def tambah():
    a = ANGKA_1.get()
    b = ANGKA_2.get()
    hasil = a + b
    showinfo(title="Hasilnya", message=hasil)
    
def kurang():
    a = ANGKA_1.get()
    b = ANGKA_2.get()
    hasil = a - b
    showinfo(title="Hasilnya", message=hasil)
    
def bagi():
    a = ANGKA_1.get()
    b = ANGKA_2.get()
    hasil = a / b
    showinfo(title="Hasilnya", message=hasil)
    
def kali():
    a = ANGKA_1.get()
    b = ANGKA_2.get()
    hasil = a * b
    showinfo(title="Hasilnya", message=hasil)

# Label Angka_1
al1 = ttk.Label(window_frame, text="Angka Pertama:")
al1.pack(padx=10, pady=10, expand=True, fill="x")

# Inputan Angka_1
e1 = ttk.Entry(window_frame, textvariable=ANGKA_1)
e1.pack(padx=10, pady=10, expand=True, fill="x")

# Label Angka_2
al2 = ttk.Label(window_frame, text="Angka Kedua:")
al2.pack(padx=10, pady=10, expand=True, fill="x")

# Inputan Angka_2
e2 = ttk.Entry(window_frame, textvariable=ANGKA_2)
e2.pack(padx=10, pady=10, expand=True, fill="x")

# Tombol
tombol_tambah = ttk.Button(window_frame, text="+", command=tambah)
tombol_tambah.pack(padx=10, pady=10, expand=True, fill="x")

tombol_kurang = ttk.Button(window_frame, text="-", command=kurang)
tombol_kurang.pack(padx=10, pady=5, expand=True, fill="x")

tombol_kali = ttk.Button(window_frame, text="x", command=kali)
tombol_kali.pack(padx=10, pady=5, expand=True, fill="x")

tombol_bagi = ttk.Button(window_frame, text="/", command=bagi)
tombol_bagi.pack(padx=10, pady=5, expand=True, fill="x")

window.mainloop()