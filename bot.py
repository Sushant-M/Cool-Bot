import spacy
import random

nlp = spacy.load('en')

GREETING_KEYWORDS = ('hello', 'hi', 'hey','sup','what up');
GREETING_RESPONSE = ['sup bro', 'hey', 'how are you?','welcome from cool bot!']

priceMapper = {'bangalore':1000 , 'pune' : 2000 , 'delhi' : 1500, 'chennai':1300}

#Check if the person greeted us and just reply with another greeting
def checkForGreeting(sentence):
	words = sentence.split()
	for word in words:
		if word.lower() in GREETING_KEYWORDS:
			return random.choice(GREETING_RESPONSE)

#Check if the user entered a location, if they did it's probably to enquire about the prices in that region
def checkLocationName(sentence):
	LOCATIONS = ('delhi' , 'bangalore', 'pune', 'chennai')
	words = sentence.split()
	for word in words:
		if word.lower() in LOCATIONS:
			return word.lower()

#Check if the price keyword exists in the user's input
def checkPrice(sentence):
	PRICE_KEYWORDS = ('price','prices','cost')
	words = sentence.split()
	for word in words:
		if word.lower() in PRICE_KEYWORDS:
			return True
	return False

#Check for verbs in the sentence, return a list of 'em
def checkVerbs(sentence):
	verbs=[]
	doc = nlp(sentence.decode('utf-8'))
	for token in doc:
		if token.pos == 97: #the int code for verb
			verbs.append(token)
	return verbs

#Check for nouns in a sentence, return a list of 'em
def checkNouns(sentence):
	nouns = []
	doc = nlp(sentence.decode('utf-8'))
	for token in doc:
		if token.pos == 89: #the int code for noun
			nouns.append(token)
	return nouns

def checkPropernouns(sentence):
	propernoun = []
	doc = nlp(sentence.decode('utf-8'))
	for token in doc:
		if token.pos == 93: #the int code for pronoun
			propernoun.append(token)
	return propernoun

def response(sentence):
	#main loop
	first_resp = checkForGreeting(sentence)
	if(first_resp):
		print first_resp
	if(checkPrice(sentence) and checkLocationName(sentence)):
		#create a response to some generic questions the bot might
		#encounter, such as 'Tell me prices in Bangalore'
		location = checkLocationName(sentence)
		price = priceMapper[location]
		print 'The prices in ', location , ' are ', price , ' per *whatever metric you guys have*'

if __name__ == "__main__":
	text = raw_input()
	response(text)