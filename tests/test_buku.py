# Patimah Azzahra_006
from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Data palsu yang seolah-olah dikembalikan oleh database
    data_palsu = [
        {'id_buku': 1, 'judul': 'Pemrograman Python', 'penulis': 'Budi', 'tahun_terbit': 2024},
        {'id_buku': 2, 'judul': 'Basis Data MySQL', 'penulis': 'Siti', 'tahun_terbit': 2025},
    ]

    # Memanipulasi (Mock) koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = data_palsu
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.get_all_buku()

    # Memverifikasi data yang dikembalikan sama dengan data dari database
    assert hasil == data_palsu
    assert len(hasil) == 2
    # Memverifikasi query SELECT dijalankan satu kali
    mock_cursor.execute.assert_called_once()
    # Memverifikasi data benar-benar diambil dari cursor
    mock_cursor.fetchall.assert_called_once()