from sklearn.feature_extraction.text import TfidfVectorizer
# list of text documents
text = open("Users/Desktop//browncorpus.txt", "r")
text = text.read()
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocabulary details
vectorizer.fit(text)
# summarize the word and character vectors
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
# encode document into vector states description through transform functions
vector = vectorizer.transform([text[0]])
# summarize encoded vector
print(vector.shape)
print(vector.toarray())
