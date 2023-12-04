import spacy
import pickle

nlp = spacy.load("en_core_web_sm")
sentence = "Wy do you thnk it happned"

SRC = pickle.load(open(f'weights/SRC.pkl', 'rb'))

# for tok in nlp.tokenizer(sentence):
#     if tok.text != " ":
#         print(tok.text, SRC.vocab.stoi[tok.text])

nlp.tokenizer(sentence)