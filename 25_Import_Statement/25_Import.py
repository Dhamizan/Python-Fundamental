# import mtk
import sapa

sapa.sapa_pengguna("Dio")
# hasil = mtk.tambah(2,4)
# print(hasil)

# Bisa juga begini - From "fil/module" import "fungsi"
from mtk import tambah
hasil = tambah(2,4)
print(hasil)

# Kalau filenya di dalam folder:
import package.module_mtk
# Maka harus begini - From "folder" import "file/module" import "fungsi"
hasil = package.module_mtk.tambah(2,4)
print(hasil)

# Kurleb begitu lah yaaa