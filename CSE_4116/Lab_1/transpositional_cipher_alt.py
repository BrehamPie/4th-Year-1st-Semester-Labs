plainData = input("Enter Your Text:")
row = int(input("Enter Row Number:"))
col = (len(plainData)+row-1)//row

plainMatrix = []
cipherMatrix = []
# Making Plain Matrix From Plain Text.
for i in range(0, len(plainData), col):
    plainMatrix.append(plainData[i:i+col])
# Making Transpose Matrix.
for j in range(col):
    new_row = []
    for i in range(row):
        if len(plainMatrix[i]) <= j:
            s = ' '
        else:
            s = plainMatrix[i][j]
        if(s.islower()):
            s = s.upper()
        elif(s.isupper()):
            s = s.lower()
        new_row.append(s)
    cipherMatrix.append(''.join(new_row))

# Printing Outputs.
print("\nPlain Text:\n")
print(plainData)
print("\nPlain Text in Matrix Form:\n")
for x in plainMatrix:
    print(x)
print("\n\n")
print("Cipher Text in Matrix after Transposition:\n")
encryptedData = ''
for x in cipherMatrix:
    print(x)
    encryptedData += x
print("\n\nCipher Text:\n")
print(encryptedData)
