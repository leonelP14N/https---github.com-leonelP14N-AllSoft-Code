import hashlib

strg=input('Digite algum texto')

result = hashlib.md5(strg.encode('UTF-8'))
result1 = hashlib.sha1(strg.encode('UTF-8'))
result2 = hashlib.sha256(strg.encode('UTF-8'))
result3 = hashlib.sha512(strg.encode('UTF-8'))

print('O hash em md5:', result)
print('O hash em sha1:', result1)
print('O hash em sha256:', result2)
print('O hash em sha512:', result3)

