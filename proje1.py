_author_="Dilek"


while True:

    say1=input("Sayi 1 degerini giriniz:")
    say2=input("Sayi 2 degerini giriniz:")
    print("Sayilarin toplami  (1) ")
    print("Sayilarin cikarimi (2) ")
    print("Sayilarin carpimi  (3) ")
    print("Sayilarin bolomu   (4) ")
    secim=input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
    print

    if secim =="1":
        print("Sayilarin Toplami =", int(say1)+int(say2))
        print
    elif secim =="2":
        print("Sayilarin cikarimi =", int(say1)-int(say2))
        print
    elif secim == "3":
        print("Sayilarin carpimi =", int(say1)*int(say2))
        print
    elif secim =="4":
        print("Sayilarin bolumu =", int(say1)/int(say2))
        print
    else:
        print("Geçersiz bir işlem girdiniz!!!")
        break