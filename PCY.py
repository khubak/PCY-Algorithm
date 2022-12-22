import functions
#import time
from collections import defaultdict
from itertools import combinations

#start_time = time.time()

input_file = functions.parser_sprut()

brKosara = input_file[0]
s = input_file[1]
brPretinaca = input_file[2]

prag = s * brKosara

brPredmeta = defaultdict(int)

for kosara in input_file[3:]:
    for predmet in kosara:
        brPredmeta[predmet] += 1

#print('time1 = ', time.time() - start_time)

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

#indeksi = [i for kosara in (input_file[3:]) for i in kosara if brPredmeta[i] >= prag]

#print('time2 = ', time.time() - start_time)

for kosara in indeksi:

    for i, j in combinations(kosara, 2):
            #print(i, j)
            #if((brPredmeta[i] >= prag) and (brPredmeta[j] >= prag)):
                pretinci[((i * velicinaBrPredmeta) + j) % brPretinaca] += 1

#print('time3 = ', time.time() - start_time)

parovi = defaultdict(int)

for kosara in indeksi:

    #duljina_kosare = len(kosara)

    for i, j in combinations(kosara, 2):
            #if(i == j):
            #    break
            #if ((brPredmeta[i] >= prag) and (brPredmeta[j] >= prag)):

                if(pretinci[((i * velicinaBrPredmeta) + j) % brPretinaca] >= prag):
                    parovi[(i, j)] += 1

#print('time4 = ', time.time() - start_time)
#nadalje isti tajmovi
P = int(len(parovi))

#print('time5 = ', time.time() - start_time)

print(A)
print(P)

pairs = list(parovi.values())
pairs.sort(reverse=True)

#print('time6 = ', time.time() - start_time)

print(*pairs, sep='\n')

#print('running_time = ', time.time()-start_time)