print("======== Calculator sederhana ========")
print("""1. Pertambahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Pangkat""")

menu = int(input("Masukan pilihan: "))
bil1 = int(input("Masukan bilangan 1: "))
bil2 = int(input("Masukan bilangan 2: "))

def calculator(menu):   
   if menu == 1:
      print("Hasilnya:", tambah(bil1,bil2))
   elif menu == 2:
      print("Hasilnya:", kurang(bil1,bil2))
   elif menu == 3:
      print("Hasilnya:", kali(bil1,bil2))
   elif menu == 4:
    print("Hasilnya:", bagi(bil1,bil2))
   elif menu == 5:
      print("Hasilnya:", pangkat(bil1,bil2))
   else:
      print("Hasilnya: Maaf input operasi antara 1-5")
def tambah(bil1, bil2):
   return bil1 + bil2
def kurang(bil1, bil2):
   return bil1 - bil2
def bagi(bil1, bil2):
   return bil1 / bil2
def kali(bil1, bil2):
   return bil1 * bil2
def pangkat(bil1, bil2):
   return bil1 ** bil2
   
calculator(menu)