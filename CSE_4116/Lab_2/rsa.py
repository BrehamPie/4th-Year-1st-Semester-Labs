import math
#p is 150 digit
p = 656692050181897513638241554199181923922955921760928836766304161790553989228223793461834703506872747071705167995972707253940099469869516422893633357693
#q is 150 digit
q = 533791764536500962982816454877600313815808544134584704665367971790938714376754987723404131641943766815146845004667377003395107827504566198008424339207
#N is 300 digit.
N = p*q

phi_n = (p-1)*(q-1)
# finding e such that 1<e<phi_n and gcd(e,phi_n)=1
for i in range(2,phi_n):
    if math.gcd(i,phi_n)==1:
        e = i
        break 
plainText = 101
#message encryption
encryptedText = pow(plainText,e,N)
#finding d such e*d = 1 mod N
d = pow(e,-1,phi_n)
#message decryption
decryptedText = pow(encryptedText,d,N)

print("    Plain Text:"+str(plainText))
print("Encrypted Text:"+str(encryptedText))
print("Decrypted Text:"+str(decryptedText))