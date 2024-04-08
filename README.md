
# The Chicago Corpus [![Static Badge](https://img.shields.io/badge/acl-LREC-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAABwAgMAAADkn5ORAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAlQTFRFAAAA7R4k7RwkoncKaQAAAAF0Uk5TAEDm2GYAAAAJcEhZcwAACxMAAAsTAQCanBgAAAJVSURBVFjD7Zc7ksMwDEPTpMnptmGD023DhqdcApCT2NvYnJTxTH7K09CiSAi+3b7X23VHIQLxQbAiA/lREJFAzsCIyOQLUZVcQvCjYx9CnwZLYxwuENI0zUZNQUbtmw8mJHsePzt6z5qBDVX/lcxwpXZO6a4enoFKSFZTvRoCXIuwnIJgVKAa1JqgdTSHIahUdIq6CHQTTDTSuZ+B/ZuJ8ZqwtpOz+3ZmYJaKIXLVG/evv2pwBopy0MVoN8GJM1D5SFc/3AX9zowFZqAiKT+K6mrztCHIPoCaQcrEmGyJXmPmDOwKcBmk+iHUXKW5QzBiKwgo3SFFgMJPQQ7Gz/vYfaEzEJSRxO8O5NTCELTS1TF0/ivc06AkL2sX+hFWwiFIpas8gCGNmYFSThwTLiWoGahujUN6WgBZJ0NQ+o4d+IDldAaGy3aXHpZZK3XOQGvefgvvkqwYgrQEnfE9WBKCGIJs/8MWPiQEmIIUpWNRgCdoDUElgoUqRUke7kjLtIafAn0a1Flhped/9g2wQZLLyasgj9yKzXj55JT4ydvgJSznwfZuPVQRyxttJ6jekNdBtb+NUdhplY4O9jDLpa6DaQcn/1aAK8xHk/J1HWRM0CF5gg63lS2b2eugV2LpxMr+2td3m3QN1OazIGwNZbyWMrzq8SxYKzRrNL0OuTme9/I0cRVMLIte9gnhHijXbb0WcxpUPGCVlsL1Uio2h/N8WDkN2nLRc0HGCzov5Wwq483KnQZ1mtlZOtjm5NxwhQmY6zGiKFd6GGCr5noOyKvg9/peo+sPhLv+BGIWS+UAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTMtMDgtMDRUMjE6NTc6MjkrMDg6MDAj62PfAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDEzLTA4LTA0VDIxOjU3OjI5KzA4OjAwUrbbYwAAAABJRU5ErkJggg==)]() <a href="https://centre-for-humanities-computing.github.io/fabula-net/"><img src="https://github.com/yuri-bizzoni/EmoArc/raw/main/static/fabulanet_logo.png" width="15%" align="right" /></a>

<br>


## ⚡ Data included

- Data for 9,000 titles
- Author, title & year

<br>

## 🔍 Example

| BOOK_ID          |      TITLE      |   AUTH_FIRST       | AUTH_LAST | PUBL_DATE    |     ARC_ang         | ARC_fea        | ... | INTENS_ang |  INTENS_joy | ...    |
| ---------------- | --------------- |------------------- |-----------|--------------|---------------------|----------------|-----|------------|-------------|--------|
| 25732            |  Infinite Jest  |   David Foster     | Wallace   |      1996    |     0.758,0.901...  | 1.451,1.601... | ... | 70.44      |  102.37     | ...    |
| 20636            |  Dune           |   Frank            | Herbert   |      1965    |     2.918,5.031...  | 4.164,4.231... | ... | 89.95      |  92.39      | ...    |
| 22741            |  Beloved        |   Toni             | Morrison  |      1987    |     7.603,5.461...  | 7.806,6.235... | ... | 63.46      |  136.63     | ...    |
| 21974            |  The Gunslinger |   Stephen          | King      |      1982    |     2.627,0.581...  | 3.308,1.764... | ... | 84.02      |  102.07     | ...    |
| 86               |  The Portrait of a Lady |   Henry    | James     |      1881    |     0.792,4.212...  | 2.381,4.672... | ... | 40.59      |  169.74     | ...    |


<br>

## 📈 Corpus statistics

<img src="https://github.com/centre-for-humanities-computing/chicago_corpus/raw/main/documentation/chicago_wordcount.png" width="45%" align="right" />


<br>

<br>

|          Titles    |           Authors                |           Titles per author                                               |
| -------------------------- | --------------------| -------------------------------------------------------------- |
|      9088     |   3166    |   2.88    | 

**Above**: Number of titles/authors in the corpus

<br>

**Below**: Mean & SD of some of the included features

|                  |    Mean (µ) |   St. dev. (±) |
|------------------|---------|--------|
| Wordcount        | 118584.71 | 64746.05 |
| Sentence Length  |    86.56 |   29.44 |
| Wordlength       |     3.67 |    0.18 |
| Type/Token Ratio        |     0.69 |    0.02 |
| Compressibility  |     2.92 |    0.14 |
| Bigram Entropy   |    14.63 |    0.55 |
| Word Entropy     |     9.69 |    0.30 |
| Flesch Ease      |    82.70 |    6.48 |
| Dale Chall New   |     5.10 |    0.33 |
| Mean Sentiment       |     0.03 |    0.04 |
| Std Sentiment         |     0.35 |    0.04 |
| End Sentiment        |     0.03 |    0.07 |
| Beginning Sentiment  |     0.04 |    0.05 |
| Hurst Exponent   |     0.61 |    0.04 |
| Approximate Entropy |  1.75 |    0.15 |


<br>

## 📖 Documentation


|              |                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------- |
| 📄 **[Paper]**              | The Chicago resource paper.                                                        |
| 📚 **[Citation]**           | Bibtex citation.                                                              | 
| 🗂️ **[Previous works]**           | Publications that have previously used the corpus.                                                              | 
| 🔬 **[Textual Optics Lab]**           | The website of the corpus at the Textual Optics Lab, University of Chicago.                                                              | 



[Paper]: https://aclanthology.org/2024.latechclfl-1.7.pdf
[Citation]: https://github.com/yuri-bizzoni/EmoArc/raw/main/citation.txt
[Previous works]: https://textual-optics-lab.uchicago.edu/us_novel_corpus
[Textual Optics Lab]: https://textual-optics-lab.uchicago.edu/us_novel_corpus


```yml
```





