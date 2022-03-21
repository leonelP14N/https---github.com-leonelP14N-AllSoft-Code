import random, string

tamanho=16
charts=string.ascii_letters + string.digits + '!@#$%&-'
rnd=random.SystemRandom()

print(''.join(rnd.choice(charts) for i in range(tamanho)))