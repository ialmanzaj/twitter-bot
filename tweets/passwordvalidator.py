# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import enchant
import re
import string
import random

class PasswordStrengthEvaluator(object):
	def __init__(self, password):
		self._password = password

	def evaluator(self):
		def checkEnglishWord(password):
			mo = re.search(r'([A-Z]+|[a-z]+)', password)
			if mo:
				english = enchant.Dict("en_US")
				if english.check(mo.group(1)):
					return {'english': True,'word':mo.group(1)}
				else:
					return {'english': False,'word':None}

		def isDigit(letter):
			mo = re.match(r'(\d)', letter)
			if mo:
				return True
			else:
				return False

		def isAlphabet(letter):
			mo = re.match(r'([A-Z]|[a-z])', letter)
			if mo:
				return True
			else: 
				return False
		
		def isWhitespace(letter):
			mo = re.match(r'(\s|\t|\n)', letter)
			if mo:
				return True
			else: 
				return False

		def isOther(letter):
			mo = re.match(
				r'^/by_tag/(?P<tag>\w+)/(?P<filename>(\w|[.,!#%{}()@])+)$',
				letter, 
				re.UNICODE)
			if mo:
				return True
			else:
				return False

		def typeCharacter(letter):
			if isAlphabet(letter):
				return'alphabet'
		
			if isDigit(letter):
				return 'digits'

			if isWhitespace(letter):
				return 'whitespace'

			if isOther(letter):
				return 'other'

		def typesOfCharacters(password):
			types = []
			for letter in password:
				type_character = typeCharacter(letter)
				if type_character:
					types.append(type_character)

			return types

		def timesOfTypesOfCharacter(types_characters):
			types_characters_times = []
			for type_character in list(set(types_characters)):
				types_characters_times.append(types_characters.count(type_character))

			return types_characters_times

		#implementation
		english_validation = checkEnglishWord(self._password)
		password_replace = ''

		if english_validation['english']:
			random_word = ''
			for i in range(len(self._password)):
				random_word += random.choice(string.ascii_lowercase)

			password_replace = self._password.replace(
				english_validation['word'],
				random_word
			)

		types_characters = typesOfCharacters(self._password)

		result = " old-password: %s, new password: %s, typesOfCharacters: %s" %(
			self._password,
			password_replace,
			types_characters)

		return result


				

		


			

