import itertools

strg=input('Informe uma palavra a ser permutada: ')
result = itertools.permutations(strg, len(strg))

for i in result:
    print(''.join(i))