def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Bir sayı sıfıra bölünemez!"
    return a / b

print("Hesap Makinesi")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminizi yapın (1/2/3/4): ")

sayi3 = float(input("Birinci sayıyı girin lütfen: "))
sayi4 = float(input("İkinci sayıyı girin lütfen: "))

if secim == '1':
    print("Sonuç:", toplama(sayi3, sayi4))
elif secim == '2':
    print("Sonuç:", cikarma(sayi3, sayi4))
elif secim == '3':
    print("Sonuç:", carpma(sayi3, sayi4))
elif secim == '4':
    print("Sonuç:", bolme(sayi3, sayi4))
else:
    print("Geçersiz seçim!")
