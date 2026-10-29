# Patimah Azzahra_006
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        # Inisialisasi Model dan View
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
        )

        # >>> TAMBAH 1: variabel penyimpan id_buku dari baris yang diklik
        self.id_terpilih = None

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)

        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol simpan
        if self.user_role != "admin":
           self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")          
           self.view.entry_judul.configure(state="disabled")
           self.view.entry_penulis.configure(state="disabled")
           self.view.entry_tahun.configure(state="disabled")
        
        # >>> TAMBAH 2 : binding tombol Hapus, Perbarui, dan klik baris tabel
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    # >>> TAMBAH 3 (awal): fungsi pilih_baris
    def pilih_baris(self, event=None):
        pilihan = self.view.tabel.selection()
        if not pilihan:
            return

        nilai = self.view.tabel.item(pilihan[0], 'values')
        # nilai = (id_buku, judul, penulis, tahun_terbit)
        self.id_terpilih = nilai[0]

        # Tampilkan data baris ke form input
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_judul.insert(0, nilai[1])
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_penulis.insert(0, nilai[2])
        self.view.entry_tahun.delete(0, 'end')
        self.view.entry_tahun.insert(0, nilai[3])
        
    # Patimah Azzahra_006 
    def simpan_data(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return
        
        # Mengambil teks dari kotak input di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo( "Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            # Muat ulang tabel agar data terbaru muncul
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    # >>> TAMBAH 5 (awal): fungsi hapus_data
    def hapus_data(self):
        if not self.id_terpilih:
            messagebox.showwarning("Peringatan", "Pilih data pada tabel yang akan dihapus!")
            return

        if not messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            return

        # Teruskan id_buku ke fungsi hapus di BukuModel
        berhasil = self.model.delete_buku(self.id_terpilih)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.id_terpilih = None
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    # >>> TAMBAH 6 (awal): fungsi perbarui_data
    def perbarui_data(self):
        if not self.id_terpilih:
            messagebox.showwarning("Peringatan", "Pilih data pada tabel yang akan diperbarui!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Teruskan id_buku beserta data baru ke fungsi update di BukuModel
        berhasil = self.model.update_buku(self.id_terpilih, judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.id_terpilih = None
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")
    
    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()