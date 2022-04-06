p = 97
q = 119

N = p*q
phi_n = (p-1)*(q-1)

e = 7

d = pow(e,-1,phi_n)

plainMessage = 535
cipherMessage = pow(plainMessage,e) % N
decryptedMessage = pow(cipherMessage,d) % N
print(plainMessage)
print(cipherMessage)
print(decryptedMessage)
print(e,d)