import nltk 

with open('article.txt','r') as rfile:
	data = rfile.readlines()
	text = ''.join(data).strip().replace('\n\n','. ')

# ANCHOR: SENTENCE ANALYZER
	sentences = nltk.sent_tokenize(text)
	counter = 0
	sent_list =[]
	for i in sentences:
		counter +=1
		print(counter,' :\t',i )
		sent_list.append(i)
	with open('sentences.txt','w') as wfile:
		for s in sent_list:
			print(s,file = wfile)
			
			

		 
			
# ANCHOR: COUNTER + GOOGLETRANS MODULE 

def GoogleTrans(text, source_lang, dest_lang):
	from googletrans import Translator
	from time import sleep
	sleep(1)
	cursor = Translator()
	sentence = cursor.translate(text, src=source_lang, dest = dest_lang)
	original_text , translate = sentence.origin, sentence.text
	#print(original_text, ':\n',translate)
	sentlist = [original_text,translate]
	return sentlist  

anki_list = []
for i in sent_list:
	counter +=1
	#ceviri_kaynak_dili
	source_lang = 'en'
	#ceviri_hedef dili
	dest_lang = 'tr'
	trans_sent = GoogleTrans(i, source_lang,dest_lang)
	anki_list.append(trans_sent)
	print(counter,':\n',trans_sent[0] ,'\n',trans_sent[1],'\n','-'*50)

with open('anki_sentences.csv','w') as csw:
	from csv import writer
	cursor = writer(csw)
	for row in anki_list:
		cursor.writerows([row])
