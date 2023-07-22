import json
import os
from random import randint
from anggota import cari_anggota_by_id


def generate_idtransaksi(idanggota):
    idtransaksi = str(randint(1000000, 9999999))
    return idtransaksi

def cari_harga(idsampah):
    with open('produksampah.json') as file:
        data_sampah = json.load(file)
    for kode, sampah in data_sampah.items():
        if kode == idsampah:
            return float(sampah['hargasatuan'])
    return 0.0



def get_saldo(idanggota):
    with open(f'tabungan{idanggota}.json') as file:
        data_tabungan = json.load(file)
    if data_tabungan:
        return data_tabungan[-1]['saldo']
    return 0

def tambah_tabungan(idanggota):
    filename = f'tabungan{idanggota}.json'

    if os.path.isfile(filename):
        with open(filename) as file:
            data_tabungan = json.load(file)
    else:
        data_tabungan = []

    with open(filename, 'w') as file:
        json.dump(data_tabungan, file, indent=4)

    data_anggota = cari_anggota_by_id(idanggota)
    print(f"IDAnggota: {idanggota} | Nama : {data_anggota['nama']} | Telepon: {data_anggota['telepon']} | Alamat: {data_anggota['alamat']}")
    print("=============================================")
    print("Kode | Jenis Sampah       | Harga Satuan (Rp)")
    print("---------------------------------------------")
    print("1    | Kardus             | 500")
    print("2    | Botol plastic      | 300")
    print("3    | Logam besi         | 800")
    print("4    | Tembaga            | 950")
    print("---------------------------------------------")

    while True:
        kode_sampah = input("Pilih jenis sampah : ")
        kuantitas = float(input("Kuantitas sampah : "))
        hargasatuan = cari_harga(kode_sampah)

        if hargasatuan == 0:
            print("Kode sampah tidak valid. Silakan coba lagi.")
        else:
            break

    idtransaksi = generate_idtransaksi(idanggota)
    tanggal = "2023-06-15"
    tipetransaksi = "K"
    total = kuantitas * hargasatuan
    saldo = get_saldo(idanggota) + total

    data_tabungan.append({
        "tanggal": tanggal,
        "idtransaksi": idtransaksi,
        "tipetransaksi": tipetransaksi,
        "sampah": kode_sampah,
        "kuantitas": kuantitas,
        "nilaisatuan": hargasatuan,
        "total": total,
        "saldo": saldo
    })

    with open(f'tabungan{idanggota}.json', 'w') as file:
        json.dump(data_tabungan, file, indent=4)

    print("Pencatatan transaksi tabungan sampah berhasil.")

    pilihan = input("Ada jenis sampah lain akan ditabung (Y/y = Ya, T/t = Tidak)? ")
    if pilihan.lower() == 'y':
        tambah_tabungan(idanggota)

def tarik_tabungan(idanggota):
    filename = f'tabungan{idanggota}.json'

    if os.path.isfile(filename):
        with open(filename) as file:
            data_tabungan = json.load(file)
    else:
        print("Data tabungan tidak ditemukan.")
        return

    total_saldo = sum(transaksi['saldo'] for transaksi in data_tabungan)

    data_anggota = cari_anggota_by_id(idanggota)
    print(f"IDAnggota: {idanggota} | Nama : {data_anggota['nama']} | Telepon: {data_anggota['telepon']} | Alamat: {data_anggota['alamat']}")
    print("=============================================")
    print(f"Total Saldo: {total_saldo}")

    print("Penarikan tabungan berhasil.")

tarik_tabungan("001")

