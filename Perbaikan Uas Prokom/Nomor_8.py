#A (Mengurutkan Data Anggota)
import json
from anggota import clear

def bubblesort(anggotas):
    a = len(anggotas)
    for x in range(a - 1):
        for y in range(a - x - 1):
            if anggotas[y]["idanggota"] > anggotas[y + 1]["idanggota"]:
                anggotas[y], anggotas[y + 1] = anggotas[y + 1], anggotas[y]

def tampilkan_anggota_sorted():
    with open("anggotas.json", "r") as file:
        anggotas = json.load(file)

    anggota_list = list(anggotas.values())
    bubblesort(anggota_list)

    for anggota in anggota_list:
        print("ID Anggota:", anggota["idanggota"])
        print("Nama:", anggota["nama"])
        print("Alamat:", anggota["alamat"])
        print("Telepon:", anggota["telepon"])
        print("Tanggal Daftar:", anggota["tanggal"])
print()

#B (Pelaporan Transaksi)
import json
import os


def laporan_transaksi(idanggota):
    filename = f'tabungan{idanggota}.json'

    if os.path.isfile(filename):
        with open(filename) as file:
            data_tabungan = json.load(file)

        for tabungan in data_tabungan:
            print("===============================================")
            print("Tanggal Transaksi    :", tabungan["tanggal"])
            print("ID Anggota           :", tabungan["idtransaksi"])
            print("Tipe Transaksi       :", tabungan["tipetransaksi"])
            print("Jumlah Transaksi     :", tabungan["total"])
            print("Saldo                :", tabungan["saldo"])
            print()
    else:
        print("Data tabungan tidak ditemukan.")
        return