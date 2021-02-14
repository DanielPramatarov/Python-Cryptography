
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_crack(cipher_text):

	for key in range(len(ALPHABET)):
	
		plain_text = ''
		words = cipher_text.split()
		
		for word in words:
			for c in word:
				if c == '':
					continue
				index = ALPHABET.find(c)
				index = (index-key)%len(ALPHABET)
				plain_text = plain_text + ALPHABET[index]
			plain_text += " "
		print('With key %s, the result is: %s'%(key,plain_text))
	

encrypted = 'WHVW PH QRZZZZ'
caesar_crack(encrypted)

encrypted = 'WHVWPHQRZZZZ'
caesar_crack(encrypted)

