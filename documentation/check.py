# %%

import pandas as pd
import json

# %%
with open('/Users/au324704/chicago_corpus/documentation/old_data/CHICAGO_CORPUS_DATA.json', 'r') as f:
    data = json.load(f)

data.keys()
df = pd.DataFrame.from_dict(data)
df.head()

# %%
new_df = pd.read_excel('/Users/au324704/Desktop/CHICAGO_MEASURES_JUNE24.xlsx')

# %%
list(df.columns)

# %%
[x for x in new_df.columns if x not in df.columns]

# %%

cols_only_in_df_new = [
 'BOOK_ID', 
 'HURST_SYUZHET',
 'FREQ_OF',
 'FREQ_THAT',
 'PRIZES',
 'GENRE_PR',
 'CANON',
 'APPENT_SYUZHET',
 'SPACY_ADJ',
 'SPACY_NOUN',
 'SPACY_VERB',
 'SPACY_SBJ',
 'SPACY_AUX',
 'SPACY_RELATIVE',
 'SPACY_PERS_PRON',
 'SPACY_FUNCTION_WORDS']

print(len(df.columns))
print(len(new_df.columns))



# %%
chi = new_df[cols_only_in_df_new].copy()
print(len(chi.columns))

# %%
merged = pd.merge(df, chi, on='BOOK_ID')
print(len(merged.columns))
# %%
merged.head()
# %%
len(merged)
[x for x in merged.columns if x.startswith('SPACY')]


# %%
list(df.columns)
# %%
merged = merged.drop_duplicates(subset='BOOK_ID')
len(merged)
# %%
with open('/Users/au324704/chicago_corpus/data/CHICAGO_CORPUS_DATASET.json', 'w') as f:
    json.dump(merged.to_dict(), f)
# %%
# %%
with open('/Users/au324704/chicago_corpus/data/CHICAGO_CORPUS_DATASET.json', 'r') as f:
    data = json.load(f)
    
df = pd.DataFrame.from_dict(data)
df.head()
# %%
[x for x in df.columns if x.startswith('SPACY')]
# %%
