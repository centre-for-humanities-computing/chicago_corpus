
# The Chicago Corpus [![Static Badge](https://img.shields.io/badge/acl-LREC-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAABwAgMAAADkn5ORAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAlQTFRFAAAA7R4k7RwkoncKaQAAAAF0Uk5TAEDm2GYAAAAJcEhZcwAACxMAAAsTAQCanBgAAAJVSURBVFjD7Zc7ksMwDEPTpMnptmGD023DhqdcApCT2NvYnJTxTH7K09CiSAi+3b7X23VHIQLxQbAiA/lREJFAzsCIyOQLUZVcQvCjYx9CnwZLYxwuENI0zUZNQUbtmw8mJHsePzt6z5qBDVX/lcxwpXZO6a4enoFKSFZTvRoCXIuwnIJgVKAa1JqgdTSHIahUdIq6CHQTTDTSuZ+B/ZuJ8ZqwtpOz+3ZmYJaKIXLVG/evv2pwBopy0MVoN8GJM1D5SFc/3AX9zowFZqAiKT+K6mrztCHIPoCaQcrEmGyJXmPmDOwKcBmk+iHUXKW5QzBiKwgo3SFFgMJPQQ7Gz/vYfaEzEJSRxO8O5NTCELTS1TF0/ivc06AkL2sX+hFWwiFIpas8gCGNmYFSThwTLiWoGahujUN6WgBZJ0NQ+o4d+IDldAaGy3aXHpZZK3XOQGvefgvvkqwYgrQEnfE9WBKCGIJs/8MWPiQEmIIUpWNRgCdoDUElgoUqRUke7kjLtIafAn0a1Flhped/9g2wQZLLyasgj9yKzXj55JT4ydvgJSznwfZuPVQRyxttJ6jekNdBtb+NUdhplY4O9jDLpa6DaQcn/1aAK8xHk/J1HWRM0CF5gg63lS2b2eugV2LpxMr+2td3m3QN1OazIGwNZbyWMrzq8SxYKzRrNL0OuTme9/I0cRVMLIte9gnhHijXbb0WcxpUPGCVlsL1Uio2h/N8WDkN2nLRc0HGCzov5Wwq483KnQZ1mtlZOtjm5NxwhQmY6zGiKFd6GGCr5noOyKvg9/peo+sPhLv+BGIWS+UAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTMtMDgtMDRUMjE6NTc6MjkrMDg6MDAj62PfAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDEzLTA4LTA0VDIxOjU3OjI5KzA4OjAwUrbbYwAAAABJRU5ErkJggg==)]() <a href="https://centre-for-humanities-computing.github.io/fabula-net/"><img src="https://github.com/yuri-bizzoni/EmoArc/raw/main/static/fabulanet_logo.png" width="15%" align="right" /></a>

As part of the efforts of the [Fabula-NET project](https://centre-for-humanities-computing.github.io/fabula-net/) at the Center for Humanities Computing, Aarhus University, we present a dataset of quality judgments on 9,000 19th and 20th century English-language literary novels by 3,166 predominantly Anglophone authors.


The data includes annotation of expert opinions and crowd-basedresources to allow comparative analyses between different literary quality evaluations, as well as several textual metrics chosen for their  connection with literary reception. 

©️ A large part of the corpus is subjected to copyright (see the available works [here](https://artflsrv04.uchicago.edu/philologic4.7/chicago_novel_corpus_pre1923_12-20/)). **We release quality and reception measures together with stylometric and sentiment data** for each of the 9,000 novels to promote future research and comparison.

<br>


## ⚡ Data included

- 9,000 titles
- Author, title & year
- Various textual metrics
- Various reception metrics

For an overview of all included data, see the corpus [documentation](https://github.com/centre-for-humanities-computing/chicago_corpus/blob/66da8be26cfccb3c24c16abcf003d10695e34385/data/corpus_description.md).

Available formats: [.xlsx](https://docs.google.com/spreadsheets/d/1mIMZw1dcoVZOQX3qtPOTmzmQZ9vm7dK1Sj2eZcgArvA/edit?usp=sharing), [.json](https://github.com/centre-for-humanities-computing/chicago_corpus/raw/main/data/CHICAGO_CORPUS_DATA.json)

<br>

## 🔍 Example

| BOOK_ID          |      TITLE      |   AUTH_FIRST       | AUTH_LAST | PUBL_DATE    | ... |    AVG_RATING    | SCIFI_AWARDS   | PULITZER | TRANSLATIONS |  ... | PERPLEXITY | MEAN_SENT | READABILITY |
| ---------------- | --------------- |------------------- |-----------|--------------|-----|------------------|----------------|----------|--------------|------|------------|-----------|-------------|
| 6913             |A Clash of Kings |   George R. R.     | Martin    |      1999    | ... |     4.41         |        1       |   0      |     38       |  ... |       79.97|  -0.002   | 92.73       |
| 20636            |  Dune           |   Frank            | Herbert   |      1965    | ... |    4.25         |        1       |   0      |     398      |  ... | 72.74      |  -0.007   | 85.18       |
| 22741            |  Beloved        |   Toni             | Morrison  |      1987    | ... |     3.92         |        0       |   1      |     68       |  ... | 68.78      |   0.030   | 91.71       |
| 5778             |  Misery         |   Stephen          | King      |      1987    | ... |     4.20         |        0       |   0      |     74       |  ... | 68.09      |  -0.032   | 82.54       |
| 86               |  The Portrait of a Lady |   Henry    | James     |      1881    | ... |     3.78         |        0       |   0      |     53       |  ... | 80.35      |   0.150   | 71.65       |

**Above**: _Example of titles and corresponding values for selected metrics_

<br>

## 📈 Corpus statistics

<img src="https://github.com/centre-for-humanities-computing/chicago_corpus/raw/main/documentation/img/chicago_wordcount.png" width="45%" align="right" />

The corpus of texts from which we constructed our dataset was assembled by Hoyt Long and Richard Jean So in the [Textual Optics Lab](https://textual-optics-lab.uchicago.edu/us_novel_corpus); it encompasses 9088 novels published in the United States between 1880 and 2000 and was compiled based on the number of libraries holding each title (based on the [WorldCat](https://search.worldcat.org) catalogue), favoring works with a higher number of library holdings. 

<br>

|          Titles    |           Authors                |           Titles per author                                               |
| -------------------------- | --------------------| -------------------------------------------------------------- |
|      9088     |   3166    |   2.88    | 

**Above**: _Number of titles/authors in the corpus_

<br>


**Below**: _Mean & SD of some of the included features_

| Metric               |   Wordcount |   Sentence Length |   Wordlength |   Type/Token Ratio |   Compressibility |   Bigram Entropy |   Word Entropy |   Flesch Ease |   Dale Chall New |   Mean Sentiment |   Std Sentiment |   End Sentiment |   Beginning Sentiment |   Hurst Exponent |   Approximate Entropy |
|----------------------|-------------|-------------------|--------------|--------------------|-------------------|-------------------|-----------------|----------------|------------------|------------------|-----------------|----------------|------------------------|-------------------|-------------------------|
| Mean (µ)             |    118584.71 |              86.56 |         3.67 |               0.69 |              2.92 |             14.63 |            9.69 |          82.70 |              5.10 |             0.03 |            0.35 |            0.03 |                   0.04 |              0.61 |                    1.75 |
| St. dev. (±)         |     64746.05 |              29.44 |         0.18 |               0.02 |              0.14 |              0.55 |            0.30 |           6.48 |              0.33 |             0.04 |            0.04 |            0.07 |                   0.05 |              0.04 |                    0.15 |


<br>

## 🏆 "Quality", "reader appreciation" or "popularity" metrics

<img src="https://github.com/centre-for-humanities-computing/chicago_corpus/raw/main/documentation/img/proxies_counts.png" width="62%" align="right" />

Beyond textual features, we present various **"quality proxies"**, that is, ways of estimating valuation in literary culture, such as whether or not titles are included in Bestseller or Canon lists. We also include what we call "continuous" proxies, that is, scores per title, for example of GoodReads ratings or translation numbers (see the corpus [documentation](https://github.com/centre-for-humanities-computing/chicago_corpus/blob/66da8be26cfccb3c24c16abcf003d10695e34385/data/corpus_description.md)).

Because of the library holdings selection criteria, the corpus comprises much high-quality fiction from authors who have received prestigious distinctions, such as the Nobel Prize (i.a., Toni Morrison), the National Book Award (i.a., Don DeLillo). Yet, library holdings appear to indicate **both high distinction and mass popularity**, reflecting library users' demand and preferences. So the corpus also comprises widely popular novels from mainstream literature (i.a., Agatha Christie), and notable works on the broad spectrum of so-called "genre literature", from Mystery to Science Fiction (i.a., Tolkien, Philip K. Dick etc.). An examination of the relation between various proxies in this corpus is [forthcoming](https://jcls.io/site/ccls2024/).

<br>

## 📖 Documentation


|              |                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------- |
| 📄 **[Paper]**              | The Chicago resource paper.                                                        |
| 📚 **[Citation]**           | Bibtex citation.                                                              | 
| 🗂️ **[Previous works]**           | Publications that have previously used the Chicago Corpus.                                                              | 
| 🔬 **[Textual Optics Lab]**           | The Chicago Corpus at the Textual Optics Lab, University of Chicago.                                                              | 



[Paper]: https://github.com/centre-for-humanities-computing/chicago_corpus/blob/3822b3f2d29775f7565c982b7bdaad160a6153ac/documentation/LREC_COLING_2024_CHICAGO.pdf
[Citation]: https://github.com/centre-for-humanities-computing/chicago_corpus/blob/8b813a9b904d7293853fdae28adb884f753bd9bd/documentation/citation.bib
[Previous works]: https://github.com/centre-for-humanities-computing/chicago_corpus/blob/e5e4762e05020f7ea1518a03d6680133c98dddf6/documentation/chicago_publications.md
[Textual Optics Lab]: https://textual-optics-lab.uchicago.edu/us_novel_corpus






