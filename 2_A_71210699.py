def ambil_tengah(kata, tambah = 0):
    if(tambah):
        hitung1 = len(kata)
        dibagi = (hitung1 // 2)
        return(kata[dibagi + tambah])
    else:
        hitung1 = len(kata)
        dibagi = (hitung1 // 2)
        return(kata[dibagi])

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd",))