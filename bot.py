import spacy

nlp = spacy.load('en')

def checkForGreeting(sentence):
	GREETING_KEYWORDS = ('hello', 'hi', 'hey','sup','what up');
	GREETING_RESPONSE = ['sup bro', 'hey', 'how are you?','welcome from cool bot!']
	for word in sentence.words:
		if word.lower() in GREETING_KEYWORDS:
			return random.choice(GREETING_RESPONSE)

def checkVerbs(sentence):
	verbs=[]
	doc = nlp(sentence.decode('utf-8'))
	for token in doc:
		if token.pos == 97: #the int code for verb
			verbs.append(token)
	return verbs

def checkNouns(sentence):
	nouns = []
	doc = nlp(sentence.decode('utf-8'))
	for token in doc:
		if token.pos == 89:
			nouns.append(token)
	return nouns

if __name__ == "__main__":
	text = raw_input()
	print_nouns = checkNouns(text)
	print_verbs = checkVerbs(text)
	print print_nouns
	print print_verbs


