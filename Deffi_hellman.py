# Diffle-Hellman algorithm
def generatePublickey(p,g, privateKey):
    publicKey = pow(g, privateKey, p)
    return publicKey

def takeUserInputs():
    while True:
        try:
            p = int(input("Enter the Value of P : "))
            g = int(input("Enter the Value of G : "))
            privateKey = int(input("Enter Your own Private Key (Keep It very secret) : "))
            return (p,g,privateKey)
        except Exception :
            print("Error while Taking inputs. TRY AGAIN!")
            
def getSharedKey(publicKey, myPrivatekey, p):
    sharedKey = pow(publicKey, myPrivatekey, p)
    return sharedKey
    
p1, g1, privateKey1= takeUserInputs()
publickey1 = generatePublickey(p1, g1, privateKey1)
print(f"Public Key 1 :  {publickey1}")

p2, g2, privateKey2= takeUserInputs()
publickey2 = generatePublickey(p2, g2, privateKey2)
print(f"Public Key 2 :  {publickey2}")

secretKey1 = getSharedKey(publickey1, privateKey2,p1)
print(f"Shared Key 1 is : {secretKey1}")

secretKey2 = getSharedKey(publickey2, privateKey1,p2)
print(f"Shared Key 2 is : {secretKey2}")
