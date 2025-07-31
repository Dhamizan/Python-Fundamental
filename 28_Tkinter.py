# Tkinter
# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()

# while True:
#     pass

window.configure(bg="lightblue")
window.geometry("600x400")
window.resizable(False, False)
window.title("Sapa Orang")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Membuat Variabel
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Fungsi Sapa
def sapa():
    hasil_sapa = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}!"
    showinfo(title="Brooo", message=hasil_sapa)

# Komponen
# Label Nama Depan
ndl = ttk.Label(input_frame, text="Nama Depan:")
ndl.pack(padx=10, pady=10, fill="x", expand=True)

# Entry/Inputan Nama Depan
NAMA_DEPAN = tk.StringVar()
nded = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nded.pack(padx=10, pady=10, fill="x", expand=True)

# Label Nama Belakang
ndb = ttk.Label(input_frame, text="Nama Belakang:")
ndb.pack(padx=10, pady=10, fill="x", expand=True)

# Entry/Inputan Nama Belakang
NAMA_BELAKANG = tk.StringVar()
ndeb = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
ndeb.pack(padx=10, pady=10, fill="x", expand=True)

tombol = ttk.Button(input_frame,text="Sapa!",command=sapa)
tombol.pack(fill='x',expand=True,padx=10,pady=10)

window.mainloop()