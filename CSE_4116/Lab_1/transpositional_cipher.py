row = int(input("Enter Row Number:"))
col = int(input("Enter Column Number:"))
print("Enter Your Text in Matrix Format")
actualData=[]
cipherData=[]
data = []
for i in range(row):
    text = input()
    if len(text)!=col:
        print("Please Maintain Correct Data Format.")
        exit()
    actualData.append(text)
for j in range(col):
    new_row=[]
    for i in range(row):
        s = actualData[i][j]
        if(s.islower()):
            s = s.upper()
        elif(s.isupper()):
            s = s.lower()
        new_row.append(s)
    cipherData.append(''.join(new_row))
print("\nPlain Text in Matrix Form:\n")
for x in actualData:
    print(x)
print("")
print("Cipher Text after Transposition:\n")
for x in cipherData:
    print(x)
