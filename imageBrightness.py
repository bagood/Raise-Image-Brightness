from numpy import asarray # import fungsi array dari modul numpy
import numpy as np # import modul numpy dan disingkat menjadi np
from PIL import Image # import Image dari modul PIL

# membuat fungsi untuk mencari index suatu value menggunakan metode linear search
def linear_search(lists, num_search):
    i = 0
    for l in lists: # melakukan perulangan for loop untuk tiap nilai dalam list
        if l[0] == num_search: # mengecek apakah nilai l[0] sama dengan angka yang ingin dicari
            return i 
        i += 1

# melakukan sorting nilai-nilai yang ada dalam list menggunakan metode bubble sort
def bubble_sort(lists):
    while True:
        breaks = True
        for i in range(0, (len(lists)-1)):
            indeks_pertama = i
            indeks_kedua = i + 1
            if lists[indeks_pertama][0] > lists[indeks_kedua][0]:
                temp = lists[indeks_kedua]
                lists[indeks_kedua] = lists[indeks_pertama]
                lists[indeks_pertama] = temp
                breaks = False
        if breaks:
            break
    return lists

# menghitung distribusi massa peluang dari matrix dari foto
def calc_pmf(matrices):
    pmf = [] # membuat list kosong untuk menyimpan hasil massa peluang yang dihitung
    for matrix in matrices: 
        for vektor in matrix:
            for value in vektor:
                list_cek = [v[0] for v in pmf] # menyimpan seluruh variabel massa peluang yang telah diitung sampai proses ini ke dalam suatu list
                if value not in list_cek: # mengecek apakah nilai value tidak ada di list_cek
                    store = [value, 1] # membuat sebuah list yang akan ditambahkan ke list yang bersikan nilai pmf
                    pmf.append(store)
                else: # kode ini akan berjalan apabila niali value sudah ada di dalam list_cek
                    index = linear_search(pmf, value) # mencari index yang memuat nilai value dalam pmf menggunakan fungsi linear search
                    pmf[index][1] += 1 # menambahkan 1 ke dalam frekuensi pmf yang sedang dihitung
    nums = matrices.shape[0] * matrices.shape[1] * matrices.shape[2] # menghitung jumlah data yang ada dalam matrices
    for i in range(0, len(pmf)): # melakukan perulangan untuk tiap massa peluang yang ada dalam pmf
        pmf[i][1] = pmf[i][1] / nums # membagi nilai frekuensi tiap variabel dalam pmf untuk memperoleh pmf dari variabel tersebut
    return pmf

# menghitung distribusi kumulatif peluang dari distribusi massa peluang yang telah dihitung dan diurutkan berdasarkan variabelnya dari terkecil ke terbesar
def calc_cdf(pmf_sorted):
    cdf = [] # membuat list kosong untuk menyimpan hasil perhitungan cdf
    sum = 0 # membuat variabel sum yang akan digunakan untuk meyimpan hasil perhitungan massa peluang
    for p in pmf_sorted: # melakukan perulangan untuk tiap variabel yang ada dalam distribusi massa peluang
        sum += p[1] # menjumlahkan seluruh massa peluang sepanjang proses perulangan
        store = [p[0], sum] # membuat list untuk menyimpan nilai variabel awal dengan peluang kumulatif nya
        cdf.append(store)
    return cdf

# melakukan proses histogram equalization untuk membuat foto menjadi lebih terang
def hist_equalization(cdf, matrices):
    num_levels = len(cdf) - 1 # menghitung pengali yang akan digunakan selama proses melakuka histogram equalization
    new_value = [[c[0], round(c[1] * num_levels)] for c in cdf] # membuat sebuah list berisikan variable sebelum dilakukan hist equal dan sesudah dilakukan hist equal
    new_matrices = [] # membuat variabel baru untuk menyimpan matriks baru yang telah diubah nilainya dengan value baru hasil daru proses histogram equalization
    for matrix in matrices: # melakukan perulangan untuk mengubah nilai variabel yang lama menjadi variable yang baru sesuai dengan proses histogram equalization
        new_matrix = []
        for vektor in matrix:
            new_vektor = []
            for value in vektor:
                new_vektor.append(new_value[value][1])
            new_matrix.append(new_vektor)
        new_matrices.append(new_matrix)
    new_matrices = np.array(new_matrices, dtype='uint8') # mengubah tipe matrix dari list menjadi array dan seluruh variabelnya memiliki tipe 'uin8'
    return new_matrices

# melakukan seluruh proses 
def final_processing(poto): 
    image = Image.open(poto) # mengimport foto ke direktori
    matrices = asarray(image) # membuat matriks dari poto
    pmf = calc_pmf(matrices) # menghitung pmf menggunakan fungsi calc_pmf
    pmf_sorted = bubble_sort(pmf) # mensort pmf berdasarkan variabelnya
    cdf = calc_cdf(pmf_sorted) # menmbuat cdf dari pmf menggunakan fungsi calc_cdf
    new = hist_equalization(cdf, matrices) # melakukan proses histogram equalization
    image_new = Image.fromarray(new) # membentuk poto dari matriks yang telah dimanipulasi
    image.show() # mencetak poto sebelum dienhance brightness nya
    image_new.show() # mencetak poto setelah dienhance brightness nya
    return ''

file_name = input('Type in the file name: ')
final_processing(file_name) # masukkan nama file foto anda ke dalam fungsi ini