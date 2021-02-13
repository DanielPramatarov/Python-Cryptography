from Crypto.Cipher import DES
import binascii

def append_space_padding(str, blocksize=64):
  pad_len = blocksize - (len(str) % blocksize)  
  padding = 'a'*pad_len
  return str + padding

def remove_space_padding(str, blocksize=64):
    
    pad_len = 0 
	
    for char in str[::-1]: 
        if char == 'a':
            pad_len += 1
        else:
            break

    str = str[:-pad_len]
   
    return str
	
def encrypt(plaintext, key):
	des = DES.new(key, DES.MODE_ECB)
	return des.encrypt(plaintext)

def decrypt(ciphertext, key):
	des = DES.new(key, DES.MODE_ECB)
	return des.decrypt(ciphertext).decode('UTF-8')


key = "SECRETKY"
plaintext = str(input("Text to be encrypt :"))
plaintext = append_space_padding(plaintext)
# print(plaintext)

ciphertext = encrypt(plaintext,key)
# print(ciphertext)
print(binascii.hexlify(bytearray(ciphertext)).decode("UTF-8"))

decrypted = decrypt(ciphertext,key)
decrypted = remove_space_padding(decrypted)
print("Decrypted message:" ,decrypted)

