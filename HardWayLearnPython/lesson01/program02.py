WORD_URL="http://learncodethehardway.org/words.txt"
WORDS=[]
import random
from urllib.request import urlopen
import sys

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = 'utf-8'))
print(WORDS)