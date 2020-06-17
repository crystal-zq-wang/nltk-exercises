##### NLTK CHAPTER 2 NOTES & EXERCISES #####

if we want to use the methods in nltk.book, we would do something like this:
	emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
	emma.concordance("surprize")

### NOTES (nltk.corpus methods) ###

fileids(): the files of the corpus

fileids([categories]): the files of the corpus corresponding to these categories

categories(): the categories of the corpus

categories([fileids]): the categories of the corpus corresponding to these files

raw(): the raw content of the corpus

raw("some text here"): gives us the contents of the file without any linguistic processing; a call to
	len(raw(text)) would give us the number of characters in that text without tokenization (includes spaces)

raw(fileids=[f1,f2,f3]): the raw content of the specified files

raw(categories=[c1,c2]): the raw content of the specified categories

words(): the words of the whole corpus

words("some text here" or list of file ids or list of categories): pretty much a transcript of the given text, 
	tokenized into a list

words(fileids=[f1,f2,f3]): the words of the specified fileids

words(categories=[c1,c2]): the words of the specified categories

sents(): the sentences of the whole corpus

sents("some text here" or list of categories): divides the text up into its sentences, where each sentence is a list of words 
	and punctuation

sents(fileids=[f1,f2,f3]): the sentences of the specified fileids

sents(categories=[c1,c2]): the sentences of the specified categories

abspath(fileid): the location of the given file on disk

encoding(fileid): the encoding of the file (if known)

open(fileid): open a stream for reading the given corpus file

root: if the path to the root of locally installed corpus

readme(): the contents of the README file of the corpus


### NOTES (nltk methods)

ConditionalFreqDist((the condition, the thing we take action on)
				for item in condition
				for object in thing to take action on
				... extra if conditions) 
	# the tuple is basically a condition-thing pair, like (English, 4) for (language, len(word))
	# ConditionalFreqDist takes in a list of pairs as input

cfdist.conditions(): the conditions

cfdist[condition]: the frequency distribution for this condition

cfdist[condition][sample]: frequency for the given sample of this condition

cfdist.tabulate(): tabulate the conditional frequency distribution

cfdist.tabulate(samples, conditions): tabulation limited to the specified samples and conditions

cfdist.plot(): graphical plot of the conditional frequency distribution

cfdist.plot(samples, conditions): graphical plot limited to the specified samples and conditions

cfdist1 < cfdist2: test if samples in cfdist1 occur less frequently than in cfdist2

# A collection of frequency distributions for a single experiment run under different conditions. Conditional frequency 
# 	distributions are used to record the number of times each sample occurred, given the condition under which the experiment 
#	was run. For example, a conditional frequency distribution could be used to record the frequency of each word (type) in a 
#	document, given its length.

# can make a plot cumulative with plot(cumulative=True)

LOADING OWN CORPUS:

>>> from nltk.corpus import PlaintextCorpusReader #BracketParseCorpusReader gets a little more specific, can use sents
>>> corpus_root = # my nltk-exercises repository filepath
>>> wordlists = PlaintextCorpusReader(corpus_root, 'tester.txt')
>>> wordlists.fileids()
['tester.txt']
>>> wordlists.words("tester.txt")
['hi', 'there', 'swinging', 'eating', 'x', 'y', 'zing', ...]

# 1.3 Your Turn
humor_text = brown.words(categories="humor")
fdist = nltk.FreqDist(w.lower() for w in humor_text)
wh_words = [w for w in fdist if w.startswith("wh")]
for m in wh_words:
	print(m + ':', fdist[m], end=' ')

>>> which: 62 when: 62 who: 49 what: 46 where: 16 while: 15 why: 13 whole: 10 whose: 8 white: 5 whether: 5 whom: 4 
	whenever: 4 whatever: 2 what's: 2 whiskey: 2 whisky: 1 whispered: 1 whichever: 1 who's: 1 wheezes: 1 whereupon: 1 
	wherever: 1 whimper: 1 wheel: 1 whosoever: 1

# 2.3 Your Turn
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
cfd = nltk.ConditionalFreqDist(
		(genre, word)
     	for genre in brown.categories()
     	for word in brown.words(categories=genre)
     	if genre in ["romance", "news"])
cfd.tabulate(samples=days)
>>> 		Monday   Tuesday Wednesday  Thursday    Friday  Saturday    Sunday 
   news        54        43        22        20        41        33        51 
romance         2         3         3         1         3         4         5 

## will continue starting from section 2.4


