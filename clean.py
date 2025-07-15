import pandas as pd
import re

dataset = pd.read_json("./raw_dataset/ner_food_dataset.json")
dataset['text'] = dataset['text'].apply(lambda x: re.sub(r'[.?]', '', x.strip()))
dataset['text'] = dataset['text'].str.lower()

print(dataset.head())

dataset.to_json("./data_bersih/ner_food_dataset.json", orient='records', force_ascii=False)