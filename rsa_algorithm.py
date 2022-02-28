import random as rd

'''
p = first prime number
q = second prime number
n = p * q
phi = (p - 1) * (q - 1)
e = encryption
d = decryption
'''

# Find prime numbers
def primeFinder ():
    testNumber = rd.randrange(50, 150)
    for numberIndex in range (2, testNumber):
        if testNumber % numberIndex == 0:
            return primeFinder()
        return testNumber


# Euclidean Algorithm - to find the greatest common divider of two numbers
# a = bk + r
# a and b are the numbers we’re working with
# k is a constant value
# r is the remainder
def greatestCommonDivider (a, b):
    if b == 0:
        return a
    return greatestCommonDivider(b, a%b)

# Generate public and private key
def generateKeys (p, q):

    # Calculating n
    n = p * q

    # Using Euler's Totient function. Phi of the totient of n
    phi = (p-1) * (q-1)


    #calculate public key
    publicKeys = []
    for numberIndexPublic in range (2, phi):
        if greatestCommonDivider(numberIndexPublic, phi) == 1 and greatestCommonDivider(numberIndexPublic, n) == 1:
            publicKeys.append(numberIndexPublic)
        if len(publicKeys) >= 100:
            break

    e = rd.choice(publicKeys)

    #calculate private key
    privateKeys = []
    numberIndexPrivate = 2
    while len(privateKeys) < 20:
        if numberIndexPrivate * e % phi == 1:
            privateKeys.append(numberIndexPrivate)
        numberIndexPrivate += 1

    d = rd.choice(privateKeys)

    #return public and private key pairs
    return ((publicKeys), (e, n), (privateKeys), (d, n))

def encrypt (publicKey, plaintext):
    #unpack public key into its components
    key, n = publicKey

    #convert each letter in plaintext to numbers based on ythe character using a^b modulus
    ciphertext = [pow(ord(char), key, n) for char in plaintext]

    #return cipher text
    return ciphertext

def decrypt (privateKey, ciphertext):
    #unpack public key into its components
    key, n = privateKey

    #Calculate plaintext with private key using a^b modulus
    output = [str(pow(char, key, n)) for char in ciphertext]

    #Convert integers to characters
    plaintext = [chr(int(char2)) for char2 in output]

    return ''.join(plaintext)

print ("")
print ("*********************************************************************************************")
print ("**************************** RSA AlGORITHM (ENCRYPT/DECRYPT) ********************************")
print ("*********************************************************************************************")
print ("")

p = primeFinder()
q = primeFinder()

print (f'Your first randomly chosen prime number = {q}')
print (f'Your second randomly chosen prime number = {p}')
print ("")

print ("Generating your public and private key-pairs now .....")
print ("")

publicPool, public, privatePool, private = generateKeys(p,q)

print (f'Possible public keys (e):')
print (publicPool)
print ("")
print ('Possible private keys (d):')
print (privatePool)
print ("")

print (f'Your public key (e, n) = {public} ')
print (f'Your private key (d, n) = {private}')
print ("")
print ("-----------------------------------------------------------------------------------------")
print ("")

message = input("Enter a message to encrypt with your public key: ")
print ("")
encryptedMessage = encrypt(public, message)

print ("Your encrypted message is:", ''.join(map(str,encryptedMessage)))
print ("")
print ("-----------------------------------------------------------------------------------------")
print ("")
print (f'Decrypting message with private key {private} ..... ')
print ("")
print ("Your decrypted message is: ", decrypt(private,encryptedMessage))
print ("")
print ("*********************************************************************************************")
print ("********************************* RSA ALGORITHM COMPLETED ***********************************")
print ("*********************************************************************************************")












