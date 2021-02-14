
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encrypt(plain_text, key):

	plain_text = plain_text.upper()
	key = key.upper()
	
	cipher_text = ''
	key_index = 0
	
	for character in plain_text:
		index = (ALPHABET.find(character)+(ALPHABET.find(key[key_index])))%len(ALPHABET)
		cipher_text = cipher_text + ALPHABET[index]
		
		key_index = key_index + 1

		if key_index == len(key):
			key_index = 0
			
	return cipher_text

def vigenere_decrypt(cipher_text, key):

	cipher_text = cipher_text.upper()
	key = key.upper()
	
	plain_text = ''
	key_index = 0
	
	for character in cipher_text:
		index = (ALPHABET.find(character)-(ALPHABET.find(key[key_index])))%len(ALPHABET)
		plain_text = plain_text + ALPHABET[index]
		
		key_index = key_index + 1
		
		if key_index == len(key):
			key_index = 0
			
	return plain_text
	
key = str(input("Eneter the key for encryption : "))
# key = "12345678123456781234567812345678123456781234567812345678"
plain_text = 'SUPER SECRET MESSAGE'
encrypted = vigenere_encrypt(plain_text,key)
print('Encrypted message: %s' % encrypted)
key2 = str(input("Eneter the key for decryption : "))
decrypted = vigenere_decrypt(encrypted,key2)
print('Decrypted mesage: %s' % decrypted)

