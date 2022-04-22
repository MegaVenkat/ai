from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
text = '''
Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems. Specific applications of AI include expert systems, natural language processing, speech recognition and machine vision.
'''
print("\nOriginal string:")
print(text)
token_text = sent_tokenize(text)
print("\nSentence-tokenized copy in a list:")
print(token_text)
print("\nRead the list:")
for s in token_text:
     print(s)
