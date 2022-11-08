#Emily Rusch

names = { "Brown":"Cody", "Bub":"Julia", "Doherty":"Catherine", "Dunn":"Margaret", "Kevin":"Ellen", "Kieft":"Brenna", "Miloserny":"Amanda", "Nyhuis":"Kaylen", "Reger":"Cadyn", "Rusch":"Emily", "Salazar":"Britney", "Schutz":"Julia", "Shadid":"Christina", "Skrip":"Holly", "Sullivan":"Anna", "Verstraete":"Adrianne", "Wardlow":"Sarah"}

dict2 = sorted(names)
vals1 = names.values()

def histogram(vals1):
    d = dict()
    for char in vals1:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

print(histogram(vals1))

