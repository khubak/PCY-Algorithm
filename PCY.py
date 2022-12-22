import functions
from collections import defaultdict
from itertools import combinations

input_file = functions.parser_sprut()

brKosara = input_file[0]
s = input_file[1]
brPretinaca = input_file[2]

prag = s * brKosara

brPredmeta = defaultdict(int)

for kosara in input_file[3:]:
    for predmet in kosara:
        brPredmeta[predmet] += 1

pretinci = defaultdict(int)
velicinaBrPredmeta = len(brPredmeta)
A = int((velicinaBrPredmeta * (velicinaBrPredmeta - 1)) / 2)

indeksi = []
j = 0

for kosara in input_file[3:]:
    indeksi.append([])
    for i in kosara:
        if(brPredmeta[i] >= prag):
            indeksi[j].append(i)
    j += 1

for kosara in indeksi:

    for i, j in combinations(kosara, 2):
        pretinci[((i * velicinaBrPredmeta) + j) % brPretinaca] += 1

parovi = defaultdict(int)

for kosara in indeksi:
    for i, j in combinations(kosara, 2):
        if(pretinci[((i * velicinaBrPredmeta) + j) % brPretinaca] >= prag):
            parovi[(i, j)] += 1

P = int(len(parovi))

print(A)
print(P)

pairs = list(parovi.values())
pairs.sort(reverse=True)

print(*pairs, sep='\n')
