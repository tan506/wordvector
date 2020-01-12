#First open the file location of the text document for proessing the textual schametics
#you are trying to derive morpheme embeddings using CNN'schametics
#decide on the appropriate CNN models
with open("browncorpus.txt") as model_document:
    try:
        while True:
            latin = model_document.next().strip()
            gloss = model_document.next().strip()
            trans = model_document.next().strip()
            #processing the embedded morphing
            process(latin, gloss, trans)
            model_document.next()    # skip blank line
    except StopIteration:
        # reached end of file
        pass
from itertools import chain
def chunk(s):
    return chain(*(c.split("-") for c in s.split()))
#processing the CNN's using Natural Language Processing
#this leaves the chunks of morpheme and predicts the next wordings
def process(latin, gloss, trans):
    chunks = zip(chunk(latin), chunk(gloss))

