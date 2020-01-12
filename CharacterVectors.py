from urllib import request
from sklearn.feature_extraction.text import CountVectorizer
# list of text documents
text = open("Users//Desktop/browncorpus.txt", "r")
s = text.read()
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocabulary detils
vectorizer.fit(text)
# summarize the vector vocabulary
print(vectorizer.vocabulary_)
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(type(vector))
print(vector.toarray())
