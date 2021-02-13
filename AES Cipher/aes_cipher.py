from Crypto.Cipher import AES
from Crypto import Random
import binascii

def append_space_padding(str, blocksize=128):
	pad_len = blocksize - (len(str) % blocksize)  
	padding = 'a'*pad_len
	return str + padding

def remove_space_padding(str, blocksize=128):
    
    pad_len = 0 
	
    for char in str[::-1]: 
        if char == 'a':
            pad_len += 1
        else:
            break

    str = str[:-pad_len]
   
    return str
	
def encrypt(plaintext, key):
	des = AES.new(key, AES.MODE_ECB)
	return des.encrypt(plaintext)

def decrypt(ciphertext, key):
	des = AES.new(key, AES.MODE_ECB)
	return des.decrypt(ciphertext).decode('UTF-8')


#key is 128 bits = 16 bytes
choise = int(input("Enter your choice : "  ))
print("1 -> For 16 bytes long key")
print("2 -> For 24 bytes long key")
print("3 -> For 32 bytes long key\n")
if choise == 1:
    key = Random.new().read(16)
    print(key)
    plaintext = "This is the secret message "
    plaintext = append_space_padding(plaintext)
    ciphertext = encrypt(plaintext,key)
    print(binascii.hexlify(bytearray(ciphertext)).decode("UTF-8"))

    decrypted = decrypt(ciphertext,key)
    decrypted = remove_space_padding(decrypted)
    print("Decrypted message:" ,decrypted)
        
elif choise == 2:
    key = Random.new().read(24)
    plaintext = "This is the secret message "
    plaintext = append_space_padding(plaintext)
    ciphertext = encrypt(plaintext,key)
    print(binascii.hexlify(bytearray(ciphertext)).decode("UTF-8"))

    decrypted = decrypt(ciphertext,key)
    decrypted = remove_space_padding(decrypted)
    print("Decrypted message:" ,decrypted)
elif choise == 3:
    key = Random.new().read(32)
    print(f"Your key to decrypt the message is {key} "   ) 
    plaintext = "This is the secret message "
    plaintext = append_space_padding(plaintext)
    ciphertext = encrypt(plaintext,key)
    print(binascii.hexlify(bytearray(ciphertext)).decode("UTF-8"))

    decrypted = decrypt(ciphertext,key)
    decrypted = remove_space_padding(decrypted)
    print("Decrypted message:" ,decrypted)

