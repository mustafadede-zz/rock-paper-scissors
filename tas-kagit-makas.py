import random
import time
print("-"*30)
print("Programa hoşgeldiniz.")
print("-"*30)

print("1 - Taş\n2 - Kağıt\n3 - Makas")

kullanıcı = input("Oyuna başlamak mı çıkmak mı istiyorsun ? Gir : e/q : ")
a = True
kullanıcı_can = 3
pc_can = 3

while a:

    if kullanıcı == "Q" or kullanıcı == "q":
        print("Çıkılıyor...")
        time.sleep(2)
        a = False

    if kullanıcı == "E" or kullanıcı == "e":
        print(f"\n**** Canın : {kullanıcı_can} , bilgisayarın canı : {pc_can} ****\n")
        if kullanıcı_can == 0:
            print("Canın kalmadı")
            time.sleep(2)
            break
        elif pc_can == 0:
            print("KAZANDIN !")
            time.sleep(2)
            break
        secim = input("Yukarıda var olan rakamlardan birisini gir:")

        pc = random.choice(["Taş","Kağıt","Makas"])

        if secim == "1":
            secim = "Taş"
            print(f"Senin seçimin : {secim}, Bilgisayarın seçimi : {pc}")
            if pc == "Kağıt":
                print("Bilgisayar yendi.")
                kullanıcı_can -= 1
            elif pc == "Taş":
                print("Berabere")
            elif pc == "Makas":
                print("Sen yendin.")
                pc_can -= 1

        elif secim == "2":
            secim="Kağıt"
            print(f"Senin seçimin : {secim}, Bilgisayarın seçimi : {pc}")
            if pc == "Makas":
                print("Bilgisayar yendi.")
                kullanıcı_can -= 1
            elif pc == "Kağıt":
                print("Berabere")
            elif pc == "Taş":
                print("Sen yendin.")
                pc_can -= 1

        elif secim == "3":
            secim="Makas"
            print(f"Senin seçimin : {secim}, Bilgisayarın seçimi : {pc}")
            if pc == "Taş":
                print("Bilgisayar yendi.")
                kullanıcı_can -= 1
            elif pc == "Makas":
                print("Berabere")
            elif pc == "Kağıt":
                print("Sen yendin")
                pc_can -= 1

        else:
            print("Var olan sayılardan gir") 