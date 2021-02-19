                    # INSTRUCTIONS
###########################################################To Operate type python key-generator.py in your terminal and give the program up to 1 minute to process your request.  When a key has been generated and verified it will appear in your terminal.
###########################################################
import random

class Key:

	def __init__(self, key=''):
		if key == '':
			self.key= self.generate_key()
		else:
			self.key = key.lower()

	def validate_key(self):
		count = 0
		verify_digit = self.key[0]
		verify_digit_count = 0
		chunks = self.key.split('-')
		for chunk in chunks:
			if len(chunk) != 4:
				return False
			for char in chunk:
				if char == verify_digit:
					verify_digit_count += 1
				count += ord(char)
		if count == 1772 and verify_digit_count == 5:
			return True
		return False

	def generate_key(self):
		key = ''
		chunk = ''
		key_chars = '0123456789abcdefghijklmnopqrstuvwxyz'
		while True:
			while len(key) < 25:
				char = random.choice(key_chars)
				key += char
				chunk += char
				if len(chunk) == 4:
					key += '-'
					chunk = ''
			key = key[:-1]
			if Key(key).validate_key():
				return key
			else:
				key = ''

	def __str__(self):
		valid = 'False aka Invalid key'
		if self.validate_key():
			valid = 'True aka Valid Key'
		return self.key.upper() + ':' + valid

key = Key('aaaa-bbbb-cccc-dddd-1111')
print(Key())