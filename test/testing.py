import spacy
nlp = spacy.load("./output/model-best")

doc = nlp("john dan mary pergi ke pasar untuk membeli buah-buahan segar")
for ent in doc.ents:
    print(ent.text, ent.label_)