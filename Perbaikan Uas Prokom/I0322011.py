from anggota import tampilkan_anggota, cari_anggota_by_id, tambah_anggota, edit_anggota, generate_idanggota, clear
from tabungansampah import tambah_tabungan, tarik_tabungan
from Nomor_8 import tampilkan_anggota_sorted,laporan_transaksi

def main():
    while True:
        clear()
        print("=========================================")
        print("   Program Pengelolaan Tabungan Sampah   ")
        print("=========================================")
        print("Pilihan menu:")
        print("1. Menu Pengelolaan Anggota")
        print("   1a. Penambahan Data Anggota")
        print("   1b. Pencarian Data Anggota")
        print("   1c. Pengubahan Data Anggota")
        print("2. Menu Tabungan Anggota")
        print("   1a. Penambahan Tabungan")
        print("   1b. Penarikan Tabungan")
        print("3. Menu Data Anggota")
        print("4. Laporan Transaksi")
        print("5. Exit")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1a":
            clear()
            print("Penambahan data anggota.")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            telepon = input("Telepon: ")
            tambah_anggota(nama=nama, alamat=alamat, telepon=telepon)
            input("Tekan tombol Enter untuk melanjutkan...")

        elif pilihan == "1b":
            clear()
            print("Pencarian data anggota")
            idanggota = input("Masukkan ID Anggota: ")
            data_anggota = cari_anggota_by_id(idanggota)               
            if data_anggota:
                print(data_anggota)
            else:
                print("{}")
            tampilkan_anggota(data_anggota)
            input("Tekan tombol Enter untuk melanjutkan...")

        elif pilihan == "1c":
            clear()
            print("Pengubahan data anggota")
            edit_anggota()
            pilihan = input("Cari lagi? (Y/y=Ya, T/t=Tidak): ")
            if pilihan.lower() == 'y':
                edit_anggota()
            return

        elif pilihan == "2a":
            print("Penambahan Tabungan Sampah.")
            idanggota = input("Input ID Anggota : ")

            data_anggota = cari_anggota_by_id(idanggota)

            if not data_anggota:
                print("Data anggota tidak ditemukan!")
                pilihan = input("Cari lagi (Y/y = Ya, T/t = Tidak)? ")
                if pilihan.lower() == 'y':
                    main()
                return

            
            tambah_tabungan(idanggota)       
        elif pilihan == "2b":
            print("Penarikan Tabungan Sampah.")
            idanggota = input("Input ID Anggota : ")
            
            tarik_tabungan(idanggota)

        elif pilihan == "2c" :
            clear()
            print("Penarikan Tabungan Sampah.")
            idanggota = input("Input ID Anggota : ")
            tampilkan_anggota(idanggota)
            input("Tekan tombol Enter untuk melanjutkan...")

        elif pilihan == "3":
            clear()
            print("Data Anggota (Sorted by ID)")
            tampilkan_anggota_sorted()
            print("Data anggota telah diurutkan berdasarkan ID.")
            input("Tekan tombol Enter untuk melanjutkan...")

        elif pilihan == "4":
            idanggota = input("Input ID Anggota : ")
            laporan_transaksi(idanggota)
            input("Tekan tombol Enter untuk melanjutkan...")

        elif pilihan == "5":
            clear()
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
            input("Tekan tombol Enter untuk melanjutkan...")

if __name__ == '__main__':
    main()