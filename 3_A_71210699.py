kata = input("Masukkan Kalimat: ")
mulai = int(input("Index start: "))
berhenti = int(input ("Index Stop: "))

def hitung_hapus (kata, mulai, berhenti):
    hitung1 = len(kata)
    hitung2 = len(kata[mulai - 1:berhenti])
    hitung3 = (hitung2 / hitung1) * 100
    return hitung3

print (hitung_hapus (kata, mulai, berhenti))
