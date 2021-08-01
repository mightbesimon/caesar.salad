def salad(ciphertext, guesses = 1):
	''' - salad(ciphertext, guesses = 1)
	[output]: plain texts from decipher salads
	# picks the optimal decipher salad(method) based on cipher text length
	# 	- guessSalad()  uses letter frequency guessing and is faster
	# 	                but is not accurate with around <40 letters
	#	- lookupSalad() dictionary look up, more accurate
	#	                but is slow and not great with pronouns
	# by mightbesimon(simon) :)'''


	return lookupSalad(ciphertext, guesses) if len(ciphertext) < 40 else guessSalad(ciphertext, guesses)



def guessSalad(cipherText, guesses=5):
	''' - guessSalad(cipherText, guesses = 5)
	[output]: most likely plain texts
	# guesses the most likely plaintexts
	# to a Caeser cipher cipher text
	#
	# guesses are based on sum of letter frequencies
	# default number of guesses = 5
	# 
	# by mightbesimon(simon) :)'''

	letterFreq = [
			.0817, .0149, .0278, .0425, .1270, .0223,
			.0202, .0609, .0697, .0015, .0077, .0402,
			.0241, .0675, .0751, .0193, .0009, .0599,
			.0633, .0906, .0276, .0098, .0236, .0015,
			.0197, .0007
		]

	cipherText = cipherText.lower()


	# makes texts from all 26 shifts #
	texts = [''.join(chr(((ord(ltr)-97 + shift)%26 + 97)*ltr.isalpha() + ord(ltr)*(not ltr.isalpha())) for ltr in cipherText) for shift in range(26)]

	# calculates goodness of all text shifts #
	#	- goodness is just the sum of letter frequency
	goodness = [round(sum(letterFreq[(ord(ltr) - 97)*ltr.isalpha()] for ltr in texts[idx]), 4) for idx in range(26)]


	# find most likely plain texts #
	if guesses == 1: return texts[goodness.index(max(goodness))]
	likelyTexts = [text for count, text in sorted(zip(goodness, texts), reverse = True)]
	return likelyTexts[:guesses]



def lookupSalad(cipherText, guesses=1):
	''' - lookupSalad(cipherText, guesses = 1)
	[output]: most likely plain text
	# guesses the most likely plaintexts
	# to a Caeser cipher cipher text
	#
	# guesses are based on number of actual words
	# from a dictionary in a sentence
	# default number of guesses = 1
	# 
	# by mightbesimon(simon) :)'''

	# get wordlist #
	with open('wordlist.txt', 'r') as wordlistFile: wordlist = wordlistFile.read().split('\n')
	cipherText = cipherText.lower()		#change to lower case for easier comparison


	# makes texts from all 26 shifts #
	texts = list(''.join(chr(((ord(ltr)-97 + shift)%26 + 97)*ltr.isalpha() + ord(ltr)*(not ltr.isalpha())) for ltr in cipherText) for shift in range(26))

	# num of actual words in each shift #
	wordCount = list(sum(word in wordlist for word in line) for line in list(text.split(' ') for text in texts))
	if not any(wordCount): return guessSalad(cipherText, guesses)	# found no words


	# find most likely plain texts #
	if guesses == 1: return texts[wordCount.index(max(wordCount))]
	plainTexts = [text for count, text in sorted(zip(wordCount, texts), reverse=True)]
	return plainTexts[:guesses]

