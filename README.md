# ARTICLE TRANSLATE AUTOMATION

## INTRODUCTION
1. You have to **download** given python libraries. Open your terminal and download these libraries using `pip`.
```bash
pip install nltk
pip install googletrans
```
2. Download both **translate.py** and **article.txt** in one specific folder. 
3. Copy and paste your translate text to **article.txt**
4. Open your terminal, go to your folder and write the code below:
```bash
python3 -i translate.py
```
5. You will get **anki_sentences.txt** This is Ankidroid compatable **csv** file. You can also open it in any suitable text editor or Excel.

> NOTE: You can change module languages:
 ```python
	# this is your source language and you can change it to any language like 'ru' , 'it' , 'de' , 'gr'
	source_lang = 'en' 
	# this is your destination language and you can change it to any language like 'ru' , 'it' , 'de' , 'gr'
	dest_lang = 'tr'
```
