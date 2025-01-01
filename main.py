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

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print("Sonuç:", toplama(sayi1, sayi2))
elif secim == '2':
    print("Sonuç:", cikarma(sayi1, sayi2))
elif secim == '3':
    print("Sonuç:", carpma(sayi1, sayi2))
elif secim == '4':
    print("Sonuç:", bolme(sayi1, sayi2))
else:
    print("Geçersiz seçim!")
