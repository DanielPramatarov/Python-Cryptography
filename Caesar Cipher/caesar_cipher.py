
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3


def caesar_encrypt(plain_text):

	cipher_text = ''
	plain_text = plain_text.upper()
	
	for c in plain_text:
    	
	
		index = ALPHABET.find(c)
		if index < 0:
    			continue
		index = (index+KEY)%len(ALPHABET)
		cipher_text = cipher_text + ALPHABET[index]
		
	return cipher_text
	
def caesar_decrypt(cipher_text):

	
	words = cipher_text.split()
	plain_text = ''
		
	for word in words:
    		
		for c in word:
			
			index = ALPHABET.find(c)
			index = (index-KEY)%len(ALPHABET)
			plain_text = plain_text + ALPHABET[index]
		plain_text += " "
		
	return plain_text
	

message_to_be_encrypted = str(input("Enter message to be encrypted with CAESAR :"))
encrypted_message = ''

words_to_be_encrypted = message_to_be_encrypted.split(" ")
for word in words_to_be_encrypted:
    	

	encrypt_word = caesar_encrypt(word)
	encrypted_message += encrypt_word 
	encrypted_message += " "

print(f"Encrypted message : {encrypted_message}")

decrypted = caesar_decrypt(encrypted_message)
print(f"Decrypted message : {decrypted}")


