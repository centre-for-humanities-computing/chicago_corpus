# Overview of measures annotated in the Chicago Corpus

# Table of Contents

**Textual measures**
1. [Stylistic](#stylistic)
2. [Syntactic](#syntactic)
4. [Readability](#readability)
5. [Sentiment Analysis-based measures](#sentiment-analysis-based-measures): [_Simple features_](#simple), [_Complex measures_](#complex)
6. [EmotionArcs](#emotionarcs)
7. [Perplexity](#perplexity)

**Quality proxies**

7. [Crowd-based](#crowd-based)
    1. [User-lists](#i-user-lists)

8. [Expert-based](#expert-based)
    1. [Lists](#lists)
    2. [Awards](#awards): 
    	[_General_](#i-general),
	[_Sci-fi_](#ii-sci-fi),
	[_Fantasy_](#iii-fantasy),
	[_Horror_](#iv-horror),
	[_Mystery_](#v-mystery)
	& [_Umbrella-categories_](#vi-umbrella-categories)

**Extra**

9. [Author gender](#gender), [Decade](#decade)

<br>

##

# Stylistic

### WORDCOUNT

Number of words in text.

### SENTENCE_LENGTH

Length of sentences in text measured in characters. 

### MSTTR-100

Mean Segmental Type-Token Ratio is a measure of lexical richness. It segments the text in segments of a given size (here 100 words, often taken as standard) and calculates the Type-Token Ratio for each segment - then takes the average of all segment ratios of the whole text.  

## TTR_VERB
The type/token ratio of only **verbs** in the text. To account for length, we only did the simple TTR of the first 60.000 tokens of each text.

## TTR_NOUN
The type/token ratio of only **nouns** in the text. To account for length, we only did the simple TTR of the first 60.000 tokens of each text.

### BZIP_TXT

Compressibility of the text-files as calculated by dividing the original bitsize of the text with the compressed bitzsize (using bzip2 compression). 
We calculated the compression ratio (original bit-size/compressed bit-size) for the first 1500 sentences of each text.

_We use the [bz2 module](https://docs.python.org/3/library/bz2.html)_
Settings: ``bz2.compress(arc.encode(),compresslevel=9)``

### BIGRAM_ENTROPY & WORD_ENTROPY
Both word and bigram entropy was calculated by means of Mark Algee-Hewitt’s github for the Stanford Literary Lab pamphlet 17. 
The code was modified to also asses entropy on the word basis (while pamphlet 17 inly includes bigram-basis). Adopted from [Algee-Hewitt's repository](https://github.com/nan-da/Entropy-for-Bigrams).

Stopwords were not removed. 
Measures the “predictability”/amount of information of words or bigrams in the text. 

##

# Syntactic
Range of tags extracted using the small spaCy model (en_core_web_sm)

### SPACY_ADJ
Adjective frequency of each text (not normalized, e.g., by wordcount)

### SPACY_NOUN
Noun frequency of each text (not normalized)

### SPACY_VERB
Verb frequency of each text (not normalized)

### SPACY_PRON
Pronoun frequency of each text (not normalized)

### SPACY_PUNCT
Punctuation-mark frequency of each text (not normalized)

### SPACY_STOPS
Stopword frequency of each text (not normalized)

### SPACY_SBJ
Nominal subject frequency of each text (not normalized)

### SPACY_PASSIVE
Passive auxiliary frequency of each text (not normalized)

### SPACY_AUX
Auxiliary frequency of each text (not normalized)

### SPACY_RELATIVE
Relative clause modifier frequency of each text (not normalized)

### SPACY_NEGATION
Negation modifier frequency of each text (not normalized)

### VERB_NOUN_RATIO
Simply the number of verbs divided by the number of nouns in a text (not normalized)

### ADV_VERB_RATIO
Simply the number of averbs divided by the number of verbs in a text (not normalized)

### PERC_ACTIVE_VERBS
The number of active verbs minus the number of passive verbs in a text (not normalized)

### PASSIVE_ACTIVE_RATIO
The number of passive verbs divided by the number of active verbs in a text (not normalized)

### NOMINAL_VERB_RATIO
The number of adjective + the number of nouns divided by the number of verbs in a text (not normalized) (see our recent [paper](https://aclanthology.org/2024.latechclfl-1.16.pdf) for more on this metric for complexity estimation)


# Readability

### READABILITY_FLESCH_EASE
A measure of readability based on the average sentence length (ASL), and the average syllables per word (word length)(ASW), with a higher weight on the word length (Crossley et al., 2011). It should be noted that the weight on word lengths is higher in the Flesch Reading Ease score compared to the Flesch-Kincaid Grade Level. It returns a readability score between 0 and 100, where higher scores are better (Hartley, 2016). The formula is:

Flesch Reading Ease =206.835 - (1.015 * sentence length) + (84.6 * word length)
				
**Why it was selected**
It’s one of the most common scores and has in several publications been argued to be the best measure compared to other readability scores (see Hartley, 2016) 
It does not return a US grade (compared to all other scores), which might be a bit difficult to interpret, but instead returns a score

**What to be aware of** (also described in Hartley, 2016)
The score might be outdated and has several issues, which also apply to other readability scores (Hartley, 2016):
Many syllables does not mean that a word is more difficult to understand
The meaning of words is not taken into account
There are individual differences between readers


### READABILITY_FLESCH_GRADE
A revised version of the Flesch Reading Ease score. Like the former, it is based on the average sentence length (ASL), and the number of syllables per word (ASW). It also weighs word length more than sentence length, but the weight is smaller compared to that in the Flesch Reading Ease Score. It returns a US grade level (Crossley et al., 2011). The formula is:

Flesch Kincaid Grade Level =(0.39 * sentence length) + (11.8 * word length) -15.59 

**Why it was selected**
It’s also one of the most common and traditional scores to assess readability

**What to be aware of** 
See Flesch Reading Ease above
The score was initially developed for document for the US Navy, so it might be questioned how well it applies to literature 


### READABILITY_SMOG
A readability score introduced by McLaughlin. It measures readability based on the average sentence length and number of words with more than 3 syllables (number of polysyllables), and returns a US grade. However, it does this by defining all words with 3 or more syllables as polysyllables, rather than using word length as a continuous measure. It was developed as an easier (and more accurate) alternative to the Gunning Fog Index, and is based on the McCall-Crabbs Standard Test Lessons in Reading (Zhou et al., 2017). The formula is: 

SMOG Index = 1.0430 * number of polysyllables * 30number of sentences+ 3.1291

**Why it was selected**
The main reason for selecting this measure was as a (better) alternative to the Gunning Fog Index, and as an alternative to the Flesch scores 
McCall-Crabbs Standard Test Lessons in Reading contain non-fiction but also fiction texts, which might be relevant for the texts we are looking at

**What to be aware of**
The SMOG Index is widely used for health documents, so it is unclear how accurate this score is when it is applied to literature
The McCall-Crabbs Standard Test Lessons in Reading have been revised multiple times, which means that the formula itself might also be inaccurate (Zhou et al., 2017)


### READABILTY_ARI
A readability score based on the average sentence length and number of characters per words (word length), and returns a US grade. However, the word length is not defined by the number of syllables, but by the number of characters in the word. It was developed to test readability of documents from the US Air Force, and was defined using 24 books and their associated grade levels (Zhou et al., 2017). The formula is: 

ARI = 4.71  characterswords + 0.5 wordssentences -21.43

**Why it was selected**
It was mostly selected as it uses an alternative measure of word length, compared to the Flesch scores and the SMOG Index

**What to be aware of** 
Since it was developed for rather technical documents it may be debated how well it applies to literature


### READABILTY_DALE_CHALL_NEW
A 1995 revision of the Dale-Chall readability score. It is based on the average sentence length (ASL) and the percentage of "difficult words" (PDW) which were defined as words which do not appear on a list of words which 80 percent of fifth-graders would know, contained in [the Dale-Chall word-list](https://countwordsworth.com/download/DaleChallEasyWordList.txt).

The Dale-Chall Readability Score also returns a US grade, but is different from all other scores, as it does not determine difficulty of words based on their length, but based on a predefined list. The raw score is adjusted, by adding 3.6365, if the number of difficult words (all words not on the list of familiar words) is above 5%. The formula to compute the raw score is as follows: 

New Dale Chall Readability Score = 0.1579 (difficult wordswords*100) + 0.0496 (wordssentences)

**Why it was selected**
This score was mainly selected as it addresses an issue of all other scores, namely that long words are not necessarily difficult to understand (e.g. interesting is a long word, but may be familiar to many and thus easy to read)

**What to be aware of**
The list of familiar words may not apply to all students and genres of text
Since the list of familiar words is based on 5th grade students, this index may be most relevant in the given age group

##

# Sentiment Analysis-based measures

the sentence-based sentiment arcs of the novels, using the [nltk implementation of VADER](https://www.nltk.org/_modules/nltk/sentiment/vader.html), arguably one of the most widespread dictionary-based methods. We provide the full version of the arcs and their coarser-grain representation in twenty segments, as well as _simpler_ and more _complex_ features of the sentiment arcs of novels.

## Simple
These are based on simple scores of the VADER sentiment annotation for valence.

### MEAN_SENT
Mean sentiment of all sentences in text

### STD_SENT
SD of sentiment in text (sentence-based)

### END_SENT
Mean sentiment of the last 10% of each text

### BEGINNING_SENT
Mean sentiment of the first 10% of each text

### DIFFERENCE_ENDING_TO_MEAN
Difference in mean sentiment between the main chunk of the text and the last 10% of the text

### ARC_SEGMENTS_MEANS
List of sentiment valence means of each segment when splitting texts into 20 segments

## 

## Complex

### BZIP_NEW

Compressibility of the sentiment-arcs as calculated by dividing the original bitsize of the arcs with the compressed bitzsize (using bzip2 compression).

_We use the [bz2 module](https://docs.python.org/3/library/bz2.html)_
Settings: ``bz2.compress(text.encode(),compresslevel=9)``

### HURST

Hurst exponent of sentiment arcs, using Adaptive Filtering for detrending arcs.
Details of the method are to be found in [this 2021 paper](https://doi.org/10.1093/llc/fqz092) and in a [blogpost](https://centre-for-humanities-computing.github.io/fabula-net/blog/intro).

### APPENT

Approximate Entropy of sentiment arcs calculated per 2 sentences. 
Sentiment arcs were exctracted with the Vader-lexicon.

Approximate entropy is a technique used to quantify the amount of regularity and the unpredictability of fluctuations over time-series data.

_We compute ApEn with [Neurokit2](https://neuropsychology.github.io/NeuroKit/functions/complexity.html#entropy)_
Settings : ``app_ent = nk.entropy_approximate(sentarc, dimension=2, tolerance='sd')``

##

# EmotionArcs
Emotion arcs are available for the full corpus, which were extracted by a method combining NRC's emotion lexicon and word embeddings. The full dataset of arcs is available in our repository [EmoArc](https://github.com/yuri-bizzoni/EmoArc).

##

# Perplexity

Perplexity as a measure can for a well-trained model, be used to approximate how surprising or complex a text can be for humans. [Our 2024 paper](https://aclanthology.org/2024.latechclfl-1.16.pdf) details the procedure for extracting perplexity scores and outlines the possible applications of this measure for literary texts.

### SELF_MODEL_PPL
The perplexity as mesured via the self-trained model (for details, see [paper](https://aclanthology.org/2024.latechclfl-1.16.pdf))

### GPT2_PPL
The perplexity as mesured via the small GPT2 model (for details, see [paper](https://aclanthology.org/2024.latechclfl-1.16.pdf))

### GPT2-XL_PPL
The perplexity as mesured via the large GPT2 model (for details, see [paper](https://aclanthology.org/2024.latechclfl-1.16.pdf))



##

# Quality_proxies

The quality metrics that we have collected belong to two main types: **crowd-based**, representing the result of many unfiltered readers (scores, counts), and, on the other hand, **expert-based**, drawn from prestigious proxies curated by experts, often institutionally affiliated (lists, series, etc.). It should be noted that this distnction is heuristic above all else, as various metrics, such as translation counts, are both subject to expert choice and the taste judgements of a larger readership.

##

## Crowd-based
These are all title-based (except for WIKI page rank)

### LIBRARIES
“Libraries” corresponds to the number of library holdings as listed in WorldCat. 


### RATING_COUNT
Number of ratings for title on Goodreads. Numbers retrieved in December 2022.

### AVG_RATING
Average rating of title on Goodreads. Numbers retrieved in December 2022.

### AUDIBLE_AVG_RATING
Average rating of title on Audible.
From a [large audible dataset](https://github.com/elipickh/Audible_full_scraper)

663 in Chicago

### AUDIBLE_RATING_COUNT
Number of ratings for title on Audible.
From a [large audible dataset](https://github.com/elipickh/Audible_full_scraper)
663 in Chicago

### AUDIBLE_CATEGORY
Category ("genre") assigned on Audible
From a [large audible dataset](https://github.com/elipickh/Audible_full_scraper)
663 in Chicago

### TRANSLATIONES
Number of translations for title as listed in [Index Translationum](https://www.unesco.org/xtrans/bsform.aspx), which lists translations in the period 1979-2019

5082 in Chicago > 0

### AUTH_PAGERANK
NB. Author-based

An author's "PageRank Complete" at Wikipedia, based on data from the [World Literature group)[https://arxiv.org/pdf/1701.00991.pdf] who used wikipedia page-ranks.
An author has a high PageRank if many other articles with a high PageRank link to it.

3558 in Chicago > 0


### RATING_DIST_DIC

Distributions of ratings per book on GoodReads. Numbers retrieved in November 2023.

They are saved as a dictionary in each row, where, e.g., '5': 300 means 300 ratings gave 5 stars, and so on for '4':300 etc. Note: keys are strings.

### i. User-lists

### GOODREADS_CLASSICS
Author-based
Authors mentioned on [the Goodreads-classics-list](https://www.goodreads.com/shelf/show/classics) are marked  1.

62 in Chicago

### GOODREADS BEST 20TH CENTURY BOOKS
Author-based
Authors mentioned on [The Best Books of the 20th Century list](https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century) are marked  1.

44 in Chicago

##

## Expert-based

<br>

## Lists

### OPENSYLLABUS
Author-based
Works that also appear in the top 1000 titles on [the Opensyllabus list of English Literature](https://opensyllabus.org/result/field?id=English+Literature) are marked  1. 

477 in Chicago

### NORTON_ENGLISH
Author-based
Authors mentioned in the 10th edition of the Norton Anthology of English Literature (British & American literature) are marked  1.

339 in Chicago

### NORTON_AMERICAN
Author-based
Authors mentioned in the 10th edition of the Norton Anthology of American Literature are marked  1.

62 in Chicago

### NORTON
Author-based
Norton english and Norton american combined

401 in Chicago

### PENGUIN_CLASSICS_SERIES_TITLEBASED
Title-based
Titles that have been published in [the Penguin Classics series](https://www.penguin.com/penguin-classics-overview/)
(1326 titles in total)

77 in Chicago

### PENGUIN_CLASSICS_SERIES_AUTHORBASED
Author-based
Authors that have been published in [the Penguin Classics series](https://www.penguin.com/penguin-classics-overview/)
(1326 titles in total)

335 in Chicago


### PUBLISHERS_WEEKLY_BESTSELLERS
Title-based

Extracted from: [database of 20th-century American bestsellers via Publishers Weekly (1900-1999)](https://web.archive.org/web/20111014055658/http://www3.isrl.illinois.edu/~unsworth/courses/bestsellers/picked.books.cgi), collected by John Unsworth of University of Illinois.

176 in Chicago

### NYT_BESTSELLERS
Title-based

Extracted from: [database of New York Times Bestsellers (1931-2024)](http://www.hawes.com/pastlist.htm) compiled by Hawes Publications.

154 in Chicago

### BESTSELLERS
Merged from the "PUBLISHERS_WEEKLY_BESTSELLERS" and the "NYT_BESTSELLERS"

228 in Chicago

##

<br>

## Awards

## i. General
### NOBEL
Author-based
Nobel-prize winners works are marked 1.

85 in Chicago

### PULITZER
Longlisted works
Title-based
Works shortlisted (winners) for the Pulitzer Prize are marked W, and works that were longlisted (finalists) are marked F.

53 in Chicago

### NBA
Longlisted works for the National Book Award
Title-based
Works shortlisted (winners) for the NBA are marked W, and works that were longlisted (finalists) are marked F.

108 in Chicago

## ii. Sci-fi
### HUGO
Longlisted works
Title-based

(1953-2022)
Works shortlisted (winners) for the Hugo Awards are marked W, and works that were longlisted (finalists) are marked F.

96 in Chicago

### LOCUS_SCIFI
Shortlisted works (Scifi)
Title-based
Locus award for best scifi novel 1980-2022

12 in Chicago

### NEBULA
Longlisted works (Scifi)
Title-based

Nebula awards 1966-2022

92 in Chicago

### PHILIP_K_DICK_AWARD
Longlisted works (Scifi)
Title-based

US Scifi award 1982-2022

4 in Chicago

### J_W_CAMPBELL_AWARD
Longlisted works (Scifi)
Title-based

Scifi award 1973-2022

35 in Chicago

### PROMETHEUS_AWARD
Longlisted works (Scifi)
Title-based

US "libertarian" scifi award 1979-2022

20 in Chicago

## iii. Fantasy
### LOCUS_FANTASY
Shortlisted works
Title-based

5 in Chicago

### BFA
Shortlisted works
Title-based
British Fantasy Awards (aka. the August Derleth Fantasy Award) 1972-2022

3 in Chicago

### WORLD_FANTASY_AWARD
Longlisted works
Title-based

Fantasy award 1975-2022

28 in Chicago

### MYTHOPOEIC_AWARDS
Longlisted works (Fantasy)
Title-based

US fantasy award 1971-2022

5 in Chicago

## iv. Horror
### LOCUS_HORROR
Shortlisted works
Title-based

Locus awards for horror fiction/dark fantasy (1989-2022)

5 in Chicago

### BRAM_STOKER_AWARD
Longlisted works
Title-based

Award for dark & horror fiction (1987-2022)

14 in Chicago


## v. Mystery
### EDGAR_AWARDS
Shortlisted works (Mystery (Crime, etc.))

10 in Chicago


## vi. Umbrella-categories
### SCIFI_AWARDS
Title-based

Combination of 'NEBULA', 'LOCUS_SCIFI', 'HUGO', 'PHILIP_K_DICK_AWARD', 'J_W_CAMPBELL_AWARD', 'PROMETHEUS_AWARD'

163 in Chicago

### HORROR_AWARDS
Title-based

Combination of 'BRAM_STOKER_AWARD', 'LOCUS_HORROR'

19 in Chicago

### FANTASY_AWARDS
Title-based

Combination of 'LOCUS_FANTASY', 'BFA', 'WORLD_FANTASY_AWARD', 'MYTHOPOEIC_AWARDS'

40 in Chicago

### ROMANTIC AWARDS
Author-based

Combination of 'RITA_AWARDS_AUTH' or 'RONA_AWARDS_AUTH'

54 in Chicago

##

# Extra

### GENDER
Collected by using genderize

### DECADE
Just publication date by decade

### GR_BOOK_ID
IDs of the books as they are assigned on GoodReads. Retrieved in November 2023.
