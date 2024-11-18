from sympy import mod_inverse

def GCD(a,b):
	while b:
		a,b = b%a
	return a

def generateKeys():
	p = int(input("Enter the value of P : "))
	q = int(input("Enter the value of q : "))
	
	n = p*q

	phiN = (p-1)*(q-1)
	
	# GCD validation for choosing a proper value of e
	while True :
		e = int(input("Enter the value of e : "))
		gcd = GCD(e,phiN)
		
		if gcd == 1:
			print("Value of e as ", e," has been taken.")
			break
		else:
			print("Value of e is not co-prime to n.\n Please Enter other value!")
	d = mod_inverse(e,phiN)
	print("Keys are generated!")
	return (e,n),(d,n)

def encrypt(message, publicKey):
	e , n = publicKey
	encryptedMessage = [pow(chr(c), e,n) for c in message]
	return encryptedMessage 


def decrypt(encryptedMessage, privateKey):
	d , n = privateKey
	decryptedMessage = " ".join([ord(pow(i,d,n)) for i in encryptedMessage])
	return decryptedMessage 			

# main program 

print("Let's Generate the keys First!")

publicKey , privateKey = generateKeys()  # tuple unpacking

message = input("Enter the message to encrypt : ")

encryptedM = encrypt(message,publicKey)
print("Encrypted message is : ", encryptedM)

decryptedM = decrypt(encryptedM, privateKey)
print(Decrypted message is : ", decryptedM)

print("Thank You!")

