
cumle=("dılek oküla gıt")
THarfler=("ı","ç","ş","ü","ö")
iHarfler=("i","ç","s","u","o")

for i in cumle:
    for harf in THarfler:
        if harf==i:
            b=THarfler.index(harf)
            x=cumle.replace(i,iHarfler[b])
            cumle=x
print(cumle)















