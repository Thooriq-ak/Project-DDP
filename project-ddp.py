import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def pesan_pizza():
    ukuran_pizza = var_ukuran.get()
    topping_pizza = var_topping.get()
    crust_pizza = var_crust.get()

    # Dictionary untuk menyimpan harga pizza berdasarkan ukuran
    harga_ukuran = {"Regular": 20000, "Medium": 50000, "Large": 80000}

    # Dictionary untuk menyimpan harga topping pizza
    harga_topping = {"Pepperoni": 10000, "Mushroom": 8000, "Chicken": 12000, "Vegetarian": 9000}

    # Dictionary untuk menyimpan harga crust pizza
    harga_crust = {"Thin Crust": 15000, "Thick Crust": 20000, "Stuffed Crust": 25000}

    # Menghitung total harga pesanan
    total_harga = harga_ukuran.get(ukuran_pizza, 0) + harga_topping.get(topping_pizza, 0) + harga_crust.get(crust_pizza, 0)

    pesan = f"Anda memesan pizza {ukuran_pizza} dengan topping {topping_pizza} dan crust {crust_pizza}. Total harga: Rp{total_harga:,.2f}. Terima kasih!"
    label_hasil.config(text=pesan)

    # Menampilkan daftar harga di label baru
    label_daftar_harga.config(text=f"Daftar Harga:\n{harga_ukuran_text}\n{harga_topping_text}\n{harga_crust_text}\nTotal: Rp{total_harga:,.2f}")

# Membuat jendela utama
app = tk.Tk()
app.title("Aplikasi Pemesanan Pizza Hut")

# Menambahkan gambar pizza sebagai header
img = Image.open("header.jpg")  # Ganti dengan path file gambar pizza yang Anda miliki
img = img.resize((650, 150))
img = ImageTk.PhotoImage(img)
label_gambar_pizza = tk.Label(app, image=img)
label_gambar_pizza.grid(row=0, column=0, columnspan=2, pady=10)

# Variabel StringVar untuk menyimpan pilihan ukuran, topping, dan crust pizza
var_ukuran = tk.StringVar()
var_topping = tk.StringVar()
var_crust = tk.StringVar()

# Label dan OptionMenu untuk ukuran pizza
label_ukuran = tk.Label(app, text="Ukuran Pizza:")
label_ukuran.grid(row=1, column=0, padx=10, pady=10)
ukuran_options = ["Regular", "Medium", "Large"]
ukuran_menu = tk.OptionMenu(app, var_ukuran, *ukuran_options, command=pesan_pizza)
ukuran_menu.grid(row=1, column=1, padx=10, pady=10)

# Label dan OptionMenu untuk topping pizza
label_topping = tk.Label(app, text="Topping Pizza:")
label_topping.grid(row=2, column=0, padx=10, pady=10)
topping_options = ["Pepperoni", "Mushroom", "Chicken", "Vegetarian"]
topping_menu = tk.OptionMenu(app, var_topping, *topping_options, command=pesan_pizza)
topping_menu.grid(row=2, column=1, padx=10, pady=10)

# Label dan OptionMenu untuk crust pizza
label_crust = tk.Label(app, text="Crust Pizza:")
label_crust.grid(row=3, column=0, padx=10, pady=10)
crust_options = ["Thin Crust", "Thick Crust", "Stuffed Crust"]
crust_menu = tk.OptionMenu(app, var_crust, *crust_options, command=pesan_pizza)
crust_menu.grid(row=3, column=1, padx=10, pady=10)

# Tombol pesan pizza
tombol_pesan = tk.Button(app, text="Pesan Pizza", command=pesan_pizza)
tombol_pesan.grid(row=4, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil pesanan
label_hasil = tk.Label(app, text="")
label_hasil.grid(row=5, column=0, columnspan=2, pady=10)

# Membuat Treeview untuk menampilkan harga pizza dalam bentuk tabel
table_columns = ["Komponen", "Harga"]
table = ttk.Treeview(app, columns=table_columns, show="headings")
table.heading("Komponen", text="Komponen")
table.heading("Harga", text="Harga (Rp)")
table.grid(row=6, column=0, columnspan=2, pady=10, rowspan=2)  # Adjust rowspan to make it centered

# Menambahkan data ke dalam tabel
table_data = [
    ("Regular Pizza", 20000),
    ("Medium Pizza", 50000),
    ("Large Pizza", 80000),
    ("Pepperoni Topping", 10000),
    ("Mushroom Topping", 8000),
    ("Chicken Topping", 12000),
    ("Vegetarian Topping", 9000),
    ("Thin Crust", 15000),
    ("Thick Crust", 20000),
    ("Stuffed Crust", 25000),
]
for data in table_data:
    table.insert("", "end", values=data)

# Menjalankan aplikasi
app.mainloop()
