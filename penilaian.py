#Tambah data mahasiswa
def tambah_data(data_mahasiswa):
    while True:
        try:
            nim = int(input("Masukan data NIM mahasiswa: "))
            if nim < 0:
                raise ValueError("NIM tidak boleh negatif.")
            # Periksa apakah NIM sudah ada dalam data mahasiswa
            if any(mahasiswa['nim'] == nim for mahasiswa in data_mahasiswa):
                raise ValueError("NIM sudah ada dalam data mahasiswa.")
            break  # Keluar dari loop jika nim valid
        except ValueError as e:
            if "invalid literal for int() with base 10" in str(e):
                print("NIM harus berupa angka.")
            else:
                print(e)

    nama = input("Masukkan data nama mahasiswa: ")
    while True:
        try:
            nilai = int(input("Masukkan data nilai mahasiswa: "))
            if nilai < 0:
                raise ValueError("nilai tidak boleh negatif.")
            break  # Keluar dari loop jika nim valid
        except ValueError as e:
            if "invalid literal for int() with base 10" in str(e):
                print("Nilai harus berupa angka.")
            else:
                print(e)
    data_mahasiswa.append({'nim': nim, 'nama': nama, 'nilai': nilai})
    print("Data mahasiswa berhasil ditambahkan.")


#Function Sort Maximum Turun
def urutkan_data_nilai(data_mahasiswa):
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        n = len(data_mahasiswa)
        for i in range(0, n - 1):
            imax = i
            for j in range(i + 1, n):
                if data_mahasiswa[j]['nilai'] > data_mahasiswa[imax]['nilai']:
                    imax = j
            temp = data_mahasiswa[i]
            data_mahasiswa[i] = data_mahasiswa[imax]
            data_mahasiswa[imax] = temp
        print("Data mahasiswa berhasil diurutkan berdasarkan nilai secara menurun.")
        return data_mahasiswa

#Function Sort Maximum Naik
def urutkan_data_nim(data_mahasiswa):
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        n = len(data_mahasiswa)
        for i in range(n-1,0,-1):
            imax = i
            for j in range(i-1,-1,-1):
                if data_mahasiswa[j]['nim'] > data_mahasiswa[imax]['nim']:
                    imax = j
            temp = data_mahasiswa[i]
            data_mahasiswa[i] = data_mahasiswa[imax]
            data_mahasiswa[imax] = temp
        print("Data mahasiswa berhasil diurutkan berdasarkan NIM secara naik.")
        return data_mahasiswa
    
#Procedure Tampilkan data mahasiswa
def tampilkan_daftar(data_mahasiswa):
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for mahasiswa in data_mahasiswa:
            print(f"NIM: {mahasiswa['nim']} - {mahasiswa['nama']} - Nilai: {mahasiswa['nilai']} - Indeks: {hitung_indeks(mahasiswa['nilai'])}")

#Function Binary Search
def pencarianBiner(data, dicari):
    bawah = 0
    atas = len(data) - 1
    while bawah <= atas:
        tengah = (bawah + atas) // 2
        if data[tengah]['nama'] == dicari:
            return tengah
        elif data[tengah]['nama'] < dicari:
            bawah = tengah + 1
        else:
            atas = tengah - 1
    return -1

def urutkan_data_nama(data_mahasiswa):
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    else:
        sorted_data = sorted(data_mahasiswa, key=lambda x: x['nama'])
        return sorted_data


#Procedure Mencari Data mahasiswa berdasarkan nama
def cari_data(data_mahasiswa):
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        nama_cari = input("Masukkan nama mahasiswa yang ingin dicari: ")
        data_urut = urutkan_data_nama(data_mahasiswa)
        posisi = pencarianBiner(data_urut, nama_cari)
        if posisi >= 0:
            mahasiswa = data_urut[posisi]
            print(f"Mahasiswa {nama_cari} ditemukan dengan NIM {mahasiswa['nim']} dan nilai {mahasiswa['nilai']} dan indeks {hitung_indeks(mahasiswa['nilai'])}.")
        else:
            print("Mahasiswa tidak ditemukan.")

def hitung_indeks(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

#Program Utama
data_mahasiswa = []

while True:
        print("\nPilihan:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Daftar Mahasiswa")
        print("3. Urutkan Daftar Mahasiswa berdasarkan Nilai")
        print("4. Cari Mahasiswa")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            tambah_data(data_mahasiswa)
        elif pilihan == '2':
            tampilkan_daftar(data_mahasiswa)
        elif pilihan == '3':
            print("Urutkan Berdasarkan? 1.NIM atau 2.Nilai")
            pilih = input("Masukan Pilihan Anda : ")
            if pilih == '1':
                data_mahasiswa = urutkan_data_nim(data_mahasiswa)
            elif pilih == '2':
                data_mahasiswa = urutkan_data_nilai(data_mahasiswa)
        elif pilihan == '4':
            cari_data(data_mahasiswa)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

