import spacy
from spacy.tokens import DocBin
from spacy.training import Example



def load_conll(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    docs = []
    words, entities = [], []

    for line in lines:
        line = line.strip()
        if not line:
            if words:
                docs.append((words, entities))
                words, entities = [], []
            continue

        parts = line.split()
        word, label = parts[0], parts[-1]
        words.append(word)
        entities.append(label)

    return docs

def create_docbin(data, nlp):
    doc_bin = DocBin()
    for words, labels in data:
        doc = nlp.make_doc(" ".join(words))
        ents = []
        start = 0
        for word, label in zip(words, labels):
            end = start + len(word)
            if label.startswith("B-"):
                ent_start = start
                ent_label = label[2:]
            elif label.startswith("I-") and 'ent_start' in locals():
                pass  # continue inside entity
            elif label == "O" and 'ent_start' in locals():
                ents.append((ent_start, prev_end, ent_label))
                del ent_start, ent_label

            prev_end = end
            start = end + 1  # add space

        if 'ent_start' in locals():
            ents.append((ent_start, prev_end, ent_label))
            del ent_start, ent_label

        doc.ents = [doc.char_span(start, end, label=label) for start, end, label in ents if doc.char_span(start, end, label=label)]
        doc_bin.add(doc)
    return doc_bin

nlp = spacy.blank("id")  

data = load_conll("./dataset/Ner.conll")
doc_bin = create_docbin(data, nlp)
doc_bin.to_disk("./model/train.spacy")