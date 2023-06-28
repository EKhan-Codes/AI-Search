import requests
from bs4 import BeautifulSoup
import nltk

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize, sent_tokenize

url = 'https://www.zameen.com/blog/grand-open-house-gulberg-city-centre-june-2023.html'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True) 

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'nav',
    'style',
    'footer',
    'header_navMenu_wrap',
    'div',
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)





# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(output)
   
# Creating a frequency table to keep the 
# score of each word
   
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1
   
# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(output)
sentenceValue = dict()
   
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq
   
   
   
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
   
# Average value of a sentence from the original text
   
average = int(sumValues / len(sentenceValue))
   
# Storing sentences into our summary.
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
print(summary)




