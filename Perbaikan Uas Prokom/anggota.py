import json
import random
import string
import datetime
import os

#2A (Tambah Anggota)
def tambah_anggota(nama, alamat, telepon):
    with open('anggotas.json') as file:
        data = json.load(file)

    idanggota = generate_idanggota()

    anggota_tambahan = {
        idanggota: {
            "idanggota": idanggota,
            "nama": nama,
            "alamat": alamat,
            "tanggal": datetime.datetime.now().strftime('%Y-%m-%d'),
            "telepon": telepon
        }
    }
    data.update(anggota_tambahan)

    with open("anggotas.json", "w") as file:
        json.dump(data, file, indent=4)

    print("=" * 50)
    print("Berhasil menambahkan data anggota.")
    print("=" * 50)

#2B (Cari Anggota)
def cari_anggota_by_id(idanggota):
    with open("anggotas.json") as file:
        data_anggota = json.load(file)

    anggota = data_anggota.get(idanggota, {})
    return anggota

#2C (Tampilkan Anggota)
def tampilkan_anggota(data):
    if data:
        print("ID Anggota   :", data['idanggota'])
        print("Nama         :", data['nama'])
        print("Alamat       :", data['alamat'])
        print("Telepon      :", data['telepon'])
        print("Tanggal Daftar:", data['tanggal'])
    else:
        print("Tidak ada data anggota!")

#2D (Edit Data Anggota)
def edit_anggota():
    id_anggota = input("Ketik ID Anggota yang akan diedit: ")
    data_anggota = cari_anggota_by_id(id_anggota)

    if data_anggota:
        print("Nama: " + data_anggota["nama"])
        print("Alamat: " + data_anggota["alamat"])
        print("Telepon: " + data_anggota["telepon"])
            
        nama_baru = input("Nama       : (" + data_anggota['nama'] + ") -> ")
        if nama_baru:
            data_anggota["nama"] = nama_baru

        alamat_baru = input("Alamat     : (" + data_anggota['alamat'] + ") -> ")
        if alamat_baru:
            data_anggota["alamat"] = alamat_baru

        telepon_baru = input("Telepon    : (" + data_anggota['telepon'] + ") -> ")
        if telepon_baru:
            data_anggota["telepon"] = telepon_baru

        with open("anggotas.json", "r") as file:
            anggotas = json.load(file)
            anggotas[id_anggota] = data_anggota

        with open("anggotas.json", "w") as file:
            json.dump(anggotas, file)

        print("Data berhasil diubah.")
    else:
        print("Data anggota tidak ditemukan!")

def generate_idanggota():
    idanggota = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return idanggota

def clear():
    print("\033[H\033[J")