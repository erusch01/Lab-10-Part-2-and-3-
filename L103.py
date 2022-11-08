#Emily Rusch

cpsc_names = ["Cody", "Brown", "Julia", "Bub", "Catherine", "Doherty", "Margaret", "Dunn", "Haley", "Greene", "Isabela", "Guthrie Beckstrom", "Danielle","Hongell", "Camryn", "Hurley", "Ellen", "Kevin", "Brenna", "Kieft", "Amanda", "Miloserny", "Kaylen", "Nyhuis", "Cadyn", "Reger", "Emily", "Rusch", "Britney", "Salazar", "Julia", "Schutz", "Christina", "Shadid", "Holly", "Skrip", "Anna", "Sullivan", "Adrianne", "Verstraete", "Sarah", "Wardlow"]

#cpsc_names[::2]  #Even
#cpsc_names[1::2]  #Odd


def histogram(cpsc_names):
    d = dict()
    for val in cpsc_names[1::2]:
        if val[0] not in d:
            d[val[0]] = 1
        else:
            d[val[0]] += 1
    return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = (histogram(cpsc_names))
inverse = invert_dict(hist)

print(inverse)
